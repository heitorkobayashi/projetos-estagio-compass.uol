select
    atr.nome
from AUTOR as atr 
left join LIVRO as lvr 
    on atr.codAutor = lvr.autor
where lvr.autor is null