from fastapi import FastAPI, File, UploadFile
from transformers import pipeline
from PIL import Image
import io

# AI Model load ho raha hai (Google's Vit Model)
classifier = pipeline("image-classification", model="google/vit-base-patch16-224")

app = FastAPI()

@app.get("/")
def home():
    return {"status": "Online", "Project": "DevOps AI Classifier", "Author": "Aapka Naam"}

@app.post("/predict")
async def predict(file: UploadFile = File(...)):
    # Image read karna
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    
    # AI Prediction
    predictions = classifier(image)
    
    return {"predictions": predictions}