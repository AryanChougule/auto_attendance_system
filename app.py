import streamlit as st
import cv2
import numpy as np
import tempfile
import os
from mtcnn import MTCNN
from deepface import DeepFace
import pandas as pd
from datetime import datetime
from PIL import Image

# Setup
RAW_DATASET_PATH = "raw_dataset"
OUTPUT_DIR = "attendance_logs"
os.makedirs(OUTPUT_DIR, exist_ok=True)
detector = MTCNN()

def detect_faces(image):
    results = detector.detect_faces(image)
    faces = []
    for res in results:
        x, y, w, h = res['box']
        x, y = abs(x), abs(y)
        face = image[y:y+h, x:x+w]
        faces.append(face)
    return faces

def recognize_faces(faces):
    recognized_ids = set()
    for face in faces:
        for student_id in os.listdir(RAW_DATASET_PATH):
            student_folder = os.path.join(RAW_DATASET_PATH, student_id)
            for img_file in os.listdir(student_folder):
                img_path = os.path.join(student_folder, img_file)
                result = DeepFace.verify(face, img_path, model_name="ArcFace", enforce_detection=False)
                if result["verified"]:
                    recognized_ids.add(student_id)
                    break
            else:
                continue
            break
    return recognized_ids

def get_next_csv_filename():
    files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith("attendance_") and f.endswith(".csv")]
    indices = [int(f.split("_")[1].split(".")[0]) for f in files if f.split("_")[1].split(".")[0].isdigit()]
    next_index = max(indices, default=0) + 1
    return os.path.join(OUTPUT_DIR, f"attendance_{next_index}.csv")

def save_attendance(student_ids):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    df = pd.DataFrame([{"Student ID": sid, "Time": timestamp} for sid in student_ids])
    path = get_next_csv_filename()
    df.to_csv(path, index=False)
    return path, df

# Streamlit UI
st.title("📸 Face Recognition Attendance System")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    with tempfile.NamedTemporaryFile(delete=False) as tmp:
        tmp.write(uploaded_file.read())
        file_path = tmp.name

    image = cv2.imread(file_path)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    faces = detect_faces(image)
    st.subheader(f"Detected {len(faces)} face(s)")

    for i, face in enumerate(faces):
        st.image(cv2.cvtColor(face, cv2.COLOR_BGR2RGB), caption=f"Face {i+1}", width=150)

    student_ids = recognize_faces(faces)

    if student_ids:
        st.success(f"Recognized Students: {', '.join(student_ids)}")
        csv_path, df = save_attendance(student_ids)
        st.download_button("Download Attendance CSV", data=df.to_csv(index=False), file_name=os.path.basename(csv_path))
    else:
        st.warning("No known students matched.")
