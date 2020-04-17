import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):

	ABS_PATH = '/'
	PYTHONGRID_DB_HOSTNAME = ''
	PYTHONGRID_DB_NAME = 'sampledb'
	PYTHONGRID_DB_USERNAME = 'root'
	PYTHONGRID_DB_PASSWORD = 'root'
	PYTHONGRID_DB_TYPE = 'mysql+pymysql'
	PYTHONGRID_DB_SOCKET = '/Applications/MAMP/tmp/mysql/mysql.sock'
	PYTHONGRID_DB_CHARSET = ''

	SECRET_KEY = os.environ.get('SECRET_KEY') or 'abcdefghijklmnopqrstuvwxyz'

	#SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
	#	'sqlite:///' + os.path.join(basedir, 'app.db')
	#SQLALCHEMY_TRACK_MODIFICATIONS = False
