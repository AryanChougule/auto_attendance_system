
# 🎓 Smart Attendance System using Face Recognition

Welcome to the future of attendance — fully automated, AI-powered, and camera-friendly.  
This project enables schools, colleges, and institutions to **mark attendance from group images or videos** using **face recognition** — all within a simple web interface.

> Built with 💡 MTCNN + ArcFace | Powered by Streamlit | Easy to deploy and use

---

## 🚀 Features

✅ Detects multiple faces in a single image  
✅ Verifies identity using powerful ArcFace model  
✅ Automatically logs attendance in CSV format  
✅ Upload support for images (video support coming soon)  
✅ Web-friendly GUI powered by **Streamlit**  
✅ Dataset organized using Student IDs  
✅ Easy to deploy, test, and scale

---

## 🖼️ How It Works

1. **Upload a group image**
2. Faces are detected using **MTCNN**
3. Each detected face is compared using **ArcFace**
4. If matched, student ID is logged as **present**
5. Results are saved to a downloadable **CSV file**

---

## 📁 Project Structure

```
face-attendance-app/
├── app.py               # Streamlit app code
├── requirements.txt     # Python dependencies
├── raw_dataset/         # Student ID folders with face images
│   ├── 1234/
│   │   └── 1.jpg
│   ├── 2217008/
│   │   └── 1.jpg
├── attendance_logs/     # Auto-created attendance CSVs
```

🗂️ **Dataset format**:
Organize student images like so:
```
raw_dataset/
├── <student_id>/
│   ├── image1.jpg
│   ├── image2.jpg
```

---

## 🧠 Tech Stack

| Layer     | Tool         |
|-----------|--------------|
| 🧠 Face Recognition | [ArcFace](https://arxiv.org/abs/1801.07698) via DeepFace |
| 🕵️ Face Detection   | MTCNN |
| 🖥️ Interface        | Streamlit |
| 📦 Storage          | CSV (can be scaled to database) |
| 🧪 Testing Ground   | Kaggle (initial dev), Streamlit Cloud (deployment) |

---

## 💻 Running Locally

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/face-attendance-app.git
cd face-attendance-app

# 2. (Optional) Setup virtual environment
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows

# 3. Install dependencies
pip install -r requirements.txt

# 4. Launch the app
streamlit run app.py
```

---

## 🌍 Deploying on Streamlit Cloud

1. Push your code to a **public GitHub repo**
2. Go to [streamlit.io/cloud](https://streamlit.io/cloud)
3. Click **New App**
4. Connect your GitHub repo
5. Set `app.py` as the entry point and deploy ✅

---

## 📊 Output Format

The app automatically generates an `attendance_logs/attendance_<n>.csv` file with the following structure:

| Student ID | Time                |
|------------|---------------------|
| 1234       | 2025-07-22 10:15:05 |
| 2217008    | 2025-07-22 10:15:05 |

You can download this file directly from the app.

---

## 📌 To-Do / Roadmap

- [ ] 📹 Add real-time video upload support
- [ ] 🧍 Show recognized names using `students.csv` mapping
- [ ] 🧠 Add liveness detection (anti-spoof)
- [ ] 📦 Connect to Firebase or PostgreSQL
- [ ] 📲 Build mobile-friendly frontend (React Native or Flutter)
- [ ] 🔐 Add admin login & secure API

---

## 🧠 Ideal Use Cases

- 🏫 Classroom attendance
- 🧑‍🏫 Faculty/Staff tracking
- 🏢 Company check-ins
- 🎤 Event participation verification

---

## 🙌 Credits

- [MTCNN](https://github.com/ipazc/mtcnn) for accurate multi-face detection
- [DeepFace](https://github.com/serengil/deepface) for simplifying face verification
- [Streamlit](https://streamlit.io) for the web UI magic

---

## 🛑 Disclaimer

This project is for **educational and prototyping purposes**.  
For real-world deployment, please consider adding:
- User authentication
- Encrypted databases
- Secure APIs and GDPR-compliant data practices

---

## 📬 Connect With Me

If you’re a school, developer, or investor looking to scale this:
- 📧 Email: yourname@example.com
- 🧠 LinkedIn: [your-profile](https://linkedin.com/in/aryanpravinchougule)
- ⭐ GitHub: [yourusername](https://github.com/AryanChougule)

---

_This project turns faces into futures. Let's automate, simplify, and innovate education._ 🧠📸
