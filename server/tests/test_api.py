def test_carsale_summary(client, carsale):  # Arrange
    # Act
    response = client.get("/api/v1/carsale/summary")
    # Assert
    assert response.status_code == 200
    # check that is has a fuel key
    assert "fuel" in response.json
    assert "paint_color" in response.json
    # check for multiple fuel types
    assert len(response.json["fuel"]) == 4
    # check for multiple paint colors
    assert len(response.json["paint_color"]) == 10
