import unittest
from unittest.mock import MagicMock, patch
from flask import Flask
from app import app
from model.user_models import user_model

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.obj = user_model()

    def test_welcome(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'Hello world')

    def test_home(self):
        response = self.app.get('/home')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data.decode('utf-8'), 'this is home page')

    @patch('model.auth_model.auth_model.token_auth')
    @patch('model.user_models.user_model.user_getall_model')
    def test_user_getall_controller(self, mock_user_getall_model, mock_token_auth):
        mock_token_auth.return_value = 'Bearer JWT_TOKEN'
        mock_user_getall_model.return_value = {'message': [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]}

        response = self.app.get('/user/getall')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': [{'id': 1, 'name': 'John'}, {'id': 2, 'name': 'Jane'}]})
        mock_token_auth.assert_called_once()

    @patch('model.auth_model.auth_model.token_auth')
    @patch('model.user_models.user_model.user_addone_model')
    def test_user_addone_controller(self, mock_user_addone_model, mock_token_auth):
        mock_token_auth.return_value = 'Bearer JWT_TOKEN'
        mock_user_addone_model.return_value = {'message': 'User created successfully'}

        response = self.app.post('/user/addone')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': 'User created successfully'})
        mock_token_auth.assert_called_once()

    @patch('model.user_models.user_model.user_update_model')
    def test_user_update_controller(self, mock_user_update_model):
        mock_user_update_model.return_value = {'message': "user updated successfully"}

        response = self.app.put('/user/update')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "user updated successfully"})

    @patch('model.user_models.user_model.user_delete_model')
    def test_user_delete_controller(self, mock_user_delete_model):
        mock_user_delete_model.return_value = {'message': "user deleted successfully"}

        response = self.app.delete('/user/delete/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "user deleted successfully"})

    @patch('model.user_models.user_model.user_patch_model')
    def test_user_patch_controller(self, mock_user_patch_model):
        mock_user_patch_model.return_value = {'message': "user updated successfully"}

        response = self.app.patch('/user/patch/1')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json, {'message': "user updated successfully"})
import unittest
from unittest.mock import MagicMock, patch
from app import app
from model.user_models import user_model
from model.auth_model import auth_model
from flask import Flask, request

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user = user_model()
        self.auth = auth_model()

    def test_user_getall_controller_with_valid_token(self):
        # Mock the request headers and endpoint
        headers = {'Authorization': 'Bearer JWT_TOKEN'}
        endpoint = '/user/getall'
        with patch('model.auth_model.request', headers=headers, url_rule=endpoint):
            # Mock the token decoding to return a valid role ID
            with patch('model.auth_model.jwt.decode') as mock_jwt_decode:
                mock_jwt_decode.return_value = {'payload': {'role_id': 1}}
                # Mock the database query result for the endpoint roles
                with patch('model.auth_model.auth_model.cur.fetchall') as mock_fetchall:
                    mock_fetchall.return_value = [{'roles': '[1, 2, 3]'}]
                    # Call the method under test
                    response = self.app.get('/user/getall')
                    # Assertions
                    self.assertEqual(response.status_code, 200)
                    # Perform additional assertions as needed

    def test_user_getall_controller_with_invalid_token(self):
        # Mock the request headers and endpoint with an invalid token
        headers = {'Authorization': 'Bearer INVALID_TOKEN'}
        endpoint = '/user/getall'
        with patch('model.auth_model.request', headers=headers, url_rule=endpoint):
            # Call the method under test
            response = self.app.get('/user/getall')
            # Assertions
            self.assertEqual(response.status_code, 401)
            # Perform additional assertions as needed

    # Write test cases for other controller methods...

if __name__ == '__main__':
    unittest.main()


import unittest
from unittest.mock import MagicMock, patch
from app import app
from model.user_models import user_model
from model.auth_model import auth_model
from flask import Flask, request

class UserControllerTestCase(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.user = user_model()
        self.auth = auth_model()

    def test_user_getall_controller_with_valid_token(self):
        # Mock the request headers and endpoint
        headers = {'Authorization': 'Bearer JWT_TOKEN'}
        endpoint = '/user/getall'
        with patch('model.auth_model.request', headers=headers, url_rule=endpoint):
            # Mock the token decoding to return a valid role ID
            with patch('model.auth_model.jwt.decode') as mock_jwt_decode:
                mock_jwt_decode.return_value = {'payload': {'role_id': 1}}
                # Mock the database query result for the endpoint roles
                with patch('model.auth_model.auth_model.cur.fetchall') as mock_fetchall:
                    mock_fetchall.return_value = [{'roles': '[1, 2, 3]'}]
                    # Call the method under test
                    response = self.app.get('/user/getall')
                    # Assertions
                    self.assertEqual(response.status_code, 200)
                    # Perform additional assertions as needed

    def test_user_getall_controller_with_invalid_token(self):
        # Mock the request headers and endpoint with an invalid token
        headers = {'Authorization': 'Bearer INVALID_TOKEN'}
        endpoint = '/user/getall'
        with patch('model.auth_model.request', headers=headers, url_rule=endpoint):
            # Call the method under test
            response = self.app.get('/user/getall')
            # Assertions
            self.assertEqual(response.status_code, 401)
            # Perform additional assertions as needed

    # Write additional test cases as needed

if __name__ == '__main__':
    unittest.main()

    

