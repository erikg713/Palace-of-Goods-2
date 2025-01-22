import unittest
from marshmallow import ValidationError
from app.schemas.user_schemas import UserSchema

class TestUserSchema(unittest.TestCase):
    def setUp(self):
        self.schema = UserSchema()

    def test_valid_data(self):
        data = {"username": "johndoe", "email": "john@example.com", "role": "user"}
        result = self.schema.load(data)
        self.assertEqual(result["username"], "johndoe")

    def test_invalid_data(self):
        data = {"username": "", "email": "invalid-email", "role": "invalid-role"}
        with self.assertRaises(ValidationError):
            self.schema.load(data)

if __name__ == "__main__":
    unittest.main()
