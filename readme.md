# BandKamp

Projeto backend de uma plataforma de musica.

O desafio é:

*"Seu objetivo nesse projeto é adequar um sistema 'legado' que inicialmente já está desenvolvido com APIView e sqlite3, fazendo a transição para Generic Views, Model Serializer e Postgres, além de documentar e de verificar e manter a integridade das funcionalidades já existentes."*

## Stack utilizada

Para o estudo foram escolhidas as tecnologias:

**Back-end:** Python, Django, PostgreSQL.

**Testes:** Pytest.

**Ambiente:** Venv.
## Rodando localmente

Clone o projeto

```bash
  git clone git@github.com:agnes-lica/Bandkamp-Python.git
```

Entre no diretório do projeto

```bash
  cd Bandkamp
```

Inicie o servidor

```bash
# linux:
  source venv/bin/activate

# windows:
  .\venv\Scripts\activate 
```

Instale as dependências

```bash
  pip install -r requirements. txt
```

## Rodando os testes

#### Rodar todos os testes
```bash
 pytest --testdox -vvs
```

#### Rodar testes por users
```bash
 pytest --testdox -vvs tests/users/
```

#### Rodar testes por albuns
```bash 
 pytest --testdox -vvs tests/albums/
```

#### Rodar testes por songs
```bash 
 pytest --testdox -vvs tests/songs/
```

## Documentação da API

#### Endpoints

| Método   | Endpoint       | Descrição                                   |
| :---------- | :--------- | :------------------------------------------ |
| `POST`      | `/api/users/` | Criação de usuário|
| `PATCH`      | `api/users/<int:pk>/` | Edita o usuário |
| `POST`      | `/api/users/login/` | Autenticação do usuário |
| `POST`      | `api/albums` | Cria um album de musica |
| `POST`      | `api/albums/<int:pk>/songs/` | Cria uma musica e relaciona com um album |

## Contato

Para entrar em contato comigo me mande um e-mail ou uma mensagem nas redes sociais:

- [github](https://www.github.com/agnes-lica)
- [LinkedIn](https://www.linkedin.com/in/agnesmr/)
- E-mail: agnes.lica@gmail.com
