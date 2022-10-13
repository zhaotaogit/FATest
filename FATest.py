from fastapi import FastAPI, Form
import uvicorn
app = FastAPI()

@app.post('/login')
def login(username: str = Form(...), password: str = Form(...)):
    return {'username': username, 'password': password}


@app.get('/test')
def login():
    return '123'


if __name__ == '__main__':
    uvicorn.run("FATest:app",host='0.0.0.0',port=80)