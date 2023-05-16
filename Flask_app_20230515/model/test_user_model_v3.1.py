import unittest

from unittest.mock import patch

from user_model import user_model

class UserModelTest(unittest.TestCase):

    def setUp(self):
        self.user_model = user_model()

        # Mock the database connection
        self.mock_conn = mock.Mock()
        self.mock_cur = mock.Mock()
        self.user_model.DB_connection = lambda: (self.mock_conn, self.mock_cur)

    def test_user_getall_model(self):
        # Arrange
        schema = "flask_tutorial"
        table = "user_details"

        # Act
        result = self.user_model.user_getall_model(schema, table)

        # Assert
        self.mock_cur.execute.assert_called_with(f"select * from {schema}.{table}")
        self.assertIsInstance(result, dict)
        self.assertIn("message", result)
        self.assertIsInstance(result["message"], list)

    def test_user_truncate(self):
        # Arrange
        schema = "flask_tutorial"
        table = "user_details"

        # Act
        result = self.user_model.user_truncate(schema, table)

        # Assert
        self.mock_cur.execute.assert_called_with(f"truncate table {schema}.{table}")
        self.assertEqual(result, "Truncate table")

    def test_user_addone_model(self):
        # Arrange
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890",
            "role": "admin",
            "password": "password"
        }

        # Act
        result = self.user_model.user_addone_model(data)

        # Assert
        self.mock_cur.execute.assert_called_with(f"insert into flask_tutorial.user_details(name,email,phone,role,password) values ('{data['name']}','{data['email']}','{data['phone']}','{data['role']}','{data['password']}')")
        self.assertEqual(result, make_response({"message": "user created successfully"}, 201))

    def test_user_update_model(self):
        # Arrange
        data = {
            "name": "Jane Doe",
            "email": "janedoe@example.com",
            "phone": "9876543210",
            "role": "user",
            "password": "password"
        }

        # Act
        result = self.user_model.user_update_model(data)

        # Assert
        self.mock_cur.execute.assert_called_with(f"update flask_tutorial.user_details set name ='{data['name']}',email ='{data['email']}',phone='{data['phone']}',role='{data['role']}',password='{data['password']}' where id={data['id']}")
        self.assertEqual(result, make_response({"message": "user updated successfully"}, 201))

    def test_user_delete_model(self):
        # Arrange
        id = 1

        # Act
        result = self.user_model.user_delete_model(id)

        # Assert
        self.mock_cur.execute.assert_called_with(f"delete from flask_tutorial.user_details  where id={id}")
        self.assertEqual(result, make_response({"message": "user deleted successfully"}, 200))

    def test_user_patch_model(self):
        # Arrange
        data = {
            "name": "John Smith"
        }
        id = 1

        # Act
        result = self.user_model.user_patch_model(data, id)

        # Assert
        self.mock_cur.execute.assert_called_with(f"update flask_tutorial.user_details set {', '.join([f'{key}={data[key]}' for key in data])} where id = {
def test_user_pagination_model(self):
    # Arrange
    limit = 10
    pageno = 1

    # Act
    result = self.user_model.user_pagination_model(limit, pageno)

    # Assert
    self.mock_cur.execute.assert_called_with(f"select * from flask_tutorial.user_details LIMIT {rownum},{limit}")
    self.assertIsInstance(result, dict)
    self.assertIn("message", result)
    self.assertIsInstance(result["message"], list)

def test_user_upload_avatar_model(self):
    # Arrange
    uid = 1
    filepath = "/path/to/avatar.jpg"

    # Act
    result = self.user_model.user_upload_avatar_model(uid, filepath)

    # Assert
    self.mock_cur.execute.assert_called_with(f"Update flask_tutorial.user_details set avatar='{filepath}' where id = {uid}")
    self.assertEqual(result, make_response({"message": "file uploaded successfully"}, 201))

def test_user_login_model(self):
    # Arrange
    data = {
        "email": "johndoe@example.com",
        "password": "password"
    }

    # Act
    result = self.user_model.user_login_model(data)

    # Assert
    self.mock_cur.execute.assert_called_with(f"select id,name,phone,avatar,role_id from flask_tutorial.user_details where email='{data['email']}'and password='{data['password']}' ")
    self.assertIsInstance(result, dict)
    self.assertIn("token", result)