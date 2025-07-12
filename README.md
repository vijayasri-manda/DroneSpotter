# 🚀 DroneSpotter

A web-based drone detection system using **YOLOv8** for object detection, powered by a **FastAPI backend** and a simple **HTML/CSS/JS frontend**.

---

## 📂 Project Structure
  ```

DroneSpotter/
├── backend/ # FastAPI backend (YOLOv8 model runs here)
│ ├── app.py
│ ├── yolo11n.pt
├── frontend/ # Frontend HTML/CSS/JS UI
│ └── index.html
├── requirements.txt # Python dependencies
├── .gitignore
└── README.md
  ```

## 🔥 Backend Deployment (Render)

### 📌 Prerequisites:
- Render account: [https://render.com](https://render.com)
- Public GitHub repository with this project

### 📦 Steps:

1. **Ensure `requirements.txt` includes:**
    ```
    fastapi
    uvicorn
    pillow
    ultralytics
    python-multipart
    ```

2. **Commit & push your code to GitHub**
    ```bash
    git add .
    git commit -m "Prepare for Render deployment"
    git push origin main
    ```

3. **Deploy on Render**
    - Go to [Render Dashboard](https://dashboard.render.com/) → **New Web Service**
    - Connect your GitHub repository
    - Set:
      - **Build Command:** `pip install -r requirements.txt`
      - **Start Command:** `uvicorn backend.app:app --host=0.0.0.0 --port=10000`
    - Add an **Environment Variable:**
      - Key: `MODEL_PATH`
      - Value: `backend/yolo11n.pt`
    - Click **Deploy**
### ✅ API Endpoint:
POST https://<your-service-name>.onrender.com/predict/


---

## 🌐 Frontend Deployment (Firebase Hosting)

### 📌 Prerequisites:
- [Firebase CLI](https://firebase.google.com/docs/cli) installed  
  ```bash
  npm install -g firebase-tools
📦 Steps:

Login to Firebase
```
firebase login
```
Initialize Firebase in your project
```
firebase init
```
Choose Hosting
```
Select your Firebase project

Set frontend/ as the public directory

Configure as a single-page app: No
```
Deploy frontend
```
firebase deploy
```
Your frontend will be live at:

# https://<your-project-name>.web.app

