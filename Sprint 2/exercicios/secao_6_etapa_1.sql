select 
    lvr.cod,
    lvr.titulo,
    atr.codautor,
    atr.nome,
    lvr.valor,
    edt.codeditora,
    edt.nome
from autor as atr
left join livro as lvr
    on atr.codautor = lvr.cod
left join editora as edt 
    on lvr.editora = edt.codeditora
group by lvr.valor
order by lvr.valor desc
limit 10