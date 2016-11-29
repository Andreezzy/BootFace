import os

class Config(object):
	SECRET_KEY = 'my_secret_token'
	PAGE_ACCESS_TOKEN = 'EAAH2xmhcwU0BAOAgYzxz03xLpMkjOs4lrFrjZCFdOO0ZB2VZBtDDd9Iq1dOdJVVV0uI8KGKKaart0yR4ZBcMU4PJFZCoy9oI9gADHYq9ZB1bcRhiWwVNBOeIGVMyLpybhChQZAeYMPx3hH4XePl2ZAyayA2mVTDZBVKrteDMDvze7xQZDZD'

class DevelopmentConfig(Config):
	DEBUG = True