from flask import render_template, flash, redirect, url_for
from app import app
from app.grid import PythonGrid
from app.data import PythonGridDbData
import pymysql.cursors

@app.route('/')		
def home():
	return render_template('index.html')

@app.route('/<demo>')		
def index(demo):
	grid = PythonGrid('SELECT * FROM orders', 'orderNumber', 'orders')

	if (demo == 'basic'):
		pass

	elif (demo == 'caption'):
		grid.set_caption('Orders Datagrid')

	elif (demo == 'column_title'):
		grid.set_col_title('orderNumber', 'Order #')
		grid.set_col_title('orderDate', 'Order Date')

	elif (demo == 'column_hidden'):
		grid.set_col_hidden(['customerNumber, logTime'])

	elif (demo == 'page_size'):
		grid.set_pagesize(20)

	elif (demo == 'dimension'):
		grid.set_dimension(1000, 400)

	elif (demo == 'search'):
		grid.enable_search(True)

	elif (demo == 'row_numer'):
		grid.enable_rownumbers(True)
		
	elif (demo == 'column_width'):
		grid.set_col_width('orderNumber', 100)
		grid.set_col_width('comments', 500)

	elif (demo == 'column_align'):
		grid.set_col_align('orderNumber', 'right')
		grid.set_col_align('comments', 'center')

	else: # set all properties
		demo = "All"

		grid.set_caption('Orders Table')
		grid.set_col_title('orderDate', 'Order Date')
		grid.set_col_title('orderNumber', 'Order #')
		grid.set_col_hidden(['logTime'])
		grid.set_pagesize(20)
		grid.set_dimension(1000, 400)
		grid.enable_search(True)
		grid.enable_rownumbers(True)
		grid.enable_pagecount(True)
		grid.set_col_width('comments', 500)
		grid.set_col_align('orderNumber', 'right')

	return render_template('grid.html', title=demo, grid=grid)

@app.route('/data', methods=['GET', 'POST'])
def data():
	data = PythonGridDbData('SELECT * FROM orders')
	return data.getData()


