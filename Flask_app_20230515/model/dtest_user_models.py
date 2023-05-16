import unittest
from unittest.mock import MagicMock
from model.user_models import user_model

class TestUserModel(unittest.TestCase):

    def setUp(self):
        self.model = user_model()

    def tearDown(self):
        pass

    def test_user_getall_model(self):
        self.model.DB_connection = MagicMock(return_value=(None, None))
        self.model.DB_close = MagicMock()
        response = self.model.user_getall_model()
        self.assertEqual(response.status_code, 200)
        # Add assertions for the expected response data
        # self.assertEqual(response.get_data(as_text=True), ...)

    def test_user_addone_model(self):
        self.model.DB_connection = MagicMock(return_value=(None, None))
        self.model.DB_close = MagicMock()
        data = {
            "name": "John Doe",
            "email": "johndoe@example.com",
            "phone": "1234567890",
            "role": "user",
            "password": "password123"
        }  # Replace with valid data
        response = self.model.user_addone_model(data)
        self.assertEqual(response.status_code, 201)
        # Add assertions for the expected response data
        # self.assertEqual(response.get_data(as_text=True), ...)

    # Add more test cases for other methods

if __name__ == '__main__':
    unittest.main()
