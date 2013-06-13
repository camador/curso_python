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

                                                      ('JUGADOR_TIPO', '0', 'Tipo de jugador'),

                                                      ('GEMA_MAX_ACTIVAS', '4', 'Número máximo de gemas activas'),
                                                      ('GEMA_RESPAWN', '1200', 'Tiempo (en milisegundos) para el respawn de las gemas');

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
-- JUGADORES
--

-- Creación de la tabla
create table jugadores (
  id int not null auto_increment,
  tipo int,
  fichero varchar(50),
  tamanio_x int,
  tamanio_y int,
  factor_velocidad float,
  primary key (id)
);

insert into jugadores (tipo, fichero, tamanio_x, tamanio_y, factor_velocidad) values (0, 'jugador1.png', 77, 90, 1),
                                                                                     (1, 'jugador2.png', 67, 88, 1),
                                                                                     (2, 'jugador3.png', 68, 91, 1),
                                                                                     (3, 'jugador4.png', 76, 89, 1),
                                                                                     (4, 'jugador5.png', 76, 99, 1);

--
-- GEMAS
--

-- Creación de la tabla
create table gemas (
  id int not null auto_increment,
  tipo int,
  fichero varchar(50),
  vida float,
  tamanio_x int,
  tamanio_y int,
  indestructible int,
  descripcion varchar(128),
  primary key (id)
);

insert into gemas (tipo, fichero, vida, tamanio_x, tamanio_y, indestructible, descripcion) values (0, 'gema1.png', 2, 95, 111, 0, 'Gema básica'),
                                                                                                  (1, 'gema2.png', 4, 48, 112, 1, 'Gema un poco más duradera'),
                                                                                                  (2, 'gema3.png', 1, 48, 112, 1, 'Gema indestructible');
                                                                                                
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
