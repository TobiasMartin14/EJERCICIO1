import email
import csv


def test():
    idCuenta = str(input("Ingrese el id de la cuenta: "))
    dominio = str(input("Ingrese el dominio: "))
    tipoDominio = str(input("Ingrese el tipo de dominio: "))
    contraseña = str(input("Ingrese la contraseña: "))
    email1 = email.Email (idCuenta, dominio, tipoDominio, contraseña)
    print(email1.retornaEmail())

    nombre = str(input("Ingrese el nombre: "))
    direccionCorreo = str(input("Ingrese su direccion de correo "))
    contraseñae2 = str(input("Ingrese la contraseña de su mail: "))
    email2 = email.Email ()
    email2.crearCuenta(direccionCorreo, contraseñae2)
    print ("Estimado " + nombre + " te enviaremos tus mensajes a la direccion " + email2.retornaEmail())

    contraseñaActual = str(input("Ingrese la contraseña actual"))
    email2.cambiarContraseña (contraseñaActual)

    email3 = email.Email ()
    direccionCorreo2 = str(input("Ingrese su direccion de correo "))
    contraseñae3 = str(input("Ingrese la contraseña de su mail: "))
    email3.crearCuenta(direccionCorreo2, contraseñae3)
    print ("La cuenta creada es: " + email3.retornaEmail())

def archivoEmails():
       emailvalido = []
       archivo = open('LISTA10.csv')
       reader = csv.reader(archivo)
       for fila in reader:
           if "@" in fila[0] and "." in fila[0]:
               print ("Direccion de email correcta{}", format(fila[0]))
               emails = email.Email ()
               contra = str(input("Para almacenar su correo: Ingrese su contraseña:  "))
               emails.crearCuenta(fila[0], contra)
               emailvalido.append(emails)
           else:
               print("Direccion de email incorrecta: {}", format(fila[0]))
       
       archivo.close()
       
       dominik = str(input("Ingrese un dominio a buscar: "))
       emaildom = 0
       for emails in emailvalido:
           if emails.getDominio() == dominik:
               emaildom = emaildom + 1
       print("Hay {} direcciones de email con el dominio {}" .format(emaildom, dominik))

if __name__ == '__main__':
    test ()
    archivoEmails()