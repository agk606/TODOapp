from flask_restplus import Api
from .routes import api as ts

api = Api(
    title='TODO app',
    version='1.0'
)

api.add_namespace(ts, path='/api')
