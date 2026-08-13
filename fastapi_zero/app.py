from http import HTTPStatus

from fastapi import FastAPI
from fastapi.responses import HTMLResponse

from fastapi_zero.schemas import Message, Sobre

app = FastAPI(title='AgnesAPI')


@app.get('/', status_code=HTTPStatus.OK, response_model=Message)
def read_root():
    return {'message': 'Hello World'}


@app.get('/Ola', response_class=HTMLResponse)
def read_Ola():
    return '<h1>ola mundo</h1>'


@app.get('/sobre', response_model=Message)
def read_foda():
    return {'message': 'EU VOU SER FODA NESSA PORRA'}


@app.get('/titulo', response_class=HTMLResponse)
def read_titulo():
    return '<h1>Bem-vinda</h1><p>Essa é minha API</p>'


@app.get('/info', response_model=Sobre)
def read_esquema():
    return {'nome': 'AgnesAPI', 'versao': '1.0'}
