-- SET CLIENT_ENCODING TO 'UTF8';

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
	teléfono varchar(255),
	mail varchar(255),
	web varchar(255)
);

ALTER TABLE alkemy ADD COLUMN created_at TIMESTAMP DEFAULT NOW();

set datestyle to 'European';

-- insert into alkemy (cod_localidad, id_provincia, id_departamento, categoría, provincia, localidad, nombre, domicilio, código_postal, teléfono, mail, web)
-- 	values
-- 		();