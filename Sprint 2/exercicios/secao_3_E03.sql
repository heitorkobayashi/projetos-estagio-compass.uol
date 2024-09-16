select
    count(liv.cod) as quantidade,
    edit.nome,
    ende.estado,
    ende.cidade
from LIVRO as liv
join EDITORA as edit
  on liv.editora = edit.codEditora
join ENDERECO as ende 
    on lower(edit.endereco) = lower(ende.codEndereco)
group by edit.nome
order by quantidade desc
limit 5