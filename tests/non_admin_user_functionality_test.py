from app.db.models import User

def test_request_about(client,add_user):
    """This makes the index page"""
    response = client.get("/dashboard")
    email = add_user.email
    user = User.query.filter_by(email=email).first()
    if not user.is_admin:
        assert response.status_code == 302
        assert b"Manage User" not in response.data