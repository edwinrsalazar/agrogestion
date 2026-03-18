CREATE DATABASE AGROGESTION;
USE AGROGESTION;

CREATE TABLE USUARIOS (
id_usuarios INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
documento VARCHAR(20),
telefono VARCHAR(20),
correo VARCHAR(100),
username VARCHAR(100),
password VARCHAR(255),
rol VARCHAR(30)
);

CREATE TABLE FINCA (
id_finca INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
ubicacion VARCHAR(150),
propietario VARCHAR(100),
id_usuarios INT,
FOREIGN KEY (id_usuarios) REFERENCES USUARIOS (id_usuarios)
);

CREATE TABLE PARCELA (
id_parcela INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
tamano_hectareas DECIMAL(5,2),
id_finca INT, 
FOREIGN KEY (id_finca) REFERENCES FINCA (id_finca)
);

CREATE TABLE CULTIVO (
id_cultivo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
tipo VARCHAR(50),
tiempo_cosecha_dias int
);

CREATE TABLE SIEMBRA (
id_siembra INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha_siembra DATE,
cantidad_semillas INT,
id_parcela INT,
id_cultivo INT,
FOREIGN KEY (id_parcela) REFERENCES PARCELA (id_parcela),
FOREIGN KEY (id_cultivo) REFERENCES CULTIVO (id_cultivo)
);

CREATE TABLE INSUMO (
id_insumo INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
tipo VARCHAR(50),
costo_unitario DECIMAL(10,2)
);

CREATE TABLE TRABAJADOR (
id_trabajador INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
documento_identidad VARCHAR(20),
cargo VARCHAR(50),
salario DECIMAL(10,2),
id_finca INT,
FOREIGN KEY (id_finca) REFERENCES FINCA (id_finca) 
);

CREATE TABLE PRODUCCION (
id_produccion INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha_cosecha DATE,
cantidad_kg DECIMAL(10,2),
calidad VARCHAR(50),
id_siembra INT,
FOREIGN KEY (id_siembra) REFERENCES SIEMBRA (id_siembra)
);

CREATE TABLE SIEMBRA_INSUMO (
id_siembra INT,
id_insumo INT,
cantidad_utilizada INT,
PRIMARY KEY (id_siembra, id_insumo),
FOREIGN KEY (id_siembra) REFERENCES SIEMBRA (id_siembra),
FOREIGN KEY (id_insumo) REFERENCES INSUMO (id_insumo)
);

CREATE TABLE ACTIVIDAD (
id_actividad INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
tipo_actividad VARCHAR(50),
descripcion TEXT,
fecha DATE,
id_siembra INT,
FOREIGN KEY (id_siembra) REFERENCES SIEMBRA (id_siembra)
);

CREATE TABLE VENTA (
id_venta INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha DATE,
cliente VARCHAR(100),
cantidad_kg DECIMAL(10,2),
precio_kg DECIMAL(10,2),
id_produccion INT,
FOREIGN KEY (id_produccion) REFERENCES PRODUCCION (id_produccion)
);

CREATE TABLE COMPRA_INSUMO (
id_compra INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha DATE,
proveedor VARCHAR(100),
cantidad INT,
precio_total DECIMAL(10,2),
id_insumo INT,
FOREIGN KEY (id_insumo) REFERENCES INSUMO (id_insumo)
);

CREATE TABLE MAQUINARIA (
id_maquinaria INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
nombre VARCHAR(100),
tipo VARCHAR(50),
estado VARCHAR(50),
fecha_adquisicion DATE,
id_finca INT,
FOREIGN KEY (id_finca) REFERENCES FINCA (id_finca)
);

CREATE TABLE MANTENIMIENTO (
id_mantenimiento INT PRIMARY KEY AUTO_INCREMENT NOT NULL,
fecha DATE,
descripcion TEXT,
costo DECIMAL(10,2),
id_maquinaria INT,
FOREIGN KEY (id_maquinaria) REFERENCES MAQUINARIA (id_maquinaria)
);

CREATE TABLE INVENTARIO (
    id_producto INT AUTO_INCREMENT PRIMARY KEY,
    nombre_producto VARCHAR(100),
    cantidad INT,
    unidad VARCHAR(20)
);

SELECT * FROM usuarios;

INSERT INTO usuarios (nombre, documento, telefono, correo, username, password, rol)
VALUES ('Administrador', '0000', '0000', 'admin@agro.com', 'admin', 'admin123', 'admin');

INSERT INTO ACTIVIDAD (tipo_actividad, descripcion, fecha, id_siembra)
VALUES ('Riego', 'Riego por goteo', '2026-03-05', 1);

INSERT INTO VENTA (fecha, cliente, cantidad_kg, precio_kg, id_produccion)
VALUES ('2026-03-06', 'Central de Abastos', 500, 2500, 1);

INSERT INTO MAQUINARIA (nombre, tipo, estado, fecha_adquisicion, id_finca)
VALUES ('Tractor John Deere', 'Tractor', 'Operativo', '2024-05-10', 1);

INSERT INTO MANTENIMIENTO (fecha, descripcion, costo, id_maquinaria)
VALUES ('2026-03-01', 'Cambio de aceite y revisión general', 250000, 1);