from common.system import create_app, connect_db

app = create_app()
connect_db('flask', 'mongodb')

if __name__ == '__main__':
    app.run(host='0.0.0.0')