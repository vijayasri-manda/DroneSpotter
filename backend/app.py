from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from ultralytics import YOLO
from PIL import Image
import io
import uvicorn
import base64

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

model = YOLO("yolo11n.pt")

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))

    results = model.predict(image, save=True, conf=0.5)
    detections = []
    for result in results:
        for box in result.boxes:
            detections.append({
                "confidence": round(float(box.conf.item()) * 100, 2)
            })

    # Save predicted image to base64
    result_img = results[0].plot()  # image with bounding boxes
    img_pil = Image.fromarray(result_img)
    buffered = io.BytesIO()
    img_pil.save(buffered, format="JPEG")
    img_base64 = base64.b64encode(buffered.getvalue()).decode()

    return {
        "filename": file.filename,
        "detections": detections,
        "predicted_image": img_base64
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
