from http import HTTPStatus

from fastapi.testclient import TestClient

from fastapi_zero.app import app


def test_root_deve_retornar_ola_mundo():
    """
    Esse teste tem 3 etapas (AAA)
    - A: Arrange - arranjo
    - A: Act     - executa a coisa (o SUT)
    - A: Assert  - garante que A é A
    """
    # arrange
    client = TestClient(app)
    # Act
    response = client.get('/')
    # Assert
    assert response.json() == {'message': 'Hello World'}
    assert response.status_code == HTTPStatus.OK


def test_ola_deve_retornar_ola_mundo_em_html():
    client = TestClient(app)

    response = client.get('/Ola')

    assert response.text == '<h1>ola mundo</h1>'
    assert response.status_code == HTTPStatus.OK


def test_treino_de_fastapi_dunossauro():
    client = TestClient(app)

    response = client.get('/sobre')

    assert response.json() == {'message': 'EU VOU SER FODA NESSA PORRA'}
    assert response.status_code == HTTPStatus.OK


def test_titulo_deve_retornar_titulo_html():
    client = TestClient(app)

    response = client.get('/titulo')

    assert response.text == '<h1>Bem-vinda</h1><p>Essa é minha API</p>'
    assert response.status_code == HTTPStatus.OK


def test_deve_checar_dois_campos():
    client = TestClient(app)

    response = client.get('/info')

    assert response.json() == {'nome': 'AgnesAPI', 'versao': '1.0'}
    assert response.status_code == HTTPStatus.OK
