import orm
from Tablas.Autores import Autores
from Tablas.Libros import Libros
from Tablas.Usuarios import Usuarios

db=orm.SQLiteORM("db_biblioteca")
db.crear_tabla(Autores)
db.crear_tabla(Libros)
db.crear_tabla(Usuarios)

# autor_uno={
#     "dni":78945612,
#     "nombre":"quevedo",
#     "apellidos":"es coja de los rios"
#     }
# db.insertarUno("Autores",autor_uno)
usuarios_varios=[
    {
        "dni":745896,
        "nombre":"nadine",
        "apellidos":"atoccsa",
        "f_nacimiento":"06/04/2005",
        "estado":"activo"
    },
    {
        "dni":78569784,
        "nombre":"feli",
        "apellidos":"ccaccachahua",
        "f_nacimiento":"07/11/1997",
        "estado":"activo"
    },
    {
        "dni":71234567,
        "nombre":"bichota",
        "apellidos":"de taype",
        "f_nacimiento":"28/11/2023",
        "estado":"inactivo"
    },
    {
        "dni":755896,
        "nombre":"chamo menor",
        "apellidos":"no jodas",
        "f_nacimiento":"30/11/2023",
        "estado":"activo"
    },
    {
        "dni":775896,
        "nombre":"yadira",
        "apellidos":"quiero mami",
        "f_nacimiento":"500 a.c",
        "estado":"momia"
    }
]
# db.insertarVarios("Usuarios",usuarios_varios)

# muestra una lista de tuplas
# print(db.mostrar("Usuarios"))
# # # muestra un objeto con sus campos y sus valores
# print(db.mostrar("Usuarios",type="objeto"))
# tambien puedo filtrar informacion
# print(db.mostrar("Usuarios",where="estado='momia'",type="objeto"))
# print(db.mostrar("Usuarios",where="nombre LIKE 'cha%'",type="objeto"))
# print(db.mostrar("Usuarios",where="dni =71234567",type="objeto"))

# db.actualizar("Usuarios",{"estado":"activo"},where="nombre='yadira'")
# db.actualizar("Usuarios",{"f_nacimiento":"11/08/2005"},where="dni=775896")
# dato_actualizar={"nombre":"chamos","apellidos":"ya es salida"}
# db.actualizar("Usuarios",dato_actualizar,where="dni=755896")
db.eliminar("Usuarios",where="nombre='bichota'")
db.eliminar("Usuarios",where="dni=755896")
print(db.mostrar("Usuarios",type="objeto"))