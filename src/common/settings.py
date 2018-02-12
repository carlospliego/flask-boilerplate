import os

"""[summary]

    When adding settings, be sure to declare them in the SETTINGS dictionary. 
    If this setting is based on an environment variable be sure to add that declaration
    to the try/except block
"""

# check environment variables
try:
    os.environ['JWT_SECRET_KEY']
    os.environ['HOST']
    os.environ['DB_NAME']
    os.environ['DB_HOST']
except KeyError as e:
    print('{} is not defined as an environment variable'.format(e))
    os.system('kill $PPID')
    pass

SETTINGS = {
    'JWT_SECRET_KEY':os.environ['JWT_SECRET_KEY'],
    'HOST':os.environ['HOST'],
    'DB_NAME':os.environ['DB_NAME'],
    'DB_HOST':os.environ['DB_HOST']
}