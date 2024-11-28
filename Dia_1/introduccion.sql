-- Asi se define un comentario en las bases de datos
-- DDL ( DATA DEFINITION LANGUAGE) es un sublenguaje de SQL que sirve para definir como se almacenaran los datos
CREATE DATABASE pruebas;

-- limpiara la terminal de nuestro sql
\! cls

CREATE TABLE alumnos (
    id SERIAL NOT NULL PRIMARY KEY, -- Columna que será autoincrementable, no puede ser nula y sera llave primaria
    nombre TEXT NOT NULL, -- Sera texto y no puede ser nula
    email TEXT NOT NULL UNIQUE, -- Sera texto, no puede ser nula y debe ser unica (no se repite)
    matriculado BOOLEAN DEFAULT true, -- Sera booleana y su valor por defecto si no se ingresa sera TRUE
    fecha_nacimiento DATE NULL -- Sera fecha y puede tener valores nulos ( su valor por defecto si no se define)
    );

-- Para agregar columnas a una tabla ya existente
ALTER TABLE alumnos ADD COLUMN apellido TEXT;

-- Cambiamos el tipo de dato de la columna nombre ahora sera VARCHAR(100)
-- NOTA: solamente se puede cambiar el tipo de dato si la columna no tiene registros
-- o si ya tiene registros entonces el nuevo tipo de dato debe ser compatible con el antiguo
-- no podemos cambiar un TEXT > INT o de un INT > FECHA
ALTER TABLE alumnos ALTER COLUMN nombre TYPE VARCHAR(100)

-- Elimina de manera permanente e irreversible la tabla y toda la información que hay en ella
DROP TABLE direcciones;
DROP DATABASE NOMBRE_BD;

-- DML (DATA MANIPULATION LANGUAGE)
-- Es un sublenguaje para poner interactuar