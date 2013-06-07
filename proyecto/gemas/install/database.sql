-- 
-- Script de creación de la base de datos para el Proyecto
-- del Curso de Programación Avanzada en Python (2ª Edición) del
-- Centro de Enseñanzas Virtuales de la Universidad de Granada
--
-- git://github.com/camador/curso_python.git
-- César Amador - camador.git@gmail.com
--

-- Borra la base de datos si existe
drop database if exists gemas_camador;

-- Crea la base de datos
create database gemas_camador;

-- Usuario para la conexión
grant all on gemas_camador.* to 'gemas'@'localhost' identified by 'gemas';

-- Creación de la tabla
use gemas_camador;
create table config (
  id int not null auto_increment,
  clave varchar(64),
  valor varchar(128),
  descripcion varchar(255),
  primary key (id)
);

-- Configuración predeterminada
insert into config (clave, valor, descripcion) values ('VENTANA_ANCHO', '1024', 'Ancho de la ventana en pixels '),
                                                      ('VENTANA_ALTO', '768', 'Alto de la ventana en pixels'),
                                                      ('DIR_IMG', 'imagenes', 'Directorio de las imágenes'),
                                                      ('VELOCIDAD_BASE', '1', 'Velocidad base para todos los sprites'),
                                                      ('FRAMERATE', '60', 'Número máximo de frames por segundo');
