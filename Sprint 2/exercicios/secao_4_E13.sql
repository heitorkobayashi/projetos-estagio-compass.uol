select
    vd.cdpro,
    vd.nmcanalvendas,
    vd.nmpro,
    sum(vd.qtd) as quantidade_vendas
from tbvendas as vd
where vd.status = 'Concluído'
    and (vd.nmcanalvendas = 'Ecommerce' or vd.nmcanalvendas = 'Matriz')
group by vd.cdpro, vd.nmcanalvendas, vd.nmpro
order by quantidade_vendas asc
limit 10
