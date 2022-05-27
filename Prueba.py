
from genericpath import exists


def AutoPartes(ventas: list):
    vendidos = {}
    for venta in ventas:
        vendidos[venta[5]] = venta
        
    return vendidos

def consultaRegistro(ventas, idProducto):
    vendidos = ventas
    venta =""
    noexists = True
    for vendido in vendidos:
        productos = vendidos[vendido]
        if(productos[0] == idProducto): 
            noexists = False
            venta += f"Producto consultado : {productos[0]}  Descripción  {productos[1]}  #Parte  {productos[2]}  Cantidad vendida  {productos[3]}  Stock  {productos[4]}  Comprador {productos[5]}  Documento  {productos[6]}  Fecha Venta  {productos[7]}\n"
    if(noexists):
        venta = "No hay registro de venta de ese producto"    
    print (venta)       
    
	
consultaRegistro(AutoPartes([
    (2001,'rosca', 'PT29872',2,45,'Luis Molero',3456,'12/06/2020'),
    (2010,'bujía', 'MS9512',4,15,'Carlos Rondon',1256,'12/06/2020'),
    (2010,'bujía', 'ER6523',9,36,'Pedro Montes',1243,'12/06/2020'),
    (3578,'tijera', 'QW8523',1,128,'Pedro Faria',1456,'12/06/2020'),
    (9251,'piñón', 'EN5698',2,8,'Juan Peña',565,'12/06/2020')]), 2010)