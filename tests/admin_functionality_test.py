#Manage User
from flask_login import login_user, login_required, logout_user, current_user
from app.db.models import User, Location, Song

def test_request_about(client,add_user):
    """This makes the index page"""
    response = client.get("/dashboard")
    email = add_user.email
    user = User.query.filter_by(email=email).first()
    if user.is_admin:
        assert response.status_code == 200
        assert b"Manage User" in response.data