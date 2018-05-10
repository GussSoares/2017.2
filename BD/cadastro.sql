create database cadastro
default character set utf8
default collate utf8_general_ci;

use cadastro;
CREATE TABLE pessoas (
	id int not null auto_increment,
    nome varchar(30) not null,
    nascimento date,
    sexo enum('M', 'F'),
    peso decimal(5,2),
    altura decimal(3,2),
    nacionalidade varchar(20) default 'Brasil',
	primary key(id)
)default charset = utf8;

use cadastro;

insert into pessoas
(id, nome, nascimento, sexo, peso, altura, nacionalidade)
values
(default, 'Gustavo', '1998-10-08', 'M', '65.5', '1.80', 'Brasil');

select * from pessoas;