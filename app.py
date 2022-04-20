from flask import Flask
from flask_restful import Api
from src.views.UserView import UserView

app = Flask(__name__)

# 实例化一个 Api 对象，用来创建、管理 RESTful Api
api = Api(app)
api.add_resource(UserView, '/user')

if __name__ == '__main__':
    app.run()
