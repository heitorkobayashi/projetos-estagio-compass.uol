select 
    edt.codeditora,
    edt.nome,
    count(lvr.cod) as "QuantidadeLivros"
from editora as edt
left join livro as lvr
    on edt.codeditora = lvr.editora  
group by edt.codeditora, edt.nome 
order by QuantidadeLivros desc
limit 5
