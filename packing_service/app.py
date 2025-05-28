from flask import Flask
from routes import packing_routes

app = Flask(__name__)
app.register_blueprint(packing_routes)

if __name__ == "__main__":
    app.run(debug=True)
