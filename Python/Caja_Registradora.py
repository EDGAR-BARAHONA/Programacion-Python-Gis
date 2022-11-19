
class Producto(object): 

    def __init__(self,Nombre,Codigo,Costo,Descuento): # define la clase Producto y crea las variables de instancia asociadas a este
        self.Nombre = Nombre
        self.Codigo = Codigo
        self.Costo = Costo
        self.Descuento = Descuento

    def __repr__(self): # permite que se imprima la clase poducto
         return "{} | Codigo: {} | Precio: {} | Descuento: {}".format(self.Nombre, self.Codigo, self.Costo, self.Descuento)


class Factura(object):

    def __init__(self):  #variables de instancia, se inicialzia como una factura vacia
        self.Codigo=[]
        self.Nombre=[]
        self.Unidades=[]
        self.Costo=[]
        self.Descuento=[]

    def agregar_producto(self,Codigo,Nombre,Unidades,Costo,Descuento): # agrega un prodcuto a la factura
        self.Codigo.append(Codigo)
        self.Nombre.append(Nombre)
        self.Unidades.append(Unidades)
        self.Costo.append(Costo)
        self.Descuento.append(Descuento)

    def calculo_subtotal(self): # sin aplicar el descuento
        Valor = 0
        for x in range(len(self.Codigo)):
            Valor += self.Costo[x]*self.Unidades[x]
        return Valor

    def calculo_total(self): # Aplicando Descuento aplicar el descuento
        Valor = 0
        for x in range(len(self.Codigo)):
            Valor += (self.Costo[x] - self.Costo[x]*self.Descuento[x]/100)*self.Unidades[x]
        return Valor

    def __repr__(self):      #permite que factura se imrprima
        elementos = ""
        for i in range(len(self.Codigo)):
            Valor=self.Costo[i]*self.Unidades[i] 
            elementos = elementos + " {} | {} | {} u/d. x ${} -- desc %{} = ${}\n".format(self.Codigo[i], self.Nombre[i], self.Unidades[i],self.Costo[i],self.Descuento[i],Valor) 
        return "Factura de Compra \n \n" + elementos


class Caja_Registradora(object):

    def __init__(self): # variables de instacnia, crea una factura vacia
        self.Factura = Factura()
        self.Producto = Producto("","","","")
        self.Codigos = []
        self.Productos = []
        self.Costos = []
        self.Descuentos = []

    def Agregar_producto_a_caja(self,Producto): # permite añadir productos a la base de datos de la caja
        self.Producto = Producto
        self.Codigos.append(Producto.Codigo)
        self.Costos.append(Producto.Costo)
        self.Productos.append(Producto.Nombre)
        self.Descuentos.append(Producto.Descuento)

    def Productos_Disponibles(self): # pemite imprimir los productos disponibles que se encuentran en la caja
        elementos = ''
        for x in range(len(self.Productos)):
            elementos+="  {} |  {} | $: {}\n".format(self.Codigos[x], self.Productos[x], self.Costos[x])
        print("Productos en Caja\n Codigo | Nombre | Valor\n" + elementos)
        
    def Agregar_producto_Factura(self):# añade los productos seleccionados a la factura
        Codigo_Producto = input("Ingrese el codigo del producto que desea añadir al carrito ").upper()
        while Codigo_Producto not in self.Codigos:
            print("Error, Codigo no Valido")
            Codigo_Producto = input("Ingrese el codigo del producto que desea añadir al carrito ").upper()
            
        val = False
        while val == False:
            try:
                Unidades=int(input(" Ingrese las unidades del producto: ")) 
            except TypeError:
                print("Error debe ingresar un valor numerico no una letra.")          
            else:
                if Unidades > 0:
                    val=True 
                else:
                    print("Error, El valor ingresado debe ser mayor que cero.")
        
        Cod = self.Codigos.index(Codigo_Producto)
        self.Factura.agregar_producto(Codigo_Producto,self.Productos[Cod],Unidades,self.Costos[Cod], self.Descuentos[Cod])

    def Factura_Limpia(self): #Devuelve la factura en limpio
        self.Factura.Codigo=[]
        self.Factura.Nombre=[]
        self.Factura.Unidades=[]
        self.Factura.Costo=[]
        self.Factura.Descuento=[]

    def Terminar_Transaccion(self):# termina la transaccion y hace el cobro al cliente
        ValorSubtotal = self.Factura.calculo_subtotal()
        Valortotal  = self.Factura.calculo_total()
        val = False
        while val == False:
            try:
                ValorCancelado = float(input("Con cuanto paga el usuario: "))
            except TypeError:
                print ( "Error, Ingrese un valor numerico no una letra: ")
            else:
                if ValorCancelado >= Valortotal:
                    val = True
                else:
                    print("Upsss, No es suficiente con el dinero suministrado")
        
        print(self.Factura)
        print("El valor total es de: ${}\n  El valor cancelado es; ${}\n  El cambio es: ${}".format(Valortotal,ValorCancelado,Valortotal-ValorCancelado))

