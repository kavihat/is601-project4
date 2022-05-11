from app import db, config
from app.db.models import User, Song

def test_upload_failure(application, client):
    with application.app_context():
        email = 'notauser@email.com'
        password = 'testtest'
        client.post("/login", data=dict(email=email, password=password),
                    follow_redirects=True)
        upload_file = 'test_transaction.csv'
        with open(upload_file, 'w') as f:
            f.write("AMOUNT,TYPE\n")
            f.write("2000,CREDIT")

        client.post("/songs/upload", data=dict(file=open(upload_file, 'rb')), follow_redirects=True)
        assert db.session.query(Song).count() == 0