Creación de una tabla sencilla en MariaDB:

CREATE TABLE prueba1(

id	INT(20)	AUTO_INCREMENT	PRIMARY KEY,

nombre VARCHAR(20) NOT NULL,

apellido VARCHAR(20) NOT NULL,

telefono	INT(15) NULL,

direccion VARCHAR(100) NOT NULL 

);
