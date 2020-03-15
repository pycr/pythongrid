from flask import render_template, flash, redirect, url_for
from app import app
from app.grid import PythonGrid
from app.data import PythonGridDbData
import pymysql.cursors


@app.route('/')
@app.route('/grid')
def index():
	grid = PythonGrid('SELECT * FROM orders', 'orderNumber', 'orders')
	return render_template('grid.html', title='GRID', grid=grid)

@app.route('/data', methods=['GET', 'POST'])
def data():
	data = PythonGridDbData('SELECT * FROM orders')
	return data.getData()


