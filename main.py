import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios
db=orm.SQLiteORM("db_biblioteca")

db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

autor_uno={
    
    "dni":78945612,
    "nombre":"Quevedo",
    "apellido":"Escoja de los rios"
    }

db.insertarUno("Autores",autor_uno)

usuarios_varios=[
    {
        
         "dni":95236895,
         "nombres":"Emerson",
         "apellidos":"Lopez",
         "f_nacimiento":"02/10/2003",
         "estado":"Activa"
     },
    {
         "dni":95236895,
         "nombres":"Juan",
         "apellidos":"Lopez",
         "f_nacimiento":"02/10/2003",
         "estado":"Activa"
    
    },
    {
         "dni":95236895,
         "nombres":"Juanito",
         "apellidos":"Lopez",
         "f_nacimiento":"02/10/2003",
         "estado":"Activa"
    },
    {
         "dni":952354895,
         "nombres":"Rul",
         "apellidos":"rojas",
         "f_nacimiento":"06/09/2013",
         "estado":"Activa"
    },
     {
        "dni":95236893,
        "nombres":"ELmer",
        "apellidos":"ramos",
        "f_nacimiento":"08/10/08",
        "estado":"Activa"
    }]
#db.insertarVarios("usuarios",usuarios_varios)
# muestra la lista de tuplas
#print(db.mostrar("usuarios"))
# muestra el objeto con sus campos y sus valores
#print(db.mostrar("usuarios",type="objeto"))
#tambien puedo filtrar informacion
# print(db.mostrar("Usuarios",where="nombre LIKE'cha%'",type="objeto"))
# print(db.mostrar("Usuarios",where="dni=952354895",type="objeto"))

db.actualizar("Usuarios",{"f_nacimiento":"11/08/2005"},where="dni=74123698")

db.eliminar("Usuarios",where"nombre='Juanito'")
db.eliminar("Usuarios",where"dni=952354895")

print(db.mostrar("Usuarios",type="objeto"))
