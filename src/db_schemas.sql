CREATE DATABASE IF NOT EXISTS ines_db;
USE ines_db;

CREATE TABLE if NOT EXISTS usuarios (
  ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  correo VARCHAR(50) NOT NULL,
  contrasenna VARCHAR (50) NOT NULL,
  nombre VARCHAR (50) NOT NULL,
  nombre2 VARCHAR (50) NULL,
  nombre3 VARCHAR (50) NULL,
  apellido VARCHAR (50) NOT NULL,
  apellido2 VARCHAR (50) NULL,
  apellido3 VARCHAR (50) NULL,
  cedula VARCHAR (15) NOT NULL
  nacimiento DATE NOT NULL NULL,
  es_admin BINARY (1) NOT NULL
);

CREATE TABLE if NOT EXISTS instrumentos (
  ID INT(10) UNSIGNED NOT NULL PRIMARY KEY,
  nombre VARCHAR(30) NOT NULL,
  preguntas JSON NULL
);

CREATE TABLE if NOT EXISTS carreras(
  codigo VARCHAR (10) NOT NULL PRIMARY KEY,
  nombre VARCHAR (30) NOT NULL
);

CREATE TABLE if NOT EXISTS tipos_de_contrato(
  ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  tipo VARCHAR (20) NOT NULL
);

CREATE TABLE if NOT EXISTS evaluadores (
  ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  es_coordinador BINARY (1) NOT NULL,
  carreras_codigo VARCHAR (10) NOT NULL,
  usuarios_ID INT (10) UNSIGNED NOT NULL
);

CREATE TABLE if NOT EXISTS profesores (
  ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  usuarios_ID INT (10) UNSIGNED NOT NULL,
  tipos_de_contrato_ID INT (10) UNSIGNED NOT NULL
);

CREATE TABLE if NOT EXISTS evaluaciones(
  ID INT (10) UNSIGNED NOT NULL PRIMARY KEY,
  resultados JSON NULL,
  fecha DATE NULL,
  tipo INT (10) UNSIGNED NOT NULL,
  instrumentos_ID INT (10) UNSIGNED NOT NULL,
  profesores_ID INT (10) UNSIGNED NOT NULL,
  evaluadores_ID INT (10) UNSIGNED NOT NULL
);

CREATE TABLE if NOT EXISTS materias(
  codigo VARCHAR (20) NOT NULL PRIMARY KEY,
  nombre VARCHAR (45) NOT NULL,
  profesores_ID INT (10) UNSIGNED NOT NULL,
  carreras_codigo VARCHAR (10) NOT NULL
);

CREATE TABLE if NOT EXISTS horarios(
  ID INT (10) UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
  modulo CHAR (50) NULL,
  dia VARCHAR (20) NULL,
  hora_inicio TIME NOT NULL,
  hora_final TIME NOT NULL,
  materias_codigo VARCHAR (45)
);  