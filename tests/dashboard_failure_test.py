from app import User
def test_dashboard_failure(application, client):
    with application.app_context():
        email = 'Notauser@email.com'
        password = 'testtest'
        response = client.post("/login", data=dict(email=email, password=password), follow_redirects=True)
        user = User.query.filter_by(email=email).first()
        assert user is  None