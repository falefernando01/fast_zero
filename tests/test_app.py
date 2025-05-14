from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_ok_e_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange
    - A: Act
    - A: Assert
    """

    client = TestClient(app)  # Arrange
    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Asset


def test_root_deve_retornar_ok_e_ola_mundo_em_html():
    client = TestClient(app)  # Arrange
    html_output = """
    <html>
      <head>
        <title>Olá mundo!</title>
      </head>
      <body>
        <h1>Olá Mundo!</h1>
      </body>
    </html>"""
    response = client.get('/ola')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.text == html_output  # Asset
