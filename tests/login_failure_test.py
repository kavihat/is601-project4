from app import User


def test_login_failure(application, client):
    with application.app_context():
        email = 'wronguser@email.com'
        password = 'wrongpass'
        response = client.post("/login", data=dict(email=email, password=password),
                               follow_redirects=True)
        user = User.query.filter_by(email=email).first()
        assert user is None

