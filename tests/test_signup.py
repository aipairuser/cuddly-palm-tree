def test_signup_successful_and_persists(client):
    # Arrange
    activity = "Chess Club"
    email = "testuser@example.com"

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json() == {"message": f"Signed up {email} for {activity}"}

    # Verify participant was added
    resp2 = client.get("/activities")
    assert email in resp2.json()[activity]["participants"]


def test_signup_duplicate_returns_400(client):
    # Arrange
    activity = "Chess Club"
    existing = "michael@mergington.edu"  # already present in fixture data

    # Act
    resp = client.post(f"/activities/{activity}/signup", params={"email": existing})

    # Assert
    assert resp.status_code == 400
    assert resp.json()["detail"] == "Student already signed up"


def test_unregister_removes_participant(client):
    # Arrange
    activity = "Chess Club"
    email = "michael@mergington.edu"

    # Act
    resp = client.delete(f"/activities/{activity}/participants", params={"email": email})

    # Assert
    assert resp.status_code == 200
    assert resp.json() == {"message": f"Unregistered {email} from {activity}"}

    # Verify removal
    resp2 = client.get("/activities")
    assert email not in resp2.json()[activity]["participants"]
