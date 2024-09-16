-- CRIAÇÃO TABELAS
-- tabela combustível
create table tb_combustivel (
  idCombustivel int primary key,
  tipoCombustivel varchar(20)
)

-- tabela carro
create table tb_carro (
  idCarro int primary key,
  marcaCarro varchar(25),
  modeloCarro varchar(50),
  kmCarro int(6, 3),
  anoCarro int,
  classiCarro varchar(50),
  idCombustivel int,
  foreign key (idCombustivel) references tb_combustivel(idCombustivel)
)

-- tabela cliente
create table tb_cliente (
  idCliente int primary key,
  nomeCliente varchar(100),
  cidadeCliente varchar(50),
  estadoCliente varchar(50),
  paisCliente varchar(50)
)

-- tabela vendedor
create table tb_vendedor (
  idVendedor int primary key,
  nomeVendedor varchar(100),
  sexoVendedor smallint,
  estadoVendedor varchar (50)
)

-- BACKUP TABELA LOCAÇÃO
alter table tb_locacao rename to tb_locacao_temp

-- Criação da tabela Locação
create table tb_locacao (
    idLocacao int primary key,
    idCliente varchar(50),
    idVendedor int,
    idCarro int,
    idcombustivel int,
    horaLocacao time,
    qtdDiaria int,
    vlrDiaria decimal(10, 2),
    horaEntrega time,
    foreign key (idCliente) references tb_cliente(idCliente),
    foreign key (idCarro) references tb_carro(idCarro),
    foreign key (idVendedor) references tb_vendedor(idVendedor)
)
-- Adição das tabelas data
alter table tb_locacao
add column dataLocacao date

alter table tb_locacao
add column dataEntrega date

-- TRANSFERÊNCIA DE DADOS
-- tabela combustivel
insert into tb_combustivel(
	idCombustivel,
	tipoCombustivel
)
select distinct
	idCombustivel,
	tipoCombustivel
from tb_locacao_temp

-- tabela vendedor
insert into tb_vendedor (
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
)
select distinct
	idVendedor,
	nomeVendedor,
	sexoVendedor,
	estadoVendedor
from tb_locacao_temp

-- tabela cliente
insert into tb_cliente (
	nomeCliente,
	cidadeCliente, 
	estadoCliente,
	paisCliente	
)
select distinct
	nomeCliente,
	cidadeCliente, 
	estadoCliente,
	paisCliente	 
from tb_locacao_temp

-- tabela carro
insert into tb_carro (
	marcaCarro,
	modeloCarro,
	kmCarro,
	anoCarro,
	classiCarro,
	idCombustivel
)
select distinct
	marcaCarro, 
	modeloCarro,
	kmCarro,
	anoCarro,
	classiCarro,
	idCombustivel
from tb_locacao_temp

-- Tabela Locação
insert into tb_locacao (
    idLocacao,
    idCliente,
	idVendedor,
    idCarro,
    idcombustivel,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    horaEntrega
)
select distinct
    idLocacao,
    idCliente,
    idVendedor,
    idCarro,
    idcombustivel,
    horaLocacao,
    qtdDiaria,
    vlrDiaria,
    horaEntrega
from tb_locacao_temp 

-- adição das datas no formato YYYY-MM-DD
with numbered as (
    select rowid as id, datalocacao from tb_locacao
)
update tb_locacao
set dataLocacao = case idLocacao
	when 1 then '2015-01-10'
    when 2 then '2015-02-10'
    when 3 then '2015-02-13'
    when 4 then '2015-02-15'
    when 5 then '2015-03-02'
    when 6 then '2016-03-02'
    when 7 then '2016-08-02'
    when 8 then '2017-01-02'
    when 9 then '2018-01-02'
    when 10 then '2018-03-02'
    when 11 then '2018-04-01'
    when 12 then '2020-04-01'
    when 13 then '2022-05-01'
    when 14 then '2022-06-01'
    when 15 then '2022-07-01'
    when 16 then '2022-08-01'
    when 17 then '2022-09-01'
    when 18 then '2022-10-01'
    when 19 then '2022-11-01'
    when 20 then '2023-01-02'
    when 21 then '2023-01-15'
    when 22 then '2023-01-25'
    when 23 then '2023-01-31'
    when 24 then '2023-02-06'
    when 25 then '2023-02-12'
    when 26 then '2023-02-18'
end
from numbered
where tb_locacao.rowid = numbered.id

--

with numbered as (
    select rowid as id, dataEntrega from tb_locacao
)
update tb_locacao
set dataEntrega = case idLocacao
    when 1 then '2015-01-12'
    when 2 then '2015-02-12'
    when 3 then '2015-02-15'
    when 4 then '2015-02-20'
    when 5 then '2015-03-07'
    when 6 then '2016-03-12'
    when 7 then '2016-08-12'
    when 8 then '2017-01-12'
    when 9 then '2018-01-12'
    when 10 then '2018-03-12'
    when 11 then '2018-04-11'
    when 12 then '2020-04-11'
    when 13 then '2022-05-21'
    when 14 then '2022-06-21'
    when 15 then '2022-07-21'
    when 16 then '2022-07-21'
    when 17 then '2022-09-21'
    when 18 then '2022-10-21'
    when 19 then '2022-11-21'
    when 20 then '2023-01-12'
    when 21 then '2023-01-25'
    when 22 then '2023-01-30'
    when 23 then '2023-02-05'
    when 24 then '2023-02-11'
    when 25 then '2023-02-17'
    when 26 then '2023-02-19'
end
from numbered
where tb_locacao.rowid = numbered.id

-- Adição dos valores no formato decimal

with numbered as (
    select rowid as id, vlrDiaria from tb_locacao
)
update tb_locacao
set vlrDiaria = case idLocacao
    when 1 then '100,00'
    when 2 then '100,00'
    when 3 then '150,00'
    when 4 then '150,00'
    when 5 then '150,00'
    when 6 then '250,00'
    when 7 then '250,00'
    when 8 then '250,00'
    when 9 then '280,00'
    when 10 then '50,00'
    when 11 then '50,00'
    when 12 then '150,00'
    when 13 then '150,00'
    when 14 then '150,00'
    when 15 then '150,00'
    when 16 then '150,00'
    when 17 then '150,00'
    when 18 then '150,00'
    when 19 then '150,00'
    when 20 then '880,00'
    when 21 then '880,00'
    when 22 then '600,00'
    when 23 then '600,00'
    when 24 then '600,00'
    when 25 then '600,00'
    when 26 then '600,00'
end
from numbered
where tb_locacao.rowid = numbered.id


-- Exclusão Tabela Locação Temporária
drop table tb_locacao_temp   

-- Criação dos índices
create index idx_locacao_cliente on tb_locacao(idCliente)
create index idx_locacao_carro on tb_locacao(idCarro)
create index idx_locacao_vendedor on tb_locacao(idVendedor)
create index idx_carro_combustivel on tb_carro(idCombustivel)