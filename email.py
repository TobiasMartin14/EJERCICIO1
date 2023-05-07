class Email:
    __idCuenta = ''
    __dominio = ''
    __tipoDominio = ''
    __contraseña = ''
    def __init__(self, idCuenta="", dominio="", tipoDominio="", contraseña=""):
        self.__idCuenta = idCuenta
        self.__dominio = dominio
        self.__tipoDominio = tipoDominio
        self.__contraseña = contraseña
    def retornaEmail(self):
        return(self.__idCuenta + '@' + self.__dominio + '.' + self.__tipoDominio)
    def getDominio(self):
        return (self.__dominio)
    def crearCuenta(self, direccionEmail, contraseña):
        parte =  direccionEmail.split("@")
        self.__idCuenta = parte[0]
        nuevaparte = parte[1].split(".")
        self.__dominio = nuevaparte[0]
        self.__tipoDominio = nuevaparte[1]
        self.__contraseña = contraseña
    def cambiarContraseña (self, contraseñaActual):
        if (contraseñaActual == self.__contraseña):
            self.__contraseña = str(input("Ingrese la nueva contraseña"))
            print("la contraseña es:" + self.__contraseña)
        else:
            print("La contraseña no coincide con la almacenada")







