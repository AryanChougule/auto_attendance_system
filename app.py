{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "8ebd7bae",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:16:45.897400Z",
     "iopub.status.busy": "2025-07-28T18:16:45.897149Z",
     "iopub.status.idle": "2025-07-28T18:16:51.729916Z",
     "shell.execute_reply": "2025-07-28T18:16:51.728940Z"
    },
    "papermill": {
     "duration": 5.838371,
     "end_time": "2025-07-28T18:16:51.731169",
     "exception": false,
     "start_time": "2025-07-28T18:16:45.892798",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting mtcnn\r\n",
      "  Downloading mtcnn-1.0.0-py3-none-any.whl.metadata (5.8 kB)\r\n",
      "Requirement already satisfied: joblib>=1.4.2 in /usr/local/lib/python3.11/dist-packages (from mtcnn) (1.5.1)\r\n",
      "Collecting lz4>=4.3.3 (from mtcnn)\r\n",
      "  Downloading lz4-4.4.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl.metadata (3.8 kB)\r\n",
      "Downloading mtcnn-1.0.0-py3-none-any.whl (1.9 MB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.9/1.9 MB\u001b[0m \u001b[31m24.2 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading lz4-4.4.4-cp311-cp311-manylinux_2_17_x86_64.manylinux2014_x86_64.whl (1.3 MB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m1.3/1.3 MB\u001b[0m \u001b[31m51.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hInstalling collected packages: lz4, mtcnn\r\n",
      "Successfully installed lz4-4.4.4 mtcnn-1.0.0\r\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install mtcnn"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "28bddca6",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:16:51.738712Z",
     "iopub.status.busy": "2025-07-28T18:16:51.738454Z",
     "iopub.status.idle": "2025-07-28T18:16:58.109844Z",
     "shell.execute_reply": "2025-07-28T18:16:58.108946Z"
    },
    "papermill": {
     "duration": 6.376441,
     "end_time": "2025-07-28T18:16:58.111102",
     "exception": false,
     "start_time": "2025-07-28T18:16:51.734661",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Collecting deepface\r\n",
      "  Downloading deepface-0.0.93-py3-none-any.whl.metadata (30 kB)\r\n",
      "Requirement already satisfied: requests>=2.27.1 in /usr/local/lib/python3.11/dist-packages (from deepface) (2.32.4)\r\n",
      "Requirement already satisfied: numpy>=1.14.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (1.26.4)\r\n",
      "Requirement already satisfied: pandas>=0.23.4 in /usr/local/lib/python3.11/dist-packages (from deepface) (2.2.3)\r\n",
      "Requirement already satisfied: gdown>=3.10.1 in /usr/local/lib/python3.11/dist-packages (from deepface) (5.2.0)\r\n",
      "Requirement already satisfied: tqdm>=4.30.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (4.67.1)\r\n",
      "Requirement already satisfied: Pillow>=5.2.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (11.2.1)\r\n",
      "Requirement already satisfied: opencv-python>=4.5.5.64 in /usr/local/lib/python3.11/dist-packages (from deepface) (4.11.0.86)\r\n",
      "Requirement already satisfied: tensorflow>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (2.18.0)\r\n",
      "Requirement already satisfied: keras>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (3.8.0)\r\n",
      "Requirement already satisfied: Flask>=1.1.2 in /usr/local/lib/python3.11/dist-packages (from deepface) (3.1.1)\r\n",
      "Collecting flask-cors>=4.0.1 (from deepface)\r\n",
      "  Downloading flask_cors-6.0.1-py3-none-any.whl.metadata (5.3 kB)\r\n",
      "Requirement already satisfied: mtcnn>=0.1.0 in /usr/local/lib/python3.11/dist-packages (from deepface) (1.0.0)\r\n",
      "Collecting retina-face>=0.0.1 (from deepface)\r\n",
      "  Downloading retina_face-0.0.17-py3-none-any.whl.metadata (10 kB)\r\n",
      "Collecting fire>=0.4.0 (from deepface)\r\n",
      "  Downloading fire-0.7.0.tar.gz (87 kB)\r\n",
      "\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m87.2/87.2 kB\u001b[0m \u001b[31m3.6 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25h  Preparing metadata (setup.py) ... \u001b[?25l\u001b[?25hdone\r\n",
      "Collecting gunicorn>=20.1.0 (from deepface)\r\n",
      "  Downloading gunicorn-23.0.0-py3-none-any.whl.metadata (4.4 kB)\r\n",
      "Requirement already satisfied: termcolor in /usr/local/lib/python3.11/dist-packages (from fire>=0.4.0->deepface) (3.1.0)\r\n",
      "Requirement already satisfied: blinker>=1.9.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (1.9.0)\r\n",
      "Requirement already satisfied: click>=8.1.3 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (8.2.1)\r\n",
      "Requirement already satisfied: itsdangerous>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (2.2.0)\r\n",
      "Requirement already satisfied: jinja2>=3.1.2 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (3.1.6)\r\n",
      "Requirement already satisfied: markupsafe>=2.1.1 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (3.0.2)\r\n",
      "Requirement already satisfied: werkzeug>=3.1.0 in /usr/local/lib/python3.11/dist-packages (from Flask>=1.1.2->deepface) (3.1.3)\r\n",
      "Requirement already satisfied: beautifulsoup4 in /usr/local/lib/python3.11/dist-packages (from gdown>=3.10.1->deepface) (4.13.4)\r\n",
      "Requirement already satisfied: filelock in /usr/local/lib/python3.11/dist-packages (from gdown>=3.10.1->deepface) (3.18.0)\r\n",
      "Requirement already satisfied: packaging in /usr/local/lib/python3.11/dist-packages (from gunicorn>=20.1.0->deepface) (25.0)\r\n",
      "Requirement already satisfied: absl-py in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (1.4.0)\r\n",
      "Requirement already satisfied: rich in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (14.0.0)\r\n",
      "Requirement already satisfied: namex in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (0.1.0)\r\n",
      "Requirement already satisfied: h5py in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (3.14.0)\r\n",
      "Requirement already satisfied: optree in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (0.16.0)\r\n",
      "Requirement already satisfied: ml-dtypes in /usr/local/lib/python3.11/dist-packages (from keras>=2.2.0->deepface) (0.4.1)\r\n",
      "Requirement already satisfied: joblib>=1.4.2 in /usr/local/lib/python3.11/dist-packages (from mtcnn>=0.1.0->deepface) (1.5.1)\r\n",
      "Requirement already satisfied: lz4>=4.3.3 in /usr/local/lib/python3.11/dist-packages (from mtcnn>=0.1.0->deepface) (4.4.4)\r\n",
      "Requirement already satisfied: mkl_fft in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (1.3.8)\r\n",
      "Requirement already satisfied: mkl_random in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (1.2.4)\r\n",
      "Requirement already satisfied: mkl_umath in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (0.1.1)\r\n",
      "Requirement already satisfied: mkl in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (2025.2.0)\r\n",
      "Requirement already satisfied: tbb4py in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (2022.2.0)\r\n",
      "Requirement already satisfied: mkl-service in /usr/local/lib/python3.11/dist-packages (from numpy>=1.14.0->deepface) (2.4.1)\r\n",
      "Requirement already satisfied: python-dateutil>=2.8.2 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.23.4->deepface) (2.9.0.post0)\r\n",
      "Requirement already satisfied: pytz>=2020.1 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.23.4->deepface) (2025.2)\r\n",
      "Requirement already satisfied: tzdata>=2022.7 in /usr/local/lib/python3.11/dist-packages (from pandas>=0.23.4->deepface) (2025.2)\r\n",
      "Requirement already satisfied: charset_normalizer<4,>=2 in /usr/local/lib/python3.11/dist-packages (from requests>=2.27.1->deepface) (3.4.2)\r\n",
      "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.11/dist-packages (from requests>=2.27.1->deepface) (3.10)\r\n",
      "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.11/dist-packages (from requests>=2.27.1->deepface) (2.5.0)\r\n",
      "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.11/dist-packages (from requests>=2.27.1->deepface) (2025.6.15)\r\n",
      "Requirement already satisfied: astunparse>=1.6.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (1.6.3)\r\n",
      "Requirement already satisfied: flatbuffers>=24.3.25 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (25.2.10)\r\n",
      "Requirement already satisfied: gast!=0.5.0,!=0.5.1,!=0.5.2,>=0.2.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (0.6.0)\r\n",
      "Requirement already satisfied: google-pasta>=0.1.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (0.2.0)\r\n",
      "Requirement already satisfied: libclang>=13.0.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (18.1.1)\r\n",
      "Requirement already satisfied: opt-einsum>=2.3.2 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (3.4.0)\r\n",
      "Requirement already satisfied: protobuf!=4.21.0,!=4.21.1,!=4.21.2,!=4.21.3,!=4.21.4,!=4.21.5,<6.0.0dev,>=3.20.3 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (3.20.3)\r\n",
      "Requirement already satisfied: setuptools in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (75.2.0)\r\n",
      "Requirement already satisfied: six>=1.12.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (1.17.0)\r\n",
      "Requirement already satisfied: typing-extensions>=3.6.6 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (4.14.0)\r\n",
      "Requirement already satisfied: wrapt>=1.11.0 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (1.17.2)\r\n",
      "Requirement already satisfied: grpcio<2.0,>=1.24.3 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (1.73.1)\r\n",
      "Requirement already satisfied: tensorboard<2.19,>=2.18 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (2.18.0)\r\n",
      "Requirement already satisfied: tensorflow-io-gcs-filesystem>=0.23.1 in /usr/local/lib/python3.11/dist-packages (from tensorflow>=1.9.0->deepface) (0.37.1)\r\n",
      "Requirement already satisfied: wheel<1.0,>=0.23.0 in /usr/local/lib/python3.11/dist-packages (from astunparse>=1.6.0->tensorflow>=1.9.0->deepface) (0.45.1)\r\n",
      "Requirement already satisfied: markdown>=2.6.8 in /usr/local/lib/python3.11/dist-packages (from tensorboard<2.19,>=2.18->tensorflow>=1.9.0->deepface) (3.8.2)\r\n",
      "Requirement already satisfied: tensorboard-data-server<0.8.0,>=0.7.0 in /usr/local/lib/python3.11/dist-packages (from tensorboard<2.19,>=2.18->tensorflow>=1.9.0->deepface) (0.7.2)\r\n",
      "Requirement already satisfied: soupsieve>1.2 in /usr/local/lib/python3.11/dist-packages (from beautifulsoup4->gdown>=3.10.1->deepface) (2.7)\r\n",
      "Requirement already satisfied: intel-openmp<2026,>=2024 in /usr/local/lib/python3.11/dist-packages (from mkl->numpy>=1.14.0->deepface) (2024.2.0)\r\n",
      "Requirement already satisfied: tbb==2022.* in /usr/local/lib/python3.11/dist-packages (from mkl->numpy>=1.14.0->deepface) (2022.2.0)\r\n",
      "Requirement already satisfied: tcmlib==1.* in /usr/local/lib/python3.11/dist-packages (from tbb==2022.*->mkl->numpy>=1.14.0->deepface) (1.4.0)\r\n",
      "Requirement already satisfied: intel-cmplr-lib-rt in /usr/local/lib/python3.11/dist-packages (from mkl_umath->numpy>=1.14.0->deepface) (2024.2.0)\r\n",
      "Requirement already satisfied: PySocks!=1.5.7,>=1.5.6 in /usr/local/lib/python3.11/dist-packages (from requests[socks]->gdown>=3.10.1->deepface) (1.7.1)\r\n",
      "Requirement already satisfied: markdown-it-py>=2.2.0 in /usr/local/lib/python3.11/dist-packages (from rich->keras>=2.2.0->deepface) (3.0.0)\r\n",
      "Requirement already satisfied: pygments<3.0.0,>=2.13.0 in /usr/local/lib/python3.11/dist-packages (from rich->keras>=2.2.0->deepface) (2.19.2)\r\n",
      "Requirement already satisfied: intel-cmplr-lib-ur==2024.2.0 in /usr/local/lib/python3.11/dist-packages (from intel-openmp<2026,>=2024->mkl->numpy>=1.14.0->deepface) (2024.2.0)\r\n",
      "Requirement already satisfied: mdurl~=0.1 in /usr/local/lib/python3.11/dist-packages (from markdown-it-py>=2.2.0->rich->keras>=2.2.0->deepface) (0.1.2)\r\n",
      "Downloading deepface-0.0.93-py3-none-any.whl (108 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m108.6/108.6 kB\u001b[0m \u001b[31m5.8 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading flask_cors-6.0.1-py3-none-any.whl (13 kB)\r\n",
      "Downloading gunicorn-23.0.0-py3-none-any.whl (85 kB)\r\n",
      "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m85.0/85.0 kB\u001b[0m \u001b[31m4.5 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\r\n",
      "\u001b[?25hDownloading retina_face-0.0.17-py3-none-any.whl (25 kB)\r\n",
      "Building wheels for collected packages: fire\r\n",
      "  Building wheel for fire (setup.py) ... \u001b[?25l\u001b[?25hdone\r\n",
      "  Created wheel for fire: filename=fire-0.7.0-py3-none-any.whl size=114249 sha256=fddc54e773be36146d952caf04e0fc8e7993766e7edd305b7b14cc83a06b8ee4\r\n",
      "  Stored in directory: /root/.cache/pip/wheels/46/54/24/1624fd5b8674eb1188623f7e8e17cdf7c0f6c24b609dfb8a89\r\n",
      "Successfully built fire\r\n",
      "Installing collected packages: gunicorn, fire, flask-cors, retina-face, deepface\r\n",
      "Successfully installed deepface-0.0.93 fire-0.7.0 flask-cors-6.0.1 gunicorn-23.0.0 retina-face-0.0.17\r\n",
      "Note: you may need to restart the kernel to use updated packages.\n"
     ]
    }
   ],
   "source": [
    "pip install deepface"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "91ee28e7",
   "metadata": {
    "papermill": {
     "duration": 0.003752,
     "end_time": "2025-07-28T18:16:58.119237",
     "exception": false,
     "start_time": "2025-07-28T18:16:58.115485",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Step 1 Library Import"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "e2ae27c0",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:16:58.128191Z",
     "iopub.status.busy": "2025-07-28T18:16:58.127693Z",
     "iopub.status.idle": "2025-07-28T18:17:19.776835Z",
     "shell.execute_reply": "2025-07-28T18:17:19.775849Z"
    },
    "papermill": {
     "duration": 21.654993,
     "end_time": "2025-07-28T18:17:19.778059",
     "exception": false,
     "start_time": "2025-07-28T18:16:58.123066",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-07-28 18:17:03.698290: E external/local_xla/xla/stream_executor/cuda/cuda_fft.cc:477] Unable to register cuFFT factory: Attempting to register factory for plugin cuFFT when one has already been registered\n",
      "WARNING: All log messages before absl::InitializeLog() is called are written to STDERR\n",
      "E0000 00:00:1753726624.074111      19 cuda_dnn.cc:8310] Unable to register cuDNN factory: Attempting to register factory for plugin cuDNN when one has already been registered\n",
      "E0000 00:00:1753726624.175557      19 cuda_blas.cc:1418] Unable to register cuBLAS factory: Attempting to register factory for plugin cuBLAS when one has already been registered\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "25-07-28 18:17:19 - Directory /root/.deepface has been created\n",
      "25-07-28 18:17:19 - Directory /root/.deepface/weights has been created\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import os\n",
    "import numpy as np\n",
    "from deepface import DeepFace\n",
    "from datetime import datetime\n",
    "import pandas as pd\n",
    "from mtcnn import MTCNN\n",
    "import imghdr\n",
    "import time\n",
    "\n",
    "# ========== CONFIGURATIONS ==========\n",
    "FRAME_CAPTURE_INTERVAL = 5  # seconds between frame captures\n",
    "RAW_DATASET_PATH = \"/kaggle/input/raw-dataset\"  # student images folder\n",
    "OUTPUT_DIR = \"/kaggle/working/attendance_logs\"    # CSV output folder\n",
    "\n",
    "if not os.path.exists(OUTPUT_DIR):\n",
    "    os.makedirs(OUTPUT_DIR)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "79570a59",
   "metadata": {
    "papermill": {
     "duration": 0.003956,
     "end_time": "2025-07-28T18:17:19.786281",
     "exception": false,
     "start_time": "2025-07-28T18:17:19.782325",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Step 1: Helper to Get Next CSV File Name"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "31d934f5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:19.795333Z",
     "iopub.status.busy": "2025-07-28T18:17:19.794883Z",
     "iopub.status.idle": "2025-07-28T18:17:19.799818Z",
     "shell.execute_reply": "2025-07-28T18:17:19.799082Z"
    },
    "papermill": {
     "duration": 0.01074,
     "end_time": "2025-07-28T18:17:19.800999",
     "exception": false,
     "start_time": "2025-07-28T18:17:19.790259",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def get_next_csv_filename():\n",
    "    existing_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith(\"attendance_\") and f.endswith(\".csv\")]\n",
    "    indices = [int(f.split(\"_\")[1].split(\".\")[0]) for f in existing_files if f.split(\"_\")[1].split(\".\")[0].isdigit()]\n",
    "    next_index = max(indices, default=0) + 1\n",
    "    return os.path.join(OUTPUT_DIR, f\"attendance_{next_index}.csv\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a3a7dd21",
   "metadata": {
    "papermill": {
     "duration": 0.003642,
     "end_time": "2025-07-28T18:17:19.808584",
     "exception": false,
     "start_time": "2025-07-28T18:17:19.804942",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Step 2: Face Detection with MTCNN"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "1dfecd57",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:19.817720Z",
     "iopub.status.busy": "2025-07-28T18:17:19.817499Z",
     "iopub.status.idle": "2025-07-28T18:17:21.861103Z",
     "shell.execute_reply": "2025-07-28T18:17:21.860536Z"
    },
    "papermill": {
     "duration": 2.049936,
     "end_time": "2025-07-28T18:17:21.862342",
     "exception": false,
     "start_time": "2025-07-28T18:17:19.812406",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "I0000 00:00:1753726641.441868      19 gpu_device.cc:2022] Created device /job:localhost/replica:0/task:0/device:GPU:0 with 13942 MB memory:  -> device: 0, name: Tesla T4, pci bus id: 0000:00:04.0, compute capability: 7.5\n",
      "I0000 00:00:1753726641.442606      19 gpu_device.cc:2022] Created device /job:localhost/replica:0/task:0/device:GPU:1 with 13942 MB memory:  -> device: 1, name: Tesla T4, pci bus id: 0000:00:05.0, compute capability: 7.5\n"
     ]
    }
   ],
   "source": [
    "\n",
    "\n",
    "detector = MTCNN()\n",
    "\n",
    "def detect_faces(image):\n",
    "    results = detector.detect_faces(image)\n",
    "    faces = []\n",
    "    for res in results:\n",
    "        x, y, w, h = res['box']\n",
    "        x, y = abs(x), abs(y)\n",
    "        face = image[y:y+h, x:x+w]\n",
    "        faces.append(face)\n",
    "    return faces\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81a03067",
   "metadata": {
    "papermill": {
     "duration": 0.003883,
     "end_time": "2025-07-28T18:17:21.870779",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.866896",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Step 3: Verify Faces with ArcFace"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "3890c5bb",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:21.879546Z",
     "iopub.status.busy": "2025-07-28T18:17:21.879312Z",
     "iopub.status.idle": "2025-07-28T18:17:21.883998Z",
     "shell.execute_reply": "2025-07-28T18:17:21.883293Z"
    },
    "papermill": {
     "duration": 0.010324,
     "end_time": "2025-07-28T18:17:21.885025",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.874701",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "def recognize_faces(faces):\n",
    "    recognized_ids = set()\n",
    "    for face in faces:\n",
    "        for student_id in os.listdir(RAW_DATASET_PATH):\n",
    "            student_folder = os.path.join(RAW_DATASET_PATH, student_id)\n",
    "            for img_file in os.listdir(student_folder):\n",
    "                img_path = os.path.join(student_folder, img_file)\n",
    "                result = DeepFace.verify(face, img_path, model_name=\"ArcFace\", enforce_detection=False)\n",
    "                if result[\"verified\"]:\n",
    "                    recognized_ids.add(student_id)\n",
    "                    break\n",
    "            else:\n",
    "                continue\n",
    "            break\n",
    "    return recognized_ids\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "dd07485d",
   "metadata": {
    "papermill": {
     "duration": 0.003706,
     "end_time": "2025-07-28T18:17:21.892747",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.889041",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "# Step 4: Save to CSV"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "id": "dabe045f",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:21.901694Z",
     "iopub.status.busy": "2025-07-28T18:17:21.901263Z",
     "iopub.status.idle": "2025-07-28T18:17:21.906892Z",
     "shell.execute_reply": "2025-07-28T18:17:21.906176Z"
    },
    "papermill": {
     "duration": 0.011137,
     "end_time": "2025-07-28T18:17:21.907896",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.896759",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "OUTPUT_DIR = \"attendance_logs\"\n",
    "os.makedirs(OUTPUT_DIR, exist_ok=True)\n",
    "\n",
    "def get_next_csv_filename():\n",
    "    existing_files = [f for f in os.listdir(OUTPUT_DIR) if f.startswith(\"attendance_\") and f.endswith(\".csv\")]\n",
    "    indices = [int(f.split(\"_\")[1].split(\".\")[0]) for f in existing_files if f.split(\"_\")[1].split(\".\")[0].isdigit()]\n",
    "    next_index = max(indices, default=0) + 1\n",
    "    return os.path.join(OUTPUT_DIR, f\"attendance_{next_index}.csv\")\n",
    "\n",
    "def save_attendance(student_ids):\n",
    "    timestamp = datetime.now().strftime(\"%Y-%m-%d %H:%M:%S\")\n",
    "    data = [{\"Student ID\": sid, \"Time\": timestamp} for sid in student_ids]\n",
    "    df = pd.DataFrame(data)\n",
    "    csv_path = get_next_csv_filename()\n",
    "    df.to_csv(csv_path, index=False)\n",
    "    print(f\"✅ Attendance saved to: {csv_path}\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "b49b52b7",
   "metadata": {
    "papermill": {
     "duration": 0.003814,
     "end_time": "2025-07-28T18:17:21.915687",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.911873",
     "status": "completed"
    },
    "tags": []
   },
   "source": [
    "#  Step 5: Capture Frame Every N Seconds"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "id": "3f8342d5",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:21.924528Z",
     "iopub.status.busy": "2025-07-28T18:17:21.924094Z",
     "iopub.status.idle": "2025-07-28T18:17:21.929259Z",
     "shell.execute_reply": "2025-07-28T18:17:21.928591Z"
    },
    "papermill": {
     "duration": 0.010776,
     "end_time": "2025-07-28T18:17:21.930344",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.919568",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": [
    "\n",
    "\n",
    "FRAME_CAPTURE_INTERVAL = 5  # seconds\n",
    "\n",
    "def run_attendance_from_file(file_path):\n",
    "    if imghdr.what(file_path):  # Image input\n",
    "        print(\"🖼️ Detected image input\")\n",
    "        image = cv2.imread(file_path)\n",
    "        faces = detect_faces(image)\n",
    "        student_ids = recognize_faces(faces)\n",
    "        save_attendance(student_ids)\n",
    "\n",
    "    else:  # Video input\n",
    "        print(\"🎥 Detected video input\")\n",
    "        cap = cv2.VideoCapture(file_path)\n",
    "        last_capture_time = 0\n",
    "\n",
    "        while cap.isOpened():\n",
    "            ret, frame = cap.read()\n",
    "            if not ret:\n",
    "                break\n",
    "\n",
    "            current_time = time.time()\n",
    "            if current_time - last_capture_time >= FRAME_CAPTURE_INTERVAL:\n",
    "                print(\"🖼️ Capturing frame and detecting faces...\")\n",
    "                faces = detect_faces(frame)\n",
    "                student_ids = recognize_faces(faces)\n",
    "                save_attendance(student_ids)\n",
    "                last_capture_time = current_time\n",
    "        cap.release()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "id": "b8957ae7",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:17:21.939039Z",
     "iopub.status.busy": "2025-07-28T18:17:21.938849Z",
     "iopub.status.idle": "2025-07-28T18:19:25.886411Z",
     "shell.execute_reply": "2025-07-28T18:19:25.885701Z"
    },
    "papermill": {
     "duration": 123.95827,
     "end_time": "2025-07-28T18:19:25.892592",
     "exception": false,
     "start_time": "2025-07-28T18:17:21.934322",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "🖼️ Detected image input\n",
      "25-07-28 18:17:24 - arcface_weights.h5 will be downloaded to /root/.deepface/weights/arcface_weights.h5\n"
     ]
    },
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "Downloading...\n",
      "From: https://github.com/serengil/deepface_models/releases/download/v1.0/arcface_weights.h5\n",
      "To: /root/.deepface/weights/arcface_weights.h5\n",
      "100%|██████████| 137M/137M [00:00<00:00, 180MB/s]\n",
      "I0000 00:00:1753726646.102441      19 cuda_dnn.cc:529] Loaded cuDNN version 90300\n"
     ]
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "✅ Attendance saved to: attendance_logs/attendance_1.csv\n"
     ]
    }
   ],
   "source": [
    "run_attendance_from_file(\"/kaggle/input/groupphotos/GroupPhoto/WhatsApp Image 2025-07-15 at 17.26.34_47c9d744.jpg\")\n",
    "# or a video path\n",
    "# run_attendance_from_file(\"/kaggle/input/test-dataset/yourvideo.mp4\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 10,
   "id": "ff47c3a3",
   "metadata": {
    "execution": {
     "iopub.execute_input": "2025-07-28T18:19:25.903287Z",
     "iopub.status.busy": "2025-07-28T18:19:25.902718Z",
     "iopub.status.idle": "2025-07-28T18:19:26.053987Z",
     "shell.execute_reply": "2025-07-28T18:19:26.053147Z"
    },
    "papermill": {
     "duration": 0.15777,
     "end_time": "2025-07-28T18:19:26.055098",
     "exception": false,
     "start_time": "2025-07-28T18:19:25.897328",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Versions:\n",
      "OpenCV (cv2): 4.11.0\n",
      "NumPy: 1.26.4\n",
      "DeepFace: 0.0.93\n",
      "Pandas: 2.2.3\n",
      "MTCNN: 1.0.0\n",
      "Python version: 3.11.13 (main, Jun  4 2025, 08:57:29) [GCC 11.4.0]\n"
     ]
    }
   ],
   "source": [
    "import cv2\n",
    "import os\n",
    "import numpy as np\n",
    "import deepface\n",
    "from datetime import datetime\n",
    "import pandas as pd\n",
    "from mtcnn import MTCNN\n",
    "import imghdr\n",
    "import time\n",
    "\n",
    "print(\"Versions:\")\n",
    "print(f\"OpenCV (cv2): {cv2.__version__}\")\n",
    "print(f\"NumPy: {np.__version__}\")\n",
    "print(f\"DeepFace: {deepface.__version__}\")\n",
    "print(f\"Pandas: {pd.__version__}\")\n",
    "\n",
    "# mtcnn does not have a __version__ attribute, so:\n",
    "try:\n",
    "    import pkg_resources\n",
    "    mtcnn_version = pkg_resources.get_distribution(\"mtcnn\").version\n",
    "    print(f\"MTCNN: {mtcnn_version}\")\n",
    "except Exception as e:\n",
    "    print(\"MTCNN version: Could not determine\")\n",
    "\n",
    "# Standard libraries (datetime, os, imghdr, time) are part of Python and don't have separate versions\n",
    "import sys\n",
    "print(f\"Python version: {sys.version}\")\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "af289877",
   "metadata": {
    "papermill": {
     "duration": 0.004423,
     "end_time": "2025-07-28T18:19:26.064288",
     "exception": false,
     "start_time": "2025-07-28T18:19:26.059865",
     "status": "completed"
    },
    "tags": []
   },
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kaggle": {
   "accelerator": "nvidiaTeslaT4",
   "dataSources": [
    {
     "datasetId": 7869389,
     "sourceId": 12473188,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7880328,
     "sourceId": 12487980,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7880560,
     "sourceId": 12488314,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7894054,
     "sourceId": 12507221,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7894183,
     "sourceId": 12507403,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7894327,
     "sourceId": 12507610,
     "sourceType": "datasetVersion"
    },
    {
     "datasetId": 7920583,
     "sourceId": 12545303,
     "sourceType": "datasetVersion"
    }
   ],
   "dockerImageVersionId": 31089,
   "isGpuEnabled": true,
   "isInternetEnabled": true,
   "language": "python",
   "sourceType": "notebook"
  },
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.13"
  },
  "papermill": {
   "default_parameters": {},
   "duration": 169.121425,
   "end_time": "2025-07-28T18:19:29.333740",
   "environment_variables": {},
   "exception": null,
   "input_path": "__notebook__.ipynb",
   "output_path": "__notebook__.ipynb",
   "parameters": {},
   "start_time": "2025-07-28T18:16:40.212315",
   "version": "2.6.0"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
