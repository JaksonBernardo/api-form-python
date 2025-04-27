from api.extensions import db
from api import create_app

app = create_app()

if __name__ == "__main__":

    db.init_app(app)
    app.run(debug = True, host = '0.0.0.0', port = 5000)
