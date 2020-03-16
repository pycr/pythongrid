# pythonGrid

pythonGrid is an easy way to create a fully working datagrid for Python Flask web framework that connects to a MySql/MariaDB database.

## Requirements

* Python 3.6+
* Flask
* PyMysql

## Install

First of all, if you don't have Python installed on your computer, go ahead and download and install from the [Python official website](https://www.python.org/downloads/) now.

To make sure your Python is functional, type `python3` in a terminal window, or just `python` if that does not work. Here is what you should expect to see:

    Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

The next step is to install Flask web framework, which is a Python package from [PyPI](https://pypi.org/), the official Python package repository. The best way to install from PyPI is to use `pip`, a Python Package manager tool that comes with Python. 

To install Flask, use command below:

    pip install flask

The chances are you will get **Permission denied** message because you are trying to install to the operation system that require administrator permission. Instead, it is highly recommended to use [Python virtual environment](https://docs.python.org/3/tutorial/venv.html). Basically, a Python virtual environment is a self-contained separate copy of Python installation. Different applications can then use different virtual environments with different copy of Python without worrying about system permissions.

The following command will creates a virtual environment named `venv` stored in a directory also named `venv`.

    python3 -m venv venv

Activate the new virtual environment:

    source venv/bin/activate

Now the terminal prompt is modified to include the name of the activated virtual environment

    (venv) $ _

With a new virtual environment created and activated, finally let's install Flask:

    pip install flask


pythonGrid chose the pure Python MySQL client [PyMySQL](https://github.com/PyMySQL/PyMySQL) to connect to MySQL database.

    pip install pymysql

Finally, run Flask

    flask run

## Quick Start

A couple quick start options are available:

* [Download the latest release](https://github.com/pycr/pythongrid/archive/master.zip)
* Clone the repo: git clone https://github.com/pycr/pythongrid.git

## Files included

Within the download you will see something like this:

    ├── LICENSE
    ├── README.md
    ├── app
    │   ├── __init__.py
    │   ├── data.py
    │   ├── grid.py
    │   ├── routes.py
    │   ├── static
    │   └── templates
    │       ├── 404.html
    │       ├── base.html
    │       ├── grid.html
    │       └── index.html
    ├── sample
    │   ├── sampledb.sql
    ├── config.py
    ├── index.py
    └── requirements.txt


## Creating the Database

Before moving forward, [install MySQL](https://dev.mysql.com/doc/mysql-getting-started/en/#mysql-getting-started-installing) or MariaDB database on your local development environment or in [Docker](https://hub.docker.com/_/mysql).

