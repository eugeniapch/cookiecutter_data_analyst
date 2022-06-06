
# Cookiecuter git
<!-- badges: start -->
ubicación de los archivos en GitHub

<!-- badges: end -->

Aprende a crear tu propia plantilla personalizada utilizando cookiecutter.

## Requiremientos
- [Anaconda](https://www.anaconda.com/download/) >= 4.x
- [git](https://git-scm.com/) >= 2.x
- [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0:
    Esto puede ser instalado con `pip` o `conda` dependiendo cómo tú manejas tus paquetes de Python:

``` bash
pip install cookiecutter
```

o

``` bash
conda install -c conda-forge cookiecutter
```


## Crear un nuevo proyecto

En el directorio en el que quieras guardar tu proyecto generado:

```bash

```


## Estructura de directorios y archivos resultantes

    {{ cookiecutter.nombre_carpeta }}
        ├── data
        │   ├── processed      <- Los datos finales de los dataset procesados
        │   └── raw            <- Datos originales
        │
        ├── notebooks          <- Los notebooks de Jupyter. La convención para nombrarlos es:
                                  número+inicales_autor+_+descripción, ejemplo: `01.0-mepch-explorando_datos`.
        │
        ├── .gitignore         <- Archivos que deben de ser ignorados por `git`.
        │
        ├── environment.yml    <- El archivo de requisitos para reproducir el entorno de análisis.
        │
        └── README.md          <- El archivo de nivel superior para los desarrolladores que utilizan este proyecto.