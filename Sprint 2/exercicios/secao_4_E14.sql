select
    vd.estado, 
    round(avg(vd.qtd * vd.vrunt), 2) as gastomedio
from tbvendas as vd
where vd.status = 'Concluído'
group by vd.estado
order by gastomedio desc
