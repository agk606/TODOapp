from flask import Flask
from apis import api
from apis.models import db, Task

app = Flask(__name__)
api.init_app(app)

if __name__ == '__main__':
    db.connect()
    Task.create_table(safe=True)
    app.run(debug=True)
