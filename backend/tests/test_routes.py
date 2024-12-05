import json
from io import BytesIO

def test_upload_document_no_file(client, auth_headers):
    response = client.post('/api/v1/documents', headers=auth_headers)
    assert response.status_code == 400
    assert b'No file provided' in response.data

def test_upload_document_invalid_type(client, auth_headers):
    data = {'file': (BytesIO(b'test'), 'test.txt')}
    response = client.post('/api/v1/documents', headers=auth_headers, data=data)
    assert response.status_code == 400
    assert b'Only PDF files are supported' in response.data

def test_query_no_question(client, auth_headers):
    response = client.post('/api/v1/query', headers=auth_headers, json={})
    assert response.status_code == 400
    assert b'No question provided' in response.data