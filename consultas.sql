CREATE OR ALTER VIEW DEUDA_CLIENTE_VENDEDOR_V (IDVENDEDOR, IDCLIENTE, IDENC_MOV, TOTAL, COMPROBANTE, FECHA, VENCE, DIAS)
AS
select cs.idvendedor,
	   result.idcliente, result.idenc_mov, result.total,
	   rpad(cc.tipocomprob, 4, ' ') || rpad(cc.letra, 2, ' ') || lpad(cc.terminal, 4, '0') || '-' || lpad(cc.numero, 8, '0') comprobante,
	   cc.fecha, cc.fecha + pv.diascob1 vence,
       datediff(day, cc.fecha + pv.diascob1, current_date) dias
from
(
  select idcliente, ref_idenc_mov as idenc_mov, sum(importe) total
  from cuentacte
  group by idcliente, ref_idenc_mov
  having sum(importe) > 0
) result
inner join cuentacte cc on cc.idenc_mov = result.idenc_mov
inner join clientessucursal cs on cs.idcliente = cc.idcliente
inner join ptovta pv on pv.ptovta = cc.terminal
where datediff(day, cc.vence, current_date) > 0
