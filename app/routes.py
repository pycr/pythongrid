from flask import render_template, flash, redirect, url_for
from app import app
from app.grid import PythonGrid
from app.data import PythonGridDbData
from app.export import PythonGridDbExport

@app.route('/')
def index():
    grid = PythonGrid('SELECT * FROM orders', 'orderNumber', 'orders')

    grid.set_caption('Orders Table')
    grid.set_col_title('orderDate', 'Order Date')
    grid.set_col_title('orderNumber', 'Order #')
    grid.set_col_hidden(['customerNumber, logTime, shippedDate, requiredDate'])
    grid.set_pagesize(20)
    grid.set_dimension(800, 400)
    grid.enable_search(True)
    grid.enable_rownumbers(True)
    grid.enable_pagecount(True)
    grid.set_col_align('status', 'center')
    grid.set_col_width('comments', 600)
    grid.enable_export()

    return render_template('grid.html', title='demo', grid=grid)

@app.route('/data', methods=['GET', 'POST'])
def data():
    data = PythonGridDbData('SELECT * FROM orders')
    return data.getData()

@app.route('/export', methods=['GET', 'POST'])
def export():
    exp = PythonGridDbExport('SELECT * FROM orders')
    return exp.export()