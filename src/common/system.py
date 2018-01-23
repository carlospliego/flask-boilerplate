from flask import Flask

app = None

def create_app():
    global app
    app = Flask(__name__)
    # if you change host you must also change the running database name too
    # app.config['MONGO_HOST'] = 'mongodb'

    # app.config['MONGO_DBNAME'] = 'flask'
    
    from accounts.views import accounts_app
    app.register_blueprint(accounts_app)
    
    return app