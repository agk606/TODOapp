import unittest
from peewee import SqliteDatabase

from apis.models import Task

MODELS = [Task]

test_db = SqliteDatabase('test.db')


class TaskTestCase(unittest.TestCase):
    def setUp(self):
        test_db.bind(MODELS, bind_refs=False, bind_backrefs=False)
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()

    def test_create_task(self):
        data = [
            {'title': 'first_title', 'content': 'first_content'},
            {'title': 'second_title', 'content': 'second_content'},
            {'title': 'third_title', 'content': 'third_content'},
            {'title': 'forth_title', 'content': 'forth_content'},
            {'title': 'fifth_title', 'content': 'fifth_content'},
        ]
        tasks = Task.insert_many(data).execute()
        self.assertEqual(tasks, 5)

    def test_change_task(self):
        Task.create(title='test_task', content='test_content')
        result = Task.update({Task.title: 'change_task'}).where(Task.id == 1)
        result.execute()
        self.assertEqual(Task.get(1).title, 'change_task')

    def test_get_task(self):
        Task.create(title='test_task', content='test_content')
        self.assertEqual(Task.get(1).title, 'test_task')
        self.assertEqual(Task.get(1).content, 'test_content')

    def test_get_list(self):
        data = [
            {'title': 'first_title', 'content': 'first_content'},
            {'title': 'second_title', 'content': 'second_content'},
            {'title': 'third_title', 'content': 'third_content'},
            {'title': 'forth_title', 'content': 'forth_content'},
            {'title': 'fifth_title', 'content': 'fifth_content'},
        ]
        Task.insert_many(data).execute()
        for i in range(1, 6):
            self.assertEqual(Task.get(i).title, data[i - 1]['title'])
            self.assertEqual(Task.get(i).content, data[i - 1]['content'])

    def test_delete_task(self):
        Task.create(title='test_task', content='test_content')
        task = Task.get(1)
        self.assertEqual(task.delete_instance(), 1)


if __name__ == '__main__':
    unittest.main()
