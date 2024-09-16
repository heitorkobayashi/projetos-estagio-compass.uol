--Criação do Modelo Dimensional:
-- Tabela Tempo
create table dim_tempo (
    idTempo int primary key,
    data date,
    ano int,
    mes int,
    semana int,
    dia int,
    horario int
)

--Tabela Localizacao
create table dim_localizacao (
    idLocalizacao int primary key,
    pais varchar(50),
    estado varchar(50),
    cidade varchar(50)
)

-- Tabela Cliente
create table dim_cliente (
    idCliente int primary key,
    Cliente varchar(100)
)

-- Tabela Vendedor
create table dim_vendedor (
    idVendedor int primary key,
    vendedor varchar(100),
    genero smallint,
    estado varchar(50)
)

-- Tabela Carro
create table dim_carro (
    idCarro int primary key,
    marca varchar(50),
    modelo varchar(50),
    quilometros decimal(6, 3),
    ano int,
    classificacao varchar(50),
    combustivel int
)

-- Tabela Fato Locação
create table fato_locacao (
    idLocacao int primary key,
    idCliente int,
    idVendedor int,
    idCarro int,
    idTempo int,
    idLocalizacao int,
    quantidade int,
    valor decimal(10, 2),
    foreign key (idCliente) references dim_cliente(idCliente),
    foreign key (idVendedor) references dim_vendedor(idVendedor),
    foreign key (idCarro) references dim_carro(idCarro),
    foreign key (idTempo) references dim_tempo(idTempo),
    foreign key (idLocalizacao) references dim_localizacao(idLocalizacao)
)