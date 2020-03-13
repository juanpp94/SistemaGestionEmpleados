#### Universidad Simón Bolívar
#### Departamento de Computación y Tecnología de la Información
#### Enero – Marzo 2020
#### Profesor: Franco Nori

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Sistema de Gestion de Empleados</h2>

  <p align="center">
	El proyecto consiste en implementar un sistema que permita gestionar y visualizar el horario de los empleados
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Tabla de Contenidos

* [Acerca del Proyecto](#acerca-del-proyecto)
  * [Implementado con](#implementado-con)
* [Comenzando](#comenzando)
  * [Prerequisitos](#prerequisitos)
  * [Instalacion](#instalacion)
* [Como se Usa](#como-se-usa)
* [Equipo](#Equipo)



<!-- Acerca del Proyecto -->
## Acerca del Proyecto

  Proyecto del Curso CI-3715 para el trimestre Enero-Marzo 2020

  Función: Visualizar horas de trabajo de empleados, otorgar vacaciones, entre otros.

  Descripción: La compañía de desarrollo de software Ubicutus Apps está en proceso de mejorar su línea de <br>
    producción y de desarrollo de nuevos proyectos. Por lo que, con la finalidad de mejorar la productividad <br>
    de sus empleados, desea desarrollar una herramienta de seguimiento y auditoría de las horas trabajadas <br>
    por cada desarrollador. Además, desea poder gestionar recursos para los empleados tales como: <br>
    vacaciones, préstamos (o adelantos de capital) e incidencias relacionadas a faltas. <br>


### Implementado Con

#### Backend:

* Python3
* Django
* Pillow
* Postgresql

#### Frontend

*Bootstrap

## Comenzando

  Sigue los pasos

### Prerequisitos

Python 3 debe estar instalado. <br>
Pipenv debe estar instalado. <br>
Postgresql debe estar instalado. <br>

### Instalacion

Los requisitos del proyecto se encuentran en requirements.txt
para instalar todas las dependencias correr

<!-- USAGE EXAMPLES -->
## Como se Usa

#### Crear un ambiente de desarrollo python
`pipenv shell`

#### Instalar dependencias
`pip install -r requirements.txt`

#### Crear base de datos ubic en Postgresql
`CREATE DATABASE ubic;`

#### Verficar puerto de postgres 
`Abrir ...\PostgreSQL\12\data\postgresql.conf en bloc de notas y verificar que port = 5432`

#### Cambiar usuario y contraseña en settings.py
`Abrir \ubicutus\settings.py y en las lineas 64 y 65 colocar usuario y contraseña validas correspondientes a su usuario en postgresql`

#### Actualizar cambios
`python manage.py makemigrations`

#### Migrar Cambios
`python manage.py migrate`

#### Subir servidor
`python manage.py runserver`

<!-- CONTACT -->
## Equipo

### Backend

Juan Diego Porras - 12-10566 - 12-10566@usb.ve <br>
Kevin Chacon - 13-10268 - 13-10268@usb.ve <br>
Marco Benitez - 13-10137 - 13-10137@usb.ve <br>

### Frontend

Luis Carlos Marval - 12-10620 - 12-10620@usb.ve  <br>
Albert Diaz - 11-10278 - 11-10278@usb.ve <br>
Victoria Torres - 12-11468 - 12-11468@usb.ve <br>
