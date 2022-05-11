from app import db, config
from app.db.models import User, Song
from flask_login import current_user, login_required

def test_bal_success(application, client):
    with application.app_context():
        email = 'testuser@email.com'
        password = 'testtest'

        response = client.post("/register", data=dict(email=email, password=password, confirm=password),
                               follow_redirects=True)

        response = client.post("/login", data=dict(email=email, password=password),
                               follow_redirects=True)

        user = User.query.filter_by(email=email).first()

        curr_bal = user.current_bal
        upload_file = 'test_transaction.csv'
        with open(upload_file, 'w') as f:

            f.write("AMOUNT,TYPE\n")
            f.write("2000,CREDIT")

        client.post("/songs/upload", data=dict(file=open(upload_file, 'rb')),follow_redirects=True)
        assert user.current_bal == curr_bal+2000

    # with application.app_context():
    #     # user = User.query.filter_by(email=login.email).first()
    #     curr_bal = current_user.current_bal
    #     upload_file = 'test_transaction.csv'
    #     with open(upload_file, 'w') as f:
    #
    #         f.write("AMOUNT,TYPE\n")
    #         f.write("2000,CREDIT")
    #
    #     client.post("/songs/upload", data=dict(file=open(upload_file, 'rb')),follow_redirects=True)
    #     assert current_user.current_bal == curr_bal+2000