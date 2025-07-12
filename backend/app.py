from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import uvicorn
import base64
import os


# Initialize FastAPI app
app = FastAPI()

# Allow CORS for all origins (so frontend can access backend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load your YOLO model
model_path = os.getenv("MODEL_PATH", "yolo11n.pt")
model = YOLO(model_path)

# Define prediction endpoint
@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    # Read image file
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    # Run prediction
    results = model.predict(image, save=True, conf=0.5)
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "confidence": round(float(box.conf.item()) * 100, 2)
            })

    # Convert prediction result image to base64
    result_img = results[0].plot()  # image with bounding boxes
    img_pil = Image.fromarray(result_img)
    buffered = io.BytesIO()
    img_pil.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    # Return prediction data
    return {
        "filename": file.filename,
        "detections": detections,
        "predicted_image": img_base64
    }

# Run app locally
if __name__ == "__main__":
    port = int(os.environ.get("PORT", 10000))
    uvicorn.run(app, host="0.0.0.0", port=port)
