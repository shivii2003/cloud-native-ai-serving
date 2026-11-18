from fastapi.testclient import TestClient
from app.core import app
def test_api():
    c=TestClient(app)
    assert c.get('/health').status_code==200
    assert c.post('/infer',json={'prompt':'abc'}).json()['output']=='cba'
