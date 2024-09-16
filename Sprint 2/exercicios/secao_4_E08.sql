with nmr_vendas as (
    select
        cdvdd,                      
        count(*) as maior_nmr_vendas
    from TBVENDAS
    where status = 'Concluído'
    order by cdvdd
) 

select
    vendedor.cdvdd,
    vendedor.nmvdd
from nmr_vendas as vendas
join TBVENDEDOR as vendedor 
    on vendas.cdvdd = vendedor.cdvdd
group by vendedor.cdvdd
order by vendedor.cdvdd desc
limit 1