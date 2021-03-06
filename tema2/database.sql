-- 
-- Script de creación de la base de datos para el ejercicio 'CRUD'
-- del Curso de Programación Avanzada en Python (2ª Edición) del
-- Centro de Enseñanzas Virtuales de la Universidad de Granada
--
-- César Amador - camador.git@gmail.com
--

-- Borra la base de datos si existe
drop database if exists crud_camador;

-- Crea la base de datos
create database crud_camador;

-- Usuario para la conexión
grant all on crud_camador.* to 'crud_camador'@'localhost' identified by 'crud';

-- Creación de la tabla
use crud_camador;
create table crud (
  id int not null auto_increment,
  campo1 varchar(15),
  campo2 varchar(5),
  campo3 varchar(10),
  campo4 varchar(10),
  campo5 int,
  primary key (id)
);

-- Algunos datos para pruebas
insert into crud (campo1, campo2, campo3, campo4, campo5) values ('a', 'aa', 'aaa', 'aaaa', 1),
                                                         ('b', 'bb', 'bbb', 'bbbb', 2),
                                                         ('c', 'cc', 'ccc', 'cccc', 3);
