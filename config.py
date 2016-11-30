import os

class Config(object):
	SECRET_KEY = 'my_secret_token'
	PAGE_ACCESS_TOKEN = 'EAAH2xmhcwU0BACzoo0gGqHyfowf0ZAYact4gxcMXLpY7mxPDrS3aORO7Ey4HZCkBnYYbLhkl9uQu7U3w2sXX6K3ZC3akTR8YVWFG9ZABxSJPxRzUXT6hDD9OuuLBdPLxZCcaMTbM5wYxd5dZCUxOiEqd3ARl8GjBCi8FZAKDcZAjBwZDZD'

class DevelopmentConfig(Config):
	DEBUG = True