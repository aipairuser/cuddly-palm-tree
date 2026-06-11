def test_get_activities_returns_activities(client):
    # Arrange
    expected_keys = [
        "Chess Club",
        "Programming Class",
    ]

    # Act
    resp = client.get("/activities")

    # Assert
    assert resp.status_code == 200
    data = resp.json()
    assert isinstance(data, dict)
    for key in expected_keys:
        assert key in data


def test_root_redirects_to_static_index(client):
    # Arrange: none

    # Act
    resp = client.get("/", follow_redirects=False)

    # Assert
    assert resp.status_code in (307, 302)
    assert "/static/index.html" in resp.headers.get("location", "")
