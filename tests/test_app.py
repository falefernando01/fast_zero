from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange
    - A: Act
    - A: Assert
    """

    response = client.get('/')  # Act
    assert response.status_code == HTTPStatus.OK  # Assert
    assert response.json() == {'message': 'Olá Mundo!'}  # Asset


def test_root_deve_retornar_ok_e_ola_mundo_em_html(client):
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


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'alice',
            'email': 'alice@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.CREATED
    assert response.json() == {
        'id': 1,
        'username': 'alice',
        'email': 'alice@example.com',
    }


def test_read_users(client):
    response = client.get('/users')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'id': 1,
                'username': 'alice',
                'email': 'alice@example.com',
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'fernando',
            'email': 'fernando@example.com',
            'password': 'secret',
        },
    )

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fernando',
        'email': 'fernando@example.com',
        'id': 1,
    }


def test_update_user_not_found(client):
    response = client.put(
        '/users/2',
        json={
            'username': 'joao',
            'email': 'joao@example.com',
            'password': 'new_password',
        },
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!!!'}


def test_read_user_found(client):
    response = client.get('/users/1')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fernando',
        'email': 'fernando@example.com',
        'id': 1,
    }


def test_read_user_not_found(client):
    response = client.get('/users/999')
    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!!!'}


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'fernando',
        'email': 'fernando@example.com',
        'id': 1,
    }


def test_delete_user_not_found(client):
    response = client.delete(
        '/users/2',
    )

    assert response.status_code == HTTPStatus.NOT_FOUND
    assert response.json() == {'detail': 'Usuário não encontrado!!!'}
