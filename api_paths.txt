# Documentação da API

## Introdução
Esta documentação descreve a API que fornece acesso a informações relacionadas a usuários, refeições, feedback, dias de funcionamento e cardápios em um sistema web Django. A API é projetada para ser acessada via HTTP e retorna os dados no formato JSON.

## Base URL
A URL base para acessar a API é `https://localhost/api/`.

## Endpoints Disponíveis

### 1. Listar Usuários

#### URL
```
GET /api/usuarios/
```

#### Descrição
Este endpoint retorna uma lista de todos os usuários cadastrados no sistema.

#### Resposta
```json
{
  "Dados de Usuarios": [
    {
      "id": 1,
      "nome": "Nome do Usuário",
      "email": "usuario@email.com",
      "senha": "senha",
      "tipo": "tipo_usuario",
      "status": "ativo",
      "data modificacao": "2023-01-01T00:00:00Z"
    },
    // ... outros usuários ...
  ]
}
```

### 2. Listar Refeições

#### URL
```
GET /api/refeicoes/
```

#### Descrição
Este endpoint retorna uma lista de todas as refeições cadastradas no sistema.

#### Resposta
```json
{
  "Dados de refeicoes": [
    {
      "id": 1,
      "nome": "Nome da Refeição",
      "descricao": "Descrição da Refeição"
    },
    // ... outras refeições ...
  ]
}
```

### 3. Listar Feedbacks

#### URL
```
GET /api/feedback/
```

#### Descrição
Este endpoint retorna uma lista de todos os feedbacks cadastrados no sistema.

#### Resposta
```json
{
  "Dados de feedback": [
    {
      "id": 1,
      "nota": 5,
      "comentario": "Comentário sobre a refeição",
      "id_usuario": 1,
      "id_refeicao": 1
    },
    // ... outros feedbacks ...
  ]
}
```

### 4. Listar Dias de Funcionamento

#### URL
```
GET /api/diafuncionamento/
```

#### Descrição
Este endpoint retorna uma lista de todos os dias de funcionamento cadastrados no sistema.

#### Resposta
```json
{
  "Dados de diaFuncionamento": [
    {
      "id": 1,
      "dia_semana": "segunda-feira",
      "data_dia": "2023-01-01"
    },
    // ... outros dias de funcionamento ...
  ]
}
```

### 5. Listar Cardápios

#### URL
```
GET /api/cardapio/
```

#### Descrição
Este endpoint retorna uma lista de todos os cardápios cadastrados no sistema.

#### Resposta
```json
{
  "Dados de cardapio": [
    {
      "id": 1,
      "tipo_refeicao": "almoço",
      "hora_refeicao": "12:00:00",
      "id_refeicoes": 1,
      "id_dia_funcionamento": 1
    },
    // ... outros cardápios ...
  ]
}
```

## Considerações Finais
Certifique-se de utilizar métodos HTTP apropriados para cada operação (por exemplo, GET para leitura). Além disso, verifique as permissões adequadas para acessar esses endpoints. Esta documentação fornece uma visão geral dos endpoints disponíveis, parâmetros de requisição e formato de resposta.