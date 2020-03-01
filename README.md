#### Universidad Simón Bolívar
#### Departamento de Computación y Tecnología de la Información
#### Enero – Marzo 2020
#### Profesor: Franco Nori

<!-- PROJECT LOGO -->
<br />
<p align="center">

  <h2 align="center">Sistema de Gestion de Empleados/h2>

  <p align="center">
	El proyecto consiste en implementar un sistema que permita gestionar y visualizar el horario de los empleados
  </p>
</p>



<!-- TABLE OF CONTENTS -->
## Tabla de Contenidos

* [Acerca del Proyecto](#acerca-del-proyecto)
  * [Implementado Con](#implementado-con)
* [Comenzando](#comenzando)
  * [Prerequisitos](#prerequisitos)
  * [Instalacion](#instalacion)
* [Como se Usa](#como-se-usa)
* [Equipo](#Equipo)



<!-- Acerca del Proyecto -->
## Acerca del Proyecto

  Proyecto del Curso CI-3725 para el trimestre Enero-Marzo 2020

  Función: Visualizar horas de trabajo de empleados, otorgar vacaciones, entre otros.

  Descripción: La compañía de desarrollo de software Ubicutus Apps está en proceso de mejorar su línea de <br>
    producción y de desarrollo de nuevos proyectos. Por lo que, con la finalidad de mejorar la productividad <br>
    de sus empleados, desea desarrollar una herramienta de seguimiento y auditoría de las horas trabajadas <br>
    por cada desarrollador. Además, desea poder gestionar recursos para los empleados tales como: <br>
    vacaciones, préstamos (o adelantos de capital) e incidencias relacionadas a faltas. <br>


### Implementado Con

Backend:

* [Python3](Python3)
* [Django](Django)
* [DjangoRestFramework] (DjangoRestFramework)

Frontend

* [Angular] (Angular)

## Comenzando

  Sigue los pasos

### Prerequisitos

Python 3 debe estar instalado. <br>
Node.js debe estar instalado <br>
Angular debe estar instalado <br>

### Instalacion
 
Backend

Los requisitos del proyecto se encuentran en requirements.txt
para instalar todas las dependencias correr

```sh
pip install -r requirements.txt
```

Frontend

Los requisitos se encuentran en package.json
para instalarlos correr

```sh
npm install
```

<!-- USAGE EXAMPLES -->
## Como se Usa

Para que funcione el sistema se debe tener arriba ambos servidores

Backend

Actualizar cambios
python manage.py makemigrations

Migrar Cambios
python manage.py migrate

Subir servidor
python manage.py runserver

Frontend

## Development server

Run `ng serve` for a dev server. Navigate to `http://localhost:4200/`. The app will automatically reload if you change any of the source files.

## Code scaffolding

Run `ng generate component component-name` to generate a new component. You can also use `ng generate directive|pipe|service|class|guard|interface|enum|module`.

## Build

Run `ng build` to build the project. The build artifacts will be stored in the `dist/` directory. Use the `-prod` flag for a production build.

## Running unit tests

Run `ng test` to execute the unit tests via [Karma](https://karma-runner.github.io).

## Running end-to-end tests

Run `ng e2e` to execute the end-to-end tests via [Protractor](http://www.protractortest.org/).

## Further help

To get more help on the Angular 6 CLI use `ng help` or go check out the [Angular CLI README](https://github.com/angular/angular-cli/blob/master/README.md).

<!-- CONTACT -->
## Equipo

Backend

Juan Diego Porras - 12-10566 - 12-10566@usb.ve
Kevin Chacon - 13-10268 - 13-10268@usb.ve
Marco Benitez - 13-10137 - 13-10137@usb.ve

Frontend

Luis Carlos Marval - 12-10620 - 12-10620@usb.ve 
Albert Diaz - 11-10278 - 11-10278@usb.ve
Victoria Torres - 12-11468 - 12-11468@usb.ve
