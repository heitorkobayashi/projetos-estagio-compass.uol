select
    v.nmvdd as vendedor, 
    sum(vd.qtd * vd.vrunt) as valor_total_vendas, 
    round(sum(vd.qtd * vd.vrunt) * v.perccomissao / 100, 2) as comissao
from tbvendas as vd
join tbvendedor as v
    on vd.cdvdd = v.cdvdd
where vd.status = 'Concluído'
group by v.nmvdd, v.perccomissao
order by comissao desc
