from flask_login import current_user

from app import User
from app.auth import register_form


def test_register_success(application, client):
    with application.app_context():
        email = 'testuser@email.com'
        password = 'testtest'
        user = User.query.filter_by(email=email).first()
        assert user is None

        response = client.post("/register", data=dict(email=email, password=password, confirm=password), follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        assert user is not None
        assert response.status_code == 200


