import os

class Config(object):
	SECRET_KEY = 'my_secret_token'
	PAGE_ACCESS_TOKEN = 'EAAH2xmhcwU0BAP6czeliRpYNLxvCCH7namIs0tpZCdEgeMq3RIZCZA8rodV2cRpEc5nYIDkwZARwTV2GF8mY8oA1ygCUbFEIAGOK0RlNFceDwpWIKZCYWjqK8rrvKvZBKwmNLNveY882ZBju2wFpYbKTewNMrZBNuMS0l7KlIUedFAZDZD'

class DevelopmentConfig(Config):
	DEBUG = True