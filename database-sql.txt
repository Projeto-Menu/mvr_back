create table usuario (
	id_usuario integer,
	nome varchar(60),
	email varchar(60),
	senha varchar(60),
	tipo_usuario varchar(20),
	status varchar(20),
	data_modificacao date,
	primary key (id_usuario)
);

create table refeicoes (
	id_refeicoes integer,
	nome_prato varchar(60),
	descricao varchar(255),
	primary key (id_refeicoes)
);

create table feedback (
	id_feedback integer,
	nota_refeicao integer,
	comentario varchar(255),
	id_usuario integer,
	id_refeicao integer,
	primary key (id_feedback),
	FOREIGN KEY (id_usuario) REFERENCES usuario(id_usuario),
	FOREIGN KEY (id_refeicao) REFERENCES refeicoes(id_refeicoes)
);


create table dia_funcionamento (
	id_dia_funcionamento integer,
	dia_semana varchar(60),
	data_dia date,
	primary key (id_dia_funcionamento)
);


create table cardapio (
	id_cardapio integer,
	tipo_refeicao varchar(60),
	hora_refeicao varchar(255),
	id_refeicoes integer,
	id_dia_funcionamento integer,
	primary key (id_cardapio),
	FOREIGN KEY (id_refeicoes) REFERENCES refeicoes(id_refeicoes),
	FOREIGN KEY (id_dia_funcionamento) REFERENCES dia_funcionamento(id_dia_funcionamento)
);
