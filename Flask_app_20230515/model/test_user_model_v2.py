import unittest
from unittest import mock
from datetime import datetime, timedelta
from flask import make_response
import jwt
from pandas import DataFrame
from user_model import user_model

class UserModelTestCase(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        cls.user = user_model()
    
    @mock.patch('user_model.mysql.connector.connect')
    def test_user_getall_model(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.fetchall.return_value = [('user1', 'email1', 'phone1', 'role1', 'password1')]
        
        result = self.user.user_getall_model('schema', 'table')
        
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('select * from schema.table')
        self.assertEqual(result.status_code, 200)
        self.assertEqual(result.json, {'message': [('user1', 'email1', 'phone1', 'role1', 'password1')]})
        
    @mock.patch('user_model.mysql.connector.connect')
    def test_user_truncate(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        
        result = self.user.user_truncate('schema', 'table')
        
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('truncate table schema.table')
        self.assertEqual(result, 'Truncate table')
        
    @mock.patch('user_model.mysql.connector.connect')
    def test_Insert_query(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.description = [('name',), ('email',), ('phone',), ('role',), ('password',)]
        
        result = self.user.Insert_query('schema', 'table', 0, 3)
        
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with('select * from schema.table')
        self.assertEqual(result, "INSERT INTO schema.table(name,email,phone)VALUES(%s,%s,%s)")
        
    @mock.patch('user_model.mysql.connector.connect')
    def test_user_addone_model(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        
        result = self.user.user_addone_model({'name': 'user1', 'email': 'email1', 'phone': 'phone1', 'role': 'role1', 'password': 'password1'})
        
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with("insert into flask_tutorial.user_details(name,email,phone,role,password) values ('user1','email1','phone1','role1','password1')")
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json, {'message': 'user created successfully'})
        
    @mock.patch('user_model.mysql.connector.connect')
    def test_user_update_model(self, mock_connect):
        mock_cursor = mock_connect.return_value.cursor.return_value
        mock_cursor.rowcount = 1
        
        result = self.user.user_update_model({'id': 1, 'name': 'user1', 'email': 'email1', 'phone': 'phone1', 'role': 'role1', 'password': 'password1'})
        
        mock_connect.assert_called_once()
        mock_cursor.execute.assert_called_once_with("update flask_tutorial.user_details set name ='user1',email ='email1',phone='phone1',role='role1',password='password1' where id=1")
        self.assertEqual(result.status_code, 201)
        self.assertEqual(result.json, {'message': 'user updated successfully'})
        
