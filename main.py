from fastapi import FastAPI

app = FastAPI()

@app.get('/time')
async def getTime():
    return { 'time': '2021-09-01 12:00:00' }

@app.get('/')
async def ping():
    return { 'msg': 'MLOps Flask API is running' }

# if __name__ == '__main__':
#     app.run(debug=True, host='0.0.0.0', port=5000)
