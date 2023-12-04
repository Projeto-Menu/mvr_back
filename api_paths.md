# Documentação da API

## Introdução
Esta documentação descreve a API que fornece acesso a informações relacionadas a usuários, cardápios, refeições, feedback, e dias de funcionamento em um sistema web Django utilizando o Django Rest Framework. A API é projetada para ser acessada via HTTP e retorna os dados no formato JSON.

## Base URL
A URL base para acessar a API é `https://localhost/api/`.

## Endpoints Disponíveis

### 1. Usuários

#### Listar Usuários

- **URL**
  ```
  GET /api/usuarios/
  ```

- **Descrição**
  Este endpoint retorna uma lista de todos os usuários cadastrados no sistema.

- **Resposta**
  ```json
  [
    {
      "id": 1,
      "nome": "Nome do Usuário",
      "email": "usuario@email.com",
      // ... outros campos ...
    },
    // ... outros usuários ...
  ]
  ```

#### Detalhes do Usuário

- **URL**
  ```
  GET /api/usuarios/{id}/
  ```

- **Descrição**
  Este endpoint retorna informações detalhadas sobre um usuário específico.

- **Resposta**
  ```json
  {
    "id": 1,
    "nome": "Nome do Usuário",
    "email": "usuario@email.com",
    // ... outros campos ...
  }
  ```

#### Criar Usuário

- **URL**
  ```
  POST /api/usuarios/
  ```

- **Descrição**
  Este endpoint permite a criação de um novo usuário no sistema.

