
create table refeicoes (
	id_refeicoes SERIAL,
	nome_prato varchar(60),
	descricao varchar(255),
	primary key (id_refeicoes)
);

create table feedback (
	id_feedback SERIAL,
	nota_refeicao integer,
	comentario varchar(255),
	id_usuario integer,
	id_refeicao integer,
	primary key (id_feedback),
	FOREIGN KEY (id_usuario) REFERENCES cardapio_usuario(id),
	FOREIGN KEY (id_refeicao) REFERENCES refeicoes(id_refeicoes)
);

create table cardapio (
	id_cardapio SERIAL,
	id_prato_principal integer,
	id_vegetariano integer,
	id_guarnicao integer,
	id_complemento integer,
	id_salada_crua integer,
	id_salada_cozida integer,
	id_sobremesa integer,
	id_bebida integer,
	primary key (id_cardapio),
	FOREIGN KEY (id_prato_principal) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_vegetariano) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_guarnicao) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_complemento) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_salada_crua) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_salada_cozida) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_sobremesa) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_bebida) REFERENCES refeicoes(id_refeicoes)
);


create table dia_funcionamento (
	id_dia_funcionamento SERIAL,
	id_almoco integer,
	id_janta integer,
	dia_semana varchar(60),
	data_dia date,
	primary key (id_dia_funcionamento),
	FOREIGN KEY (id_almoco) REFERENCES cardapio(id_cardapio),
	FOREIGN KEY (id_janta) REFERENCES cardapio(id_cardapio)
);

INSERT INTO cardapio_usuario (
    id, password, last_login, is_superuser, username, first_name, last_name, is_staff, is_active, date_joined, email
)
VALUES 
(
    1, 'senha123', '2023-12-06T12:00:00Z', false, 'joedoe', 'Joe', 'Doe', false, true, '2023-12-06T12:00:00Z', 'joe.doe@example.com'
),
(
    2, 'outrasenha456', '2023-12-06T12:30:00Z', false, 'janedoe', 'Jane', 'Doe', false, true, '2023-12-06T12:30:00Z', 'jane.doe@example.com'
);

INSERT INTO public.refeicoes (nome_prato, descricao) VALUES 
('Prato Principal 1', 'Descrição do Prato Principal 1'),
('Prato Principal 2', 'Descrição do Prato Principal 2'),
('Vegetariano 1', 'Descrição do Vegetariano 1'),
('Guarnição 1', 'Descrição da Guarnição 1'),
('Complemento 1', 'Descrição do Complemento 1'),
('Salada Crua 1', 'Descrição da Salada Crua 1'),
('Salada Cozida 1', 'Descrição da Salada Cozida 1'),
('Sobremesa 1', 'Descrição da Sobremesa 1'),
('Bebida 1', 'Descrição da Bebida 1');

INSERT INTO public.feedback (nota_refeicao, comentario, id_usuario, id_refeicao) VALUES 
(4, 'Ótima refeição!', 1, 1),
(3, 'Poderia melhorar.', 2, 2),
(5, 'Excelente como sempre.', 1, 3);

INSERT INTO public.cardapio (
    id_prato_principal, id_vegetariano, id_guarnicao, id_complemento, 
    id_salada_crua, id_salada_cozida, id_sobremesa, id_bebida
) VALUES 
(1, 3, 4, 5, 6, 7, 8, 9),
(2, 3, 4, 5, 6, 7, 8, 9),
(1, 3, 4, 5, 6, 7, 8, 9);

INSERT INTO public.dia_funcionamento (id_almoco, id_janta, dia_semana, data_dia) VALUES 
(1, 2, 'Segunda-feira', '2023-12-11'),
(3, 1, 'Terça-feira', '2023-12-12'),
(1, 2, 'Quarta-feira', '2023-12-13'),
(2, 3, 'Quinta-feira', '2023-12-13'),
(3, 2, 'Sexta-feira', '2023-12-13');

