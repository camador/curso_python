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

--
-- CONFIGURACIÓN GENERAL
--

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

                                                      ('FRAMERATE', '60', 'Número máximo de frames por segundo'),

                                                      ('GEMA_MAX_ACTIVAS', '4', 'Número máximo de gemas activas'),
                                                      ('GEMA_RESPAWN', '1200', 'Tiempo (en milisegundos) para el respawn de las gemas'),
                                                      ('GEMA_VIDA', '3', 'Vida (en segundos) de las gemas');

--
-- RESOLUCIONES
--

-- Creación de la tabla
create table resoluciones (
  id int not null auto_increment,
  descripcion varchar(12),
  ancho varchar(4),
  alto varchar(4),
  primary key (id)
);

insert into resoluciones (descripcion, ancho, alto) values ('800 x 600', '800', '600'),
                                                           ('1024 x 768', '1024', '768');


--
-- ENEMIGOS
--

-- Creación de la tabla
create table enemigos (
  id int not null auto_increment,
  tipo int,
  fichero varchar(50),
  tamanio_x int,
  tamanio_y int,
  factor_velocidad float,
  descripcion varchar(128),
  primary key (id)
);

insert into enemigos (tipo, fichero, tamanio_x, tamanio_y, factor_velocidad, descripcion) values (0, 'enemigo.png', 49, 38, 0.5, 'Enemigo rápido'),
                                                                                                 (1, 'roca.png', 48, 49, 0.15, 'Enemigo lento que rompe las gemas');
