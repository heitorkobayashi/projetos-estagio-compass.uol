select
    atr.codAutor,
    atr.nome,
    count(lvr.cod) as quantidade_publicacoes
from AUTOR as atr 
join LIVRO as lvr 
    on atr.codAutor = lvr.autor
group by atr.nome
order by quantidade_publicacoes desc
limit 1
