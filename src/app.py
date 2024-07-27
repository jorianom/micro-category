import os
from flask import Flask
from dotenv import load_dotenv
from flask_cors import CORS
from database import mongo
from categories.routes import categories

config = load_dotenv()
app = Flask(__name__)
CORS(app, resources={r'/*': {'origins': '*'}})


app.config['MONGO_URI'] = os.getenv('MONGO_URI')
mongo.init_app(app)


app.register_blueprint(categories, url_prefix='/api/categories')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
