import unittest
from datetime import datetime
from models.state import State


class TestState(unittest.TestCase):

    def setUp(self):
        # This method will be called before each test method
        self.state_instance = State()

    def tearDown(self):
        # This method will be called after each test method
        del self.state_instance

    def test_instance_creation(self):
        instance = self.state_instance
        self.assertIsInstance(instance, State)

    def test_state_attrs(self):
        """
        Test id attribute type 
        Test name attribute type
        """
        self.assertEqual(str, type(self.state_instance.id))
        self.assertEqual(str, type(self.state_instance.name))

    def test_id_unique(self):
        """
        Test that the id attribute is unique
        """
        instance1 = State()
        instance2 = State()
        self.assertNotEqual(instance1.id, instance2.id)

    def test_init_with_attributes(self):
        # Test initialization with specific attributes
        state = State(id="123", name="California")

        self.assertEqual(state.id, "123")
        self.assertEqual(state.name, "California")

    def test_init_with_defaults(self):
        # Test initialization with default values
        state = State()

        self.assertIsNotNone(state.id)
        self.assertEqual(state.name, "")

    def test_str_representation(self):
        # Test the string representation of the state
        state = State(id="123", name="California")

        expected_str = "[State](123){'id': '123', 'name': 'California'}"
        self.assertEqual(state.__str__(), expected_str)

    

    def test_to_dict_method(self):
        instance = self.state_instance
        dictionary = instance.to_dict()
        self.assertIsInstance(dictionary, dict)
        self.assertEqual(dictionary['__class__'], 'State')


if __name__ == '__main__':
    unittest.main()
