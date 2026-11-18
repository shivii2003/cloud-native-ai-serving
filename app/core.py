from fastapi import FastAPI
from pydantic import BaseModel
app=FastAPI()
class Request(BaseModel):
    prompt:str
@app.get('/health')
def health(): return {'status':'ok'}
@app.post('/infer')
def infer(body:Request): return {'output':body.prompt[::-1],'provider':'mock'}
