# cc-crispdm
## First version of CRISP-DM template using cookie-cutter

#### [Project at](https://github.com/apolotakeshi/cc-crispdm)

### Requirements to use the cookiecutter template:
-----------
 - Python 2.7 or 3.5
 - [Cookiecutter Python package](http://cookiecutter.readthedocs.org/en/latest/installation.html) >= 1.4.0: This can be installed with pip by or conda depending on how you manage your Python packages:

``` bash
$ pip install cookiecutter
```

or

``` bash
$ conda config --add channels conda-forge
$ conda install cookiecutter
```

### To start a new project using this template, run:
------------

    cookiecutter https://github.com/apolotakeshi/cc-crispdm.git

### The resulting directory structure
------------

The directory structure of your new project looks like this: 

```
├── README.md          <- The top-level README for developers using this project.
├── data
│   ├── external       <- Data from third party sources.
│   ├── interim        <- Intermediate data that has been transformed.
│   ├── processed      <- The final, canonical data sets for modeling.
│   └── raw            <- The original, immutable data dump.
│
├── notebooks          <- Jupyter notebooks. Naming convention is a number (for ordering)
│                         and a short `-` delimited description, e.g. `1.0-EDA`.
│                         
│
├── scripts            <- useful scripts used by the project and all other configurable 
|                         .env / .ini / credentials.
│
└── sql                <- required sql code for reproductibility.

```

# Following work will be
## Provide a new template for data scientists

