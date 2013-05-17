Víctimas de Conan
-----------------

Escribe un programa que, basándose en los datos del ejemplo anterior, rellene automáticamente una base de datos de víctimas de Conan con 10 ejemplos y, además, permita introducir un nuevo registro y mostrar los que ya hay.

Para no dar ventaja a ningún alumno, no deben usare más características de SQL que las aquí vistas.

Al iniciar el programa, este creará 10 registros automáticamente

Después, irá pidiendo datos al usuario: Nombre, Profesion y Muerte (salvo id, que deberá ser generado automáticamente)

El valor del campo id no debe repetirse (y esto debe controlarlo Python, no por medio de las características de MySQL)

No es necesario que se pueda introducir más de un registro en cada ejecución del programa, pero se valorará que lo haga.

Si se introduce un valor en blanco para cualquier campo, no se efectuará el insert y se enviará al usuario un aviso advirtiendo que no se ha hecho

Se introduzca o nó un nuevo valor, al final se mostrará una tabla con los datos actualmente almacenados

Por último, el programa NO debe borrar la tabla ni ningún dato. 