- **Corpo da Requisição**
  ```json
  {
    "nome": "Novo Usuário",
    "email": "novo_usuario@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 2,
    "nome": "Novo Usuário",
    "email": "novo_usuario@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

#### Atualizar Usuário

- **URL**
  ```
  PUT /api/usuarios/{id}/
  ```

- **Descrição**
  Este endpoint permite a atualização das informações de um usuário existente.

- **Corpo da Requisição**
  ```json
  {
    "nome": "Novo Nome",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "nome": "Novo Nome",
    // ... outros campos ...
  }
  ```

#### Deletar Usuário

- **URL**
  ```
  DELETE /api/usuarios/{id}/
  ```

- **Descrição**
  Este endpoint permite a exclusão de um usuário do sistema.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### 2. Cardápios

#### Listar Cardápios

- **URL**
  ```
  GET /api/cardapios/
  ```

- **Descrição**
  Este endpoint retorna uma lista de todos os cardápios cadastrados no sistema.

- **Resposta**
  ```json
  [
    {
      "id": 1,
      "tipo_refeicao": "Almoço",
      // ... outros campos ...
    },
    // ... outros cardápios ...
  ]
  ```

#### Detalhes do Cardápio

- **URL**
  ```
  GET /api/cardapios/{id}/
  ```

- **Descrição**
  Este endpoint retorna informações detalhadas sobre um cardápio específico.

- **Resposta**
  ```json
  {
    "id": 1,
    "tipo_refeicao": "Almoço",
    // ... outros campos ...
  }
  ```

#### Criar Cardápio

- **URL**
  ```
  POST /api/cardapios/
  ```

- **Descrição**
  Este endpoint permite a criação de um novo cardápio no sistema.

- **Corpo da Requisição**
  ```json
  {
    "tipo_refeicao": "Jantar",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 2,
    "tipo_refeicao": "Jantar",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

#### Atualizar Cardápio

- **URL**
  ```
  PUT /api/cardapios/{id}/
  ```

- **Descrição**
  Este endpoint permite a atualização das informações de um cardápio existente.

- **Corpo da Requisição**
  ```json
  {
    "tipo_refeicao": "Almoço",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "tipo_refeicao": "Almoço",
    // ... outros campos ...
  }
  ```

#### Deletar Cardápio

- **URL**
  ```
  DELETE /api/cardapios/{id}/
  ```

- **Descrição**
  Este endpoint permite a exclusão de um cardápio do sistema.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### 3. Refeições

#### Listar Refeições

- **URL**
  ```
  GET /api/refeicoes/
  ```

- **Descrição**
  Este endpoint retorna uma lista de todas as refeições cadastradas no sistema.

- **Resposta**
  ```json
  [
    {
      "id": 1,
      "nome": "Nome da Refeição",
      // ... outros campos ...
    },
    // ... outras refeições ...
  ]
  ```

#### Detalhes da Refeição

- **URL**
  ```
  GET /api/refeicoes/{id}/
  ```

- **Descrição**
  Este endpoint retorna informações detalhadas sobre uma refeição específica.

- **Resposta**
  ```json
  {
    "id": 1,
    "nome": "Nome da Refeição",
    // ... outros campos ...
  }
  ```

#### Criar Refeição

- **URL**
  ```
  POST /api/refeicoes/
  ```

- **Descrição**
  Este endpoint permite a criação de uma nova refeição no sistema.

- **Corpo da Requisição**
  ```json
  {
    "nome": "Nova Refeição",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "

id": 2,
    "nome": "Nova Refeição",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

#### Atualizar Refeição

- **URL**
  ```
  PUT /api/refeicoes/{id}/
  ```

- **Descrição**
  Este endpoint permite a atualização das informações de uma refeição existente.

- **Corpo da Requisição**
  ```json
  {
    "nome": "Novo Nome",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "nome": "Novo Nome",
    // ... outros campos ...
  }
  ```

#### Deletar Refeição

- **URL**
  ```
  DELETE /api/refeicoes/{id}/
  ```

- **Descrição**
  Este endpoint permite a exclusão de uma refeição do sistema.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### 4. Feedbacks

#### Listar Feedbacks

- **URL**
  ```
  GET /api/feedbacks/
  ```

- **Descrição**
  Este endpoint retorna uma lista de todos os feedbacks cadastrados no sistema.

- **Resposta**
  ```json
  [
    {
      "id": 1,
      "nota": 5,
      // ... outros campos ...
    },
    // ... outros feedbacks ...
  ]
  ```

#### Detalhes do Feedback

- **URL**
  ```
  GET /api/feedbacks/{id}/
  ```

- **Descrição**
  Este endpoint retorna informações detalhadas sobre um feedback específico.

- **Resposta**
  ```json
  {
    "id": 1,
    "nota": 5,
    // ... outros campos ...
  }
  ```

#### Criar Feedback

- **URL**
  ```
  POST /api/feedbacks/
  ```

- **Descrição**
  Este endpoint permite a criação de um novo feedback no sistema.

- **Corpo da Requisição**
  ```json
  {
    "nota": 4,
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 2,
    "nota": 4,
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

#### Atualizar Feedback

- **URL**
  ```
  PUT /api/feedbacks/{id}/
  ```

- **Descrição**
  Este endpoint permite a atualização das informações de um feedback existente.

- **Corpo da Requisição**
  ```json
  {
    "nota": 3,
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "nota": 3,
    // ... outros campos ...
  }
  ```

#### Deletar Feedback

- **URL**
  ```
  DELETE /api/feedbacks/{id}/
  ```

- **Descrição**
  Este endpoint permite a exclusão de um feedback do sistema.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### 5. Dias de Funcionamento

#### Listar Dias de Funcionamento

- **URL**
  ```
  GET /api/diasfuncionamento/
  ```

- **Descrição**
  Este endpoint retorna uma lista de todos os dias de funcionamento cadastrados no sistema.

- **Resposta**
  ```json
  [
    {
      "id": 1,
      "dia_semana": "Segunda-feira",
      // ... outros campos ...
    },
    // ... outros dias de funcionamento ...
  ]
  ```

#### Detalhes do Dia de Funcionamento

- **URL**
  ```
  GET /api/diasfuncionamento/{id}/
  ```

- **Descrição**
  Este endpoint retorna informações detalhadas sobre um dia de funcionamento específico.

- **Resposta**
  ```json
  {
    "id": 1,
    "dia_semana": "Segunda-feira",
    // ... outros campos ...
  }
  ```

#### Criar Dia de Funcionamento

- **URL**
  ```
  POST /api/diasfuncionamento/
  ```

- **Descrição**
  Este endpoint permite a criação de um novo dia de funcionamento no sistema.

- **Corpo da Requisição**
  ```json
  {
    "dia_semana": "Terça-feira",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 2,
    "dia_semana": "Terça-feira",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

#### Atualizar Dia de Funcionamento

- **URL**
  ```
  PUT /api/diasfuncionamento/{id}/
  ```

- **Descrição**
  Este endpoint permite a atualização das informações de um dia de funcionamento existente.

- **Corpo da Requisição**
  ```json
  {
    "dia_semana": "Quarta-feira",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "dia_semana": "Quarta-feira",
    // ... outros campos ...
  }
  ```

#### Deletar Dia de Funcionamento

- **URL**
  ```
  DELETE /api/diasfuncionamento/{id}/
  ```

- **Descrição**
  Este endpoint permite a exclusão de um dia de funcionamento do sistema.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### Registro de Usuário

- **URL**
  ```
  POST /api/register/
  ```

- **Descrição**
  Este endpoint permite o registro de um novo usuário no sistema.

- **Corpo da Requisição**
  ```json
  {
    "username": "NovoUsuario",
    "password": "SenhaSegura123",
    "email": "novousuario@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 2,
    "nome": "NovoUsuario",
    "email": "novousuario@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

### Login de Usuário

- **URL**
  ```
  POST /api/login/
  ```

- **Descrição**
  Este endpoint permite o login de um usuário existente.

- **Corpo da Requisição**
  ```json
  {
    "username": "UsuarioExistente",
    "password": "SenhaSegura123",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  ```json
  {
    "id": 1,
    "nome": "UsuarioExistente",
    "email": "usuarioexistente@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

### Logout de Usuário

- **URL**
  ```
  POST /api/logout/
  ```

- **Descrição**
  Este endpoint realiza o logout do usuário atual.

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

### Redefinição de Senha

- **URL**
  ```
  POST /api/password-reset/
  ```

- **Descrição**
  Este endpoint permite a redefinição de senha para um usuário.

- **Corpo da Requisição**
  ```json
  {
    "email": "usuario@email.com",
    // ... outros campos ...
  }
  ```

- **Resposta (Sucesso)**
  Sem conteúdo (204 No Content)

- **Resposta (Erro)**
  ```json
  {
    "erro": "Mensagem de erro detalhada"
  }
  ```

## Considerações Finais
Certifique-se de utilizar métodos HTTP apropriados para cada operação (por exemplo, GET para leitura). Além disso, verifique as permissões adequadas para acessar esses endpoints. Esta documentação fornece uma visão geral dos endpoints disponíveis, parâmetros de requisição e formato de resposta.