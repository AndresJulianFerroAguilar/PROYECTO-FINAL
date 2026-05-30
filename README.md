# PROYECTO-FINAL
TODAS LAS EVIDENCIAS Y EL READ ME DEL PROYECTO
# Proyecto Final - Detección de Activos de Red con YOLOv8 y Controles de Seguridad

## Descripción

Este proyecto implementa un sistema de detección automática de activos de red utilizando YOLOv8. El modelo fue entrenado para reconocer cinco tipos de dispositivos:

* Firewall
* Hub
* Router
* Server
* Switch

Adicionalmente, se aplicaron controles de seguridad mediante criptografía AES, RSA y funciones hash SHA-256, alineados con conceptos de la norma ISO 27001.

## Objetivo

Desarrollar un sistema capaz de identificar activos de red a partir de imágenes y aplicar mecanismos básicos de protección de la información.

## Tecnologías Utilizadas

* Python 3.11
* YOLOv8 (Ultralytics)
* Label Studio
* Cryptography
* SHA-256
* GitHub

## Módulo 1: Entrenamiento del Modelo

### Recolección de Datos

Se recopilaron 50 imágenes distribuidas entre las siguientes clases:

* Firewall
* Hub
* Router
* Server
* Switch

### Etiquetado

Las imágenes fueron etiquetadas utilizando Label Studio mediante cuadros delimitadores (Bounding Boxes).

### Entrenamiento

Se entrenó un modelo YOLOv8n durante 50 épocas.

### Resultados

* Precision: 0.969
* Recall: 1.000
* mAP50: 0.995
* mAP50-95: 0.858

### Evidencias

* Dataset etiquetado
* Entrenamiento completado
* Archivo best.pt generado
* Matriz de confusión
* Detección exitosa sobre una imagen de prueba

## Módulo 2: Criptografía

### AES

Se cifró una imagen utilizando una clave AES generada automáticamente.

Archivos generados:

* aes_key.key
* prueba_encriptada.bin

### SHA-256

Se calculó el hash SHA-256 de la imagen original para garantizar la integridad.

### RSA + AES

Se generó un par de claves RSA y se utilizó la clave pública para cifrar la clave AES.

Archivos generados:

* private_key.pem
* public_key.pem
* aes_key_encrypted.bin

## Módulo 3: Auditoría ISO 27001

### Matriz de Riesgos

* Acceso no autorizado a imágenes.
* Pérdida de información.
* Alteración de archivos.
* Etiquetado incorrecto.
* Robo de datos.

### Controles Aplicados

* Inventario de activos.
* Clasificación de activos.
* Protección mediante cifrado.
* Verificación de integridad.
* Protección frente a accesos no autorizados.

## Conclusiones

Se logró desarrollar un sistema funcional para la identificación automática de activos de red mediante inteligencia artificial. Asimismo, se implementaron mecanismos de seguridad para proteger la información generada durante el proyecto, aplicando conceptos de criptografía y controles inspirados en ISO 27001.
