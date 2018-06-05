class Pedido:
  def __init__(this):
    objProductos = Productos()
    objClientes = Clientes()
    this.direccionEnvio=direccionEnvio
    this.precio=precio
    this.fecha=fecha

  def getObjproductos():
    return this.objProductos

  def getObjclientes():
    return this.objClientes

  def getDireccionenvio():
    return this.direccionEnvio

  def getPrecio():
    return this.precio

  def getFecha():
    return this.fecha

  def setObjproductos(this,objProductos):
    this.objProductos = objProductos

  def setObjclientes(this,objClientes):
    this.objClientes = objClientes

  def setDireccionenvio(this,direccionEnvio):
    this.direccionEnvio = direccionEnvio

  def setPrecio(this,precio):
    this.precio = precio

  def setFecha(this,fecha):
    this.fecha = fecha

