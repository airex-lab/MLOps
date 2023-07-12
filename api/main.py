from fastapi import FastAPI
from datetime import datetime

app = FastAPI()

@app.post("/predict")
def predict(file: UploadFile = File(...)):
    try:
        contents = file.file.read()
        with open(file.filename), 'wb') as f:
            f.write(contents)
    except Exception as e:
        print(e)
        return { 'error': 'Error during file upload' }
    finally:
        file.file.close()

    return { 'msg': f'Successfully uploaded {file.filename}' }

@app.get('/time')
async def getTime():
    now = datetime.now()
    time = now.strftime("%Y-%m-%d %H:%M:%S")
    return { 'time': time }

@app.get('/')
async def ping():
    return { 'msg': 'MLOps Flask API is running' }
