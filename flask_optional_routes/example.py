if __name__ == '__main__':
    from flask import Flask

    try:
        # package is installed via pip
        from flask_optional_routes import OptionalRoutes
    except:
        # if just downloaded
        from optional_routes import OptionalRoutes


    app = Flask(__name__, template_folder="html")
    optional = OptionalRoutes(app)

    @optional.routes('/a/b?/c/d?/')
    def foobar():
        return 'it worked!'

    if __name__ == "__main__":
        app.run(host='0.0.0.0', port=5000)
