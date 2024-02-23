from app.app import create_app

app = create_app()

def user_view():
    return {'message': 'Hello World!'}

app.add_url_rule('/', view_func=user_view)


if __name__ == "__main__":
    app.run(debug=True)