# mvr_back
Back em django

Tô considerando Windows. Linux? Se vira.

Crie seu ambiente virtual

```
virtualenv nome_do_ambiente
```

Ative o ambiente

```
.\nome_do_ambiente\Scripts\activate
```

Instala o django

```python
pip install django
```

Depois puxa o código do repositório https://github.com/Projeto-Menu/mvr_back.git

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