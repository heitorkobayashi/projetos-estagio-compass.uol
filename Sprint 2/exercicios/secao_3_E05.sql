select distinct
    atr.nome
from AUTOR as atr 
join LIVRO as lvr 
    on atr.codAutor = lvr.autor 
join EDITORA as edt 
    on lvr.editora = edt.codEditora 
join ENDERECO as endr
    on edt.endereco = endr.codEndereco 
where (endr.estado != 'PARANÁ' and endr.estado != 'RIO GRANDE DO SUL')
order by atr.nome