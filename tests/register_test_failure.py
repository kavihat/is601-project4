
from app import User
def test_register_failure(application, client):
    with application.app_context():
        email = 'testuser@email.com'
        password = ''
        user = User.query.filter_by(email=email).first()
        assert user is None

        response = client.post("/register", data=dict(email=email, password=password, confirm=password), follow_redirects=True)

        user = User.query.filter_by(email=email).first()
        assert user is None