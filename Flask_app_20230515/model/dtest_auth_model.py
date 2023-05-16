import unittest
from unittest.mock import MagicMock
from model.user_models import user_model
from flask import Flask
from unittest.mock import MagicMock

class MockCursor:
    def __init__(self):
        self._execute_result = []
        self._fetchall_result = []

    def execute(self, query):
        pass

    def fetchall(self):
        return self._fetchall_result

    @property
    def rowcount(self):
        return len(self._execute_result)

    def set_execute_result(self, result):
        self._execute_result = result

    def set_fetchall_result(self, result):
        self._fetchall_result = result

class UserModelTestCase(unittest.TestCase):
    
    def setUp(self):
        self.dbconfig = {
            'hostname': 'localhost',
            'username': 'testuser',
            'password': 'testpassword',
            'database': 'testdb',
            'port': 3306
        }
        self.app = Flask(__name__)  # Create a Flask application instance
        self.app_context = self.app.app_context()  # Create an application context
        self.app_context.push()  # Push the context to activate it
        self.user = user_model()

    def tearDown(self):
        self.app_context.pop()

    def test_user_getall_model_with_records(self):
        # Mock the cursor and its methods
        self.user.cur.execute = MagicMock()
        self.user.cur.fetchall = MagicMock(return_value=[{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}])

        # Call the method under test
        response = self.user.user_getall_model()

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]})

    def test_user_getall_model_with_no_records(self):
        # Mock the cursor and its methods
        self.user.cur.execute = MagicMock()
        self.user.cur.fetchall = MagicMock(return_value=[])

        # Call the method under test
        response = self.user.user_getall_model()

        # Assertions
        self.assertEqual(response.status_code, 204)
        self.assertEqual(response.json, {'message': "No Records found"})

    def test_user_addone_model(self):
        # Mock the cursor and its methods
        self.user.cur.execute = MagicMock()

        # Call the method under test
        response = self.user.user_addone_model({'name': 'John', 'email': 'john@example.com', 'phone': '1234567890', 'role': 'user', 'password': 'password'})

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': "user created successfully"})

    def test_user_update_model(self):
        # Mock the cursor and its methods
        cursor_mock = MockCursor()
        cursor_mock.set_execute_result([(1,)])

        self.user.cur = cursor_mock

        # Call the method under test
        response = self.user.user_update_model({'id': 1, 'name': 'John Doe', 'email': 'johndoe@example.com', 'phone': '9876543210', 'role': 'admin', 'password': 'newpassword'})

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': "user updated successfully"})

    def test_user_delete_model(self):
        # Mock the cursor and its methods
        cursor_mock = MockCursor()
        cursor_mock.set_execute_result([(1,)])

        self.user.cur = cursor_mock

        # Call the method under test
        response = self.user.user_delete_model(1)

        # Assertions
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "user deleted successfully"})

    def test_user_patch_model(self):
        # Mock the cursor and its methods
        cursor_mock = MockCursor()
        cursor_mock.set_execute_result([(1,)])

        self.user.cur = cursor_mock

        # Call the method under test
        response = self.user.user_patch_model({'name': 'John Doe', 'email': 'johndoe@example.com'}, 1)

        # Assertions
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json, {'message': "user updated successfully"})

if __name__ == '__main__':
    unittest.main()
