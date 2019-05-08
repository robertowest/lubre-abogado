create or alter view deuda_cliente_vendedor_v (idvendedor, idcliente, idenc_mov, total, comprobante, dias, meses)
as
select cs.idvendedor,
	   result.idcliente, result.idenc_mov, result.total,
	   rpad(cc.tipocomprob, 4, ' ') || rpad(cc.letra, 2, ' ') || lpad(cc.terminal, 4, '0') || '-' || lpad(cc.numero, 8, '0') comprobante,
     datediff(month, cc.vence, current_date) meses, datediff(day, cc.vence, current_date) dias
from 
(
  select idcliente, ref_idenc_mov as idenc_mov, sum(importe) total
  from cuentacte
  group by idcliente, ref_idenc_mov
  having sum(importe) > 0
) result
inner join cuentacte cc on cc.idenc_mov = result.idenc_mov
inner join clientessucursal cs on cs.idcliente = cc.idcliente
where datediff(day, cc.vence, current_date) > 0

