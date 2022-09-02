SET CLIENT_ENCODING TO 'UTF8';

DROP TABLE IF EXISTS alkemy;

create table alkemy (
	id SERIAL PRIMARY KEY,
	cod_localidad int not null,
	id_provincia int not null,
	id_departamento int not null,
	categoría varchar(255),
	provincia varchar(255),
	localidad varchar(255),
	nombre varchar(255),
	domicilio varchar(255),
	código_postal varchar(255),
	codigo_tel varchar(255),
	teléfono varchar(255),
	mail varchar(255),
	web varchar(255),
	fuente varchar(255)
);

ALTER TABLE alkemy ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

set datestyle to 'European';