select
    vd.estado,
    vd.nmpro, 
    round(avg(vd.qtd), 4) as quantidade_media
from tbvendas as vd
where vd.status = 'Concluído'
group by vd.estado, vd.nmpro
order by vd.estado asc, vd.nmpro asc