create table usuario (
	id_usuario SERIAL,
	nome varchar(60),
	email varchar(60),
	senha varchar(60),
	tipo_usuario varchar(20),
	status varchar(20),
	data_modificacao date,
	primary key (id_usuario)
);

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
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
	FOREIGN KEY (id_refeicao) REFERENCES refeicoes(id_refeicoes)
);

create table cardapio (
	id_cardapio SERIAL,
	hora_refeicao varchar(255),
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
