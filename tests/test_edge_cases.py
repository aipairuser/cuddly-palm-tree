def test_signup_nonexistent_activity_returns_404(client):
    # Arrange
    activity = "Nonexistent Activity"
    email = "a@b.com"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Activity not found"


def test_unregister_nonexistent_participant_returns_404(client):
    # Arrange
    activity = "Chess Club"
    email = "noone@nowhere.com"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 404
    assert resp.json()["detail"] == "Participant not found"
