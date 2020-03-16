# pythonGrid

pythonGrid is an easy way to create a fully working datagrid for Python Flask web framework that connects to a MySql/MariaDB database.

## Requirements

* Python 3.6+
* Flask
* PyMysql

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

pythonGrid current has two main files in `grid.py` and `data.py` in **app** folder.

* `grid.py` is the main Python class that is responsible for creating the datagrid table. It relies on [jqGrid](https://free-jqgrid.github.io/getting-started/index.html), a popular jQuery datagrid plugin, to render grids in the browser. 

* `data.py` is a Python class that returns the data via AJAX to populate the grid from a database.

* `static` contains all of the client side Javascript and CSS files used for rendering.

## Creating the Database

Find the sample database in **sample** folder named `sampledb.sql`. Using your favorite MySQL client such as [MySQL Workbench](https://dev.mysql.com/downloads/workbench/), Create a new database named `sampledb` and run the sample sql script.

## Install Python

First of all, if you don't have Python installed on your computer, download and install from the [Python official website](https://www.python.org/downloads/) now.

To make sure your Python is functional, type `python3` in a terminal window, or just `python` if that does not work. Here is what you should expect to see:

    Python 3.6.3 (v3.6.3:2c5fed86e0, Oct  3 2017, 00:32:08)
    [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

Next, you need to install Flask framework. You got two options.

## Install Flask Framework (Option 1)

The next step is to install Flask web framework, which is a Python package from [PyPI](https://pypi.org/), the official Python package repository. The best way to install from PyPI is to use `pip`, a Python Package manager tool that comes with Python. 

To install Flask, use command below:

    pip install flask

## Install Flask Framework via Virtual Environment (Option 2) - Recommended

The chances are you will get **Permission denied** message because you are trying to install to the operation system that require administrator permission. Instead, it is highly recommended to use [Python virtual environment](https://docs.python.org/3/tutorial/venv.html). Basically, a Python virtual environment is a self-contained separate copy of Python installation. Different applications can then use different virtual environments with different copy of Python without worrying about system permissions.

The following command will creates a virtual environment named `venv` stored in a directory also named `venv`.

    python3 -m venv venv

Activate the new virtual environment:

    source venv/bin/activate

Now the terminal prompt is modified to include the name of the activated virtual environment

    (venv) $ _

With a new virtual environment created and activated, finally let's install Flask:

    pip install flask

## Install PyMySQL

pythonGrid chose the pure Python MySQL client [PyMySQL](https://github.com/PyMySQL/PyMySQL) to connect to MySQL database.

    pip install pymysql

## Configuration

Find file `config.py`, and set the database connection properties according to your environment. You can use socket to connect to your database. 

    PYTHONGRID_DB_HOSTNAME = ''
    PYTHONGRID_DB_NAME = 'sampledb'
    PYTHONGRID_DB_USERNAME = 'root'
    PYTHONGRID_DB_PASSWORD = 'root'
    PYTHONGRID_DB_SOCKET = '/mysql/mysql.sock'

## Initialize Grid

Flask uses *view functions* to handle for the application routes. View functions are mapped to one or more route URLs so that Flask knows what logic to execute when a client requests a given URL such as **"https://example.com/grid"**.

We have two view functions that needs initialization.

### index()

The file `routes.py` contains our `def index()` view functions associate with URL `/` and `/grid`. This means that when a web browser requests either of these two URLs, Flask is going to invoke this function and pass the return value of it back to the browser as a response.

Inside the function, it creates a new instance of the PythonGrid class and assigns this object to the local variable `grid`. Note `orders` is a table from sample database `sampledb.sql`.

    grid = PythonGrid('SELECT * FROM orders', 'orderNumber', 'orders')

The PythonGrid initializer requires three parameters:

1. A simple SQL SELECT statement
2. The database table primary key
3. The database table name

The view function returns the rendered template from `grid.html` template. It passes grid object. 

    return render_template('grid.html', title='GRID', grid=grid)

### data()

In the next view function `data()`, we create a new instance for `PythonGridDbData` class that is responsible for retrieve data from the database.

It has requires only one parameter should be the same SQL SELECT statement used for PythonGrid.

    data = PythonGridDbData('SELECT * FROM orders')

## Hello, Grid!

At this point, we can run our program with the command below

    flask run

It should show you a beautiful datagrid with data come from the table `orders`. 

The pythonGrid supports

* Sort
* Row number
* Toolbar search
* Pagination
* Page size
* Column title
* Hide columns
* Datagrid dimension
* Column width
* Column text alignment