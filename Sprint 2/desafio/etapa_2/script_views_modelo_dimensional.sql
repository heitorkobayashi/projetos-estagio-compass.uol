-- Criação dos views
-- Fato
create view fato_locacao as
select distinct
	idLocacao,
	idCliente,
	idVendedor,
	idCarro,
	idCombustivel,
	idTempo,
	idLocalizacao,
	qtdDiaria 		as quantidade,
	vlrDiaria 		as valor
from tb_locacao, dim_tempo, dim_localizacao

-- Cliente
create view dim_cliente as
select distinct
	idCliente,
	nomeCliente as cliente
from tb_cliente
	
-- Vendedor
create view dim_vendedor as
select distinct
	idVendedor,
	nomeVendedor 	as vendedor,
	sexoVendedor 	as genero,
	estadoVendedor  as estado
from tb_vendedor

-- Carro
create view dim_carro as
select distinct
	idCarro,
	marcaCarro	 			 as marca,
	modeloCarro				 as modelo,
	kmCarro					 as quilometros,
	strftime('%Y', anoCarro) as ano,
	classiCarro				 as classificacao,
	tipoCombustivel 		 as combustivel
from tb_carro, tb_combustivel 

-- Localização
create view dim_localizacao as
select distinct
		idLocacao 		as idLocalizacao,
		paisCliente 	as pais,
		estadoCliente 	as estado,
		cidadeCliente 	as cidade
from tb_locacao, tb_cliente

-- Tempo
create view dim_tempo as
select distinct
		idlocacao 					as idTempo,
		dataLocacao				    as data,
		strftime('%Y', dataLocacao) as ano,
		strftime('%m', dataLocacao) as mes,
		strftime('%W', dataLocacao) as semana,
		strftime('%d', dataLocacao) as dia,
		horaLocacao 				as horario
from tb_locacao