select
    atr.nome,
    atr.codAutor,
    atr.nascimento,
    count(liv.autor) as quantidade
from AUTOR as atr
left join LIVRO as liv
    on atr.codAutor = liv.autor
group by nome
order by atr.nome