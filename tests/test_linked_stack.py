import unittest
from linked_stack import LinkedStack


class TestLinkedStack(unittest.TestCase):

    def setUp(self):
        self.stack = LinkedStack()

    def test_stack_awalnya_kosong(self):
        self.assertTrue(self.stack.is_empty())

    def test_push_data(self):
        self.stack.push("Data 1")
        self.assertFalse(self.stack.is_empty())

    def test_pop_data(self):
        self.stack.push("Data 1")
        self.stack.push("Data 2")

        hasil = self.stack.pop()

        self.assertEqual(hasil, "Data 2")

    def test_prinsip_lifo(self):
        self.stack.push("A")
        self.stack.push("B")
        self.stack.push("C")

        self.assertEqual(self.stack.pop(), "C")
        self.assertEqual(self.stack.pop(), "B")
        self.assertEqual(self.stack.pop(), "A")

    def test_peek_data(self):
        self.stack.push("Data 1")

        self.assertEqual(self.stack.peek(), "Data 1")

    def test_clear_stack(self):
        self.stack.push("A")
        self.stack.push("B")

        self.stack.clear()

        self.assertTrue(self.stack.is_empty())


if __name__ == "__main__":
    unittest.main()