#Cuerpo de Ejecucion

Caja_Registradora1 = Caja_Registradora() # define la instancia de la clase caja registradora

#productos de la tienda
Arroz=Producto("Arroz","ID01",1180, 9)
Pasta=Producto("Pasta","ID02", 1450,7)
Yuca=Producto("Yuca","ID03",1450,0)
Papa=Producto("Papa","ID04",850,2)
Arveja=Producto("Arveja","ID05",4500,3)
Aguacate=Producto("Aguacate","ID06",6000,5)
Platano=Producto("Platano","ID07",2800,10)
Carne=Producto("Carne","ID08",8000,7)
Pollo=Producto("Pollo","ID09",4500,6)
Aceite=Producto("Aceite","ID10",6200,8)
Sal=Producto("Sal","ID11",2200,10)
Azucar=Producto("Azucar","ID12",3150,8)
Leche=Producto("Leche","ID13",3200,15)

#productos disponibles en la caja registradora
Caja_Registradora1.Agregar_producto_a_caja(Arroz)
Caja_Registradora1.Agregar_producto_a_caja(Pasta)
Caja_Registradora1.Agregar_producto_a_caja(Yuca)
Caja_Registradora1.Agregar_producto_a_caja(Papa)
Caja_Registradora1.Agregar_producto_a_caja(Arveja)
Caja_Registradora1.Agregar_producto_a_caja(Aguacate)
Caja_Registradora1.Agregar_producto_a_caja(Platano)
Caja_Registradora1.Agregar_producto_a_caja(Carne)
Caja_Registradora1.Agregar_producto_a_caja(Pollo)
Caja_Registradora1.Agregar_producto_a_caja(Aceite)
Caja_Registradora1.Agregar_producto_a_caja(Sal)
Caja_Registradora1.Agregar_producto_a_caja(Azucar)
Caja_Registradora1.Agregar_producto_a_caja(Leche)

# cuerpo del codigo --- controla el funcionamiento basico
#primero le muestra los productos al cajero, despues el cajero registra los productos que necesite
# al terminar el cajero con la adicion de productos calcula el precio final de estos
#por ultimo el cajero decide y cerrar el sistema o hacer una transaccion nueva
print("""Caja Registradora Numero 1""") 

Termino =0
while Termino==0:
    Continuar = 0
    while Continuar == 0:
        Opc1 = input("Desea ver los prodcutos disponibles en caja si/no ").upper()
        while not (Opc1 == 'SI' or Opc1 == 'NO'):
            print ("Error, argumentos no validos")
            Opc1 = input("Desea ver los productos disponibles en caja si/no ").upper()

        if Opc1 == 'SI':
            Caja_Registradora1.Productos_Disponibles()
        
        Caja_Registradora1.Agregar_producto_Factura()
        print(Caja_Registradora1.Factura)
        print(" \n Subtotal : ${}".format(Caja_Registradora1.Factura.calculo_subtotal()))
        print(" \n Total : ${}".format(Caja_Registradora1.Factura.calculo_total()))

        Opc2 = input("Desea agregar mas productos si/no ").upper()
        while not (Opc2 == 'SI' or Opc2 == 'NO'):
            print ("Error, argumentos no validos")

        if Opc2 == 'NO':
            Continuar = 1
    
    Caja_Registradora1.Factura
    print(" \n Subtotal : ${}".format(Caja_Registradora1.Factura.calculo_subtotal()))
    print(" \n Total : ${}".format(Caja_Registradora1.Factura.calculo_total()))
    print("\n Descuento: ${}".format(Caja_Registradora1.Factura.calculo_subtotal()-Caja_Registradora1.Factura.calculo_total()))
    print("")
    Caja_Registradora1.Terminar_Transaccion()

    var = input("Desea realziar otra transaccion si/no ").upper()
    while not (var == 'SI' or var == 'NO'):
            print ("Error, argumentos no validos ")
            Opc1 = input("Desea realziar otra transaccion si/no ").upper()
        
    if var == 'NO':
        Termino = 1
    else:
        Caja_Registradora1.Factura_Limpia()

