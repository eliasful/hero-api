# hero-api

Esse README contém as instruções para instalação e execução da API.
Você terá acesso a uma incrível ferramenta para armazenar e compartilhar facilmente, seus super-heróis prediletos.

## Pre-requesitos

Você precisará dos aplicativos abaixo instalados em seu computador.

* [Git](https://git-scm.com/)
* [Python 3](https://www.python.org/)
* [Virtualenv](https://virtualenv.pypa.io/)
* [Google Chrome](https://google.com/chrome/)

## Instalando

Siga os passos abaixo para utilizar a aplicação na seu computador.

* Clone este repositório
~~~~
git clone https://github.com/eliasful/hero-api.git
~~~~
* Navege até a pasta
~~~~
cd hero-api
~~~~
* Crie um ambiente isolado python e ative-o
~~~~
python3 -m venv env
. env/bin/activate
~~~~
* Instale as dependências necessárias
~~~~
pip3 install -r requirements-dev.txt
~~~~
* Crie o banco de dados
~~~~
python3 manage.py migrate
~~~~

## Executando

* Inicie o servidor
~~~~
python3 manage.py runserver
~~~~
* Acesse [http://localhost:8000](http://localhost:8000) para visualizar a API em funcionamento

## Testando

* Execute o comando abaixo para executar os testes da aplicação
~~~~
python3 manage.py test
~~~~

## Utilizando

A lista abaixo apresenta os endpoints disponíveis para utilização da API.

~~~~
GET /heroes/
~~~~

#### Resposta

Retorna um array com todos os super-heróis cadastrados

~~~~
HTTP 200 OK

[
    {
        "id": 1,
        "name": "Name",
        "description": "Description",
        "photo": "https://www.google.com/",
        "favorite": true
    }
]
~~~~
---
~~~~
GET /heroes/favorites/
~~~~

#### Resposta

Retorna um array com todos os super-heróis marcados como favorito

~~~~
HTTP 200 OK

[
    {
        "id": 1,
        "name": "Name",
        "description": "Description",
        "photo": "https://www.google.com/",
        "favorite": true
    }
]
~~~~
---
~~~~
GET /heroes/:id/
~~~~

#### Resposta, se existir

Retorna um JSON com o super-herói correspondente

~~~~
HTTP 200 OK

{
    "id": 1,
    "name": "Name",
    "description": "Description",
    "photo": "https://www.google.com/",
    "favorite": true
}
~~~~

#### Resposta, se não existir

~~~~
HTTP 404 Not Found

{
    "detail": "Not found."
}
~~~~
---
~~~~
POST /heroes/
~~~~
#### Requisição

Espera um JSON contendo os atributos abaixo

~~~~
Media type: application/json

{
  "name": "Elias",
  "description": "Not a superhero",
  "photo": null,
  "favorite": false
}
~~~~

#### Resposta

Retorna o super-herói criado

~~~~
HTTP 201 Created

{
    "id": 2,
    "name": "Elias",
    "description": "Not a superhero",
    "photo": null,
    "favorite": false
}
~~~~
---
~~~~
PUT /heroes/:id/
~~~~
#### Requisição

Espera um JSON contendo os atributos abaixo

~~~~
Media type: application/json

{
  "id": 2
  "name": "Elias",
  "description": "Realy not a superhero",
  "photo": null,
  "favorite": false
}
~~~~

#### Resposta

Retorna o super-herói atualizado

~~~~
HTTP 200 OK

{
    "id": 2,
    "name": "Elias",
    "description": "Realy not a superhero",
    "photo": null,
    "favorite": false
}
~~~~
---
~~~~
DELETE /heroes/:id/
~~~~
#### Requisição

Espera um ID como parâmetro

#### Resposta
~~~~
HTTP 204 No Content
~~~~
