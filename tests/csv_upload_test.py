import os
from flask_login import current_user
from flask_wtf.file import FileField

from app import User
from app.auth import register_form
from app import db, config
from app.db.models import User, Song


# def test_upload_success(application, client):
#     with application.app_context():
#         email = 'testuser@email.com'
#         password = 'testtest'
#         user = User.query.filter_by(email=email).first()
#         assert user is None
#
#         client.post("/register", data=dict(email=email, password=password, confirm=password), follow_redirects=True)
#         client.post("/login", data=dict(email=email, password=password),
#                                follow_redirects=True)
#
#         upload_file = 'test_music.csv'
#         with open(upload_file, 'w') as f:
#             f.write("Name,Artist,Composer,Album,Grouping,Work,Movement Number,Movement Count,Movement Name,Genre\n")
#             f.write("Down,Marian Hill,Jeremy Lloyd & Samantha Gongol,ACT ONE,,,,,,Electronic")
#
#         client.post("/songs/upload", data=dict(file=open(upload_file, 'rb')),follow_redirects=True)
#         assert db.session.query(Song).count() == 1


def test_upload_failure(application, client):
    with application.app_context():
        email = 'notauser@email.com'
        password = 'testtest'
        response = client.get("/songs/upload")
        assert db.session.query(Song).count() == 0

