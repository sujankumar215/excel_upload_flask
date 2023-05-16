import unittest
from unittest.mock import patch, MagicMock
from flask import Response
from pandas import DataFrame
from datetime import datetime, timedelta
import jwt
from model.user_models import user_model

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.user_model = user_model()

    def tearDown(self):
        pass

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_getall_model_with_records(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = [('John', 'john@example.com', '1234567890')]
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        result = self.user_model.user_getall_model('schema', 'table')

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with('select * from schema.table')
        mock_make_response.assert_called_once_with({'message': [('John', 'john@example.com', '1234567890')]}, 200)

        self.assertEqual(result, mock_make_response.return_value)

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_getall_model_with_no_records(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.fetchall.return_value = []
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        result = self.user_model.user_getall_model('schema', 'table')

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with('select * from schema.table')
        mock_make_response.assert_called_once_with({'message': 'No Records found'}, 204)

        self.assertEqual(result, mock_make_response.return_value)
@patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_truncate_success(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        result = self.user_model.user_truncate('schema', 'table')

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with('truncate table schema.table')
        self.assertEqual(result, 'Truncate table')

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_truncate_exception(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.execute.side_effect = Exception('Table not truncated')
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        result = self.user_model.user_truncate('schema', 'table')

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with('truncate table schema.table')
        self.assertEqual(result, 'Table not truncted')

    @patch('user_model.mysql.connector.connect')
    def test_Insert_query(self, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor
        mock_cursor.description = [('id',), ('name',), ('email',), ('phone',), ('role',), ('password',)]

        result = self.user_model.Insert_query('schema', 'table', 1, 4)

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        expected_query = "INSERT INTO schema.table(name,email,phone)VALUES(%s,%s,%s)"
        self.assertEqual(result, expected_query)

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_addone_model(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        data = {'name': 'John', 'email': 'john@example.com', 'phone': '1234567890', 'role': 'user', 'password': 'password'}
        result = self.user_model.user_addone_model(data)

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with(
            "insert into flask_tutorial.user_details(name,email,phone,role,password) values "
            "('John','john@example.com','1234567890','user','password')"
        )
        mock_make_response.assert_called_once_with({'message': 'user created successfully'}, 201)

        self.assertEqual(result, mock_make_response.return_value)

        @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_update_model_success(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        data = {'id': 1, 'name': 'John', 'email': 'john@example.com', 'phone': '1234567890', 'role': 'user', 'password': 'password'}
        result = self.user_model.user_update_model(data)

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with(
            "update flask_tutorial.user_details set name ='John',email ='john@example.com',phone='1234567890',"
            "role='user',password='password' where id=1"
        )
        mock_make_response.assert_called_once_with({'message': 'user updated successfully'}, 201)

        self.assertEqual(result, mock_make_response.return_value)

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_update_model_not_updated(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 0
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        data = {'id': 1, 'name': 'John', 'email': 'john@example.com', 'phone': '1234567890', 'role': 'user', 'password': 'password'}
        result = self.user_model.user_update_model(data)

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with(
            "update flask_tutorial.user_details set name ='John',email ='john@example.com',phone='1234567890',"
            "role='user',password='password' where id=1"
        )
        mock_make_response.assert_called_once_with({'message': 'not updated'}, 204)

        self.assertEqual(result, mock_make_response.return_value)

    @patch('user_model.mysql.connector.connect')
    @patch('user_model.make_response')
    def test_user_delete_model_success(self, mock_make_response, mock_connect):
        mock_cursor = MagicMock()
        mock_cursor.rowcount = 1
        mock_connect.return_value.__enter__.return_value.cursor.return_value = mock_cursor

        result = self.user_model.user_delete_model(1)

        mock_connect.assert_called_once_with(
            host='hostname', username='username', password='password', database='database', port='port'
        )
        mock_cursor.execute.assert_called_once_with("delete from flask_tutorial.user_details  where id=1")
        mock_make_response.assert_called_once_with({'message': 'user deleted successfully'}, 200)

        self.assertEqual(result, mock_make_response.return_value)
    # Write similar test cases for other methods

if __name__ == '__main__':
    unittest.main()
