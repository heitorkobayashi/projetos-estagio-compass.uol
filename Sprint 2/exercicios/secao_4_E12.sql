select
    dep.cddep,
    dep.nmdep,
    dep.dtnasc,
    v.valor_total_vendas
from tbdependente as dep
join tbvendas as vd
    on vd.cdvdd = dep.cdvdd
join (
    select vd.cdvdd, sum(vd.qtd * vd.vrunt) as valor_total_vendas
    from tbvendas as vd
    where vd.status = 'Concluído'
    group by vd.cdvdd
    having valor_total_vendas > 0
    order by valor_total_vendas asc
) as v on v.cdvdd = dep.cdvdd
limit 1
