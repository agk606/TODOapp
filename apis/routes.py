from flask_restplus import Namespace, Resource, reqparse
from flask import request, jsonify

from apis.models import Task

api = Namespace('todos', description='TODO operations')
parser = reqparse.RequestParser()
parser.add_argument('title')
parser.add_argument('content')


@api.route('/task/', methods=['GET', 'POST'])
class TaskList(Resource):
    """Operations with a list of tasks"""

    def get(self):
        """Get a list of tasks"""
        # for testing in terminal enter: http GET http://localhost:5000/api/task/
        return jsonify([{task.title: task.created_at} for task in Task.select()])

    @api.doc(parser=parser)
    def post(self):
        """Add a new task"""
        # for testing in terminal enter: http POST http://localhost:5000/api/task/ title="title" content="content"
        data = parser.parse_args()
        Task.create(title=data['title'], content=data['content'])
        return jsonify({'Success': 'OK'})


@api.route('/task/<int:task_id>/', methods=['GET', 'PUT', 'PATCH', 'DELETE'])
class TaskItem(Resource):
    """Operations with a single task"""

    def get(self, task_id):
        """Get a single task with given task_id"""
        # for testing in terminal enter: http GET http://localhost:5000/api/task/task_id/
        return jsonify(Task.get(id=task_id).task_info())

    def delete(self, task_id):
        """Delete a single task with given task_id"""
        # for testing in terminal enter: http DELETE http://localhost:5000/api/task/task_id/
        Task.get(task_id).delete_instance()
        return jsonify({'Success': 'OK'})

    @api.doc(parser=parser)
    def put(self, task_id):
        """Change a single task with given task_id"""
        # for testing in terminal enter: http PUT http://localhost:5000/api/task/task_id/ title="title"
        # content="content"
        data = parser.parse_args()
        result = Task.update({Task.title: data['title'], Task.content: data['content']}) \
            .where(Task.id == task_id)
        result.execute()
        return jsonify({'Success': 'OK'})

    @api.doc(parser=parser)
    def patch(self, task_id):
        """Change a single task with given task_id"""
        # for testing in terminal enter: http PATCH http://localhost:5000/api/task/task_id/ title="title"
        # content="content"
        data = parser.parse_args()
        result = Task.update({Task.title: data['title'], Task.content: data['content']}) \
            .where(Task.id == task_id)
        result.execute()
        return jsonify({'Success': 'OK'})
