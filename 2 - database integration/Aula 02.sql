drop table if exists livros;
drop table if exists autores;
drop table if exists categorias;
drop table if exists editoras;

create table autores (
  id        bigserial        primary key,
  nome      varchar(255)     default 'Anonimo',
  email     varchar(255)     unique,
  telefone  varchar(20)      default '0',
  bio       text
);

create table editoras (
  id        bigserial        primary key,
  nome      varchar(255),
  endereco  text, 
  telefone  varchar(20)
);

create table categorias (
  id        bigserial        primary key,
  nome      varchar(50)      unique
);

create table livros (
  id        bigserial        primary key,
  titulo    varchar,     
  resumo    text, 
  ano       int,
  paginas   int,
  isbn      varchar(20),

  id_autores int8,
  id_categoria int8,
  id_editora int8
);

alter table livros
  add constraint fk_id_autores
  foreign key (id_autores)
  references autores(id) on update cascade on delete cascade,

  add constraint fk_id_categoria
  foreign key (id_categoria)
  references categorias(id) on update cascade on delete cascade,

  add constraint fk_id_editora
  foreign key (id_editora)
  references editoras(id) on update cascade on delete cascade,

  add preco int;

insert into autores (email, bio)
  values
  ('victor@gmail.com', 'a vida dele'),
  ('a@gmail.com', 'teste');

update autores
  set nome = 'Victor Mendes',
  telefone = '1234'
where email = 'victor@gmail.com';

insert into livros (titulo, ano, paginas, preco)
  values ('titulo1', 2020, 200, 20),
         ('titulo2', 2023, 412, 200),
         ('titulo3', 2022, 420, 200),
         ('titulo4', 2021, 242, 300),
         ('titulo5', 2019, 142, 200);

insert into autores (nome, email, telefone)
  values ('AAAAAA', 'A@', '204440'),
         ('BBBBBBBB', 'b@', '422212'),
         ('CCCCCC', 'c@', '423330'),
         ('DDDDDD', 'd@', '22242'),
         ('EEEEEEE', 'e@', '144442');

insert into editoras (nome, endereco)
  values ('editora1','rua A'),
         ('editora2', 'rua B'),
         ('editora3', 'rua c'),
         ('editora4', 'rua D'),
         ('editora5', 'rua e');

insert into categorias (nome)
  values ('nome1'),
         ('nome2'),
         ('nome3'),
         ('nome4'),
         ('nome5');


delete from autores where id <=2;
-- returning *;
select * from livros
