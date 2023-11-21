# mvr_back
Back em django

Tô considerando Windows. Linux? Se vira.

Puxa o código do repositório https://github.com/Projeto-Menu/mvr_back.git

Crie seu ambiente virtual

```
virtualenv nome_do_ambiente
```

Ative o ambiente

```
.\nome_do_ambiente\Scripts\activate
```

Instale as dependÊncias

```python
pip install -r requirements.txt
```

Gere as variáveis de ambiente(.env)

```python
python contrib/env_gen.py
```

Crie as migrações

```python
python manage.py migrate
```

Para criar um superUser e acessar o admin

```python
python manage.py createsuperuser
```

Rode o servidor

```python
python manage.py runserver
```

Para fazer chamadas pro backend, pode usar axios, pra instalar use

```python
npm install axios
```
As rotas da API estão em api_paths


## Configuração do docker:

### Na pasta mvr_back:


```
docker compose up --build
```
### Configuração do banco de dados:

No brower:
```
localhost:15432
```
Email:
```
projetomenu@gmail.com
```
Senha:
```
postgres
```
### Configuração do servidor pgAdmin

Nome:
```
docker
```

Connection: 
Host name:
```
database
```
Username:
```
postgres
```
Password:
```
postgres
```
### Criação do banco de dados
Banco de dados:
cardapio -> Query Tools -> (Todo o documento database-sql.txt)

Qualquer coisa, é só perguntar! Linux? Se vira.