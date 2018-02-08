from system import create_app, connect_db
from common.settings import SETTINGS

app = create_app()
connect_db(SETTINGS['DB_NAME'], SETTINGS['DB_HOST'])

if __name__ == '__main__':
    app.run(host=app.config['HOST'])