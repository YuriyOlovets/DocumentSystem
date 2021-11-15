from app import create_app, env

app = create_app()
if __name__ == '__main__':
    app.run(port=env.PORT, host=env.HOST, debug=env.DEBUG)
