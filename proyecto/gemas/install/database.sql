-- 
-- Script de creación de la base de datos para el ejercicio Proyecto
-- del Curso de Programación Avanzada en Python (2ª Edición) del
-- Centro de Enseñanzas Virtuales de la Universidad de Granada
--
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
  primary key (id)
);

-- Configuración predeterminada
insert into config (clave, valor) values ('VENTANA_ANCHO', '1024'),
                                         ('VENTANA_ALTO', '768');
