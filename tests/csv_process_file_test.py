def test_csv_processed(client):
    response = client.get('/songs/upload')
    assert response.status_code == 302