import unittest
from memento import Memento


class TestMemento(unittest.TestCase):

    def test_menyimpan_state(self):
        memento = Memento("Halo Dunia")

        self.assertEqual(memento.get_state(), "Halo Dunia")

    def test_menyimpan_state_kosong(self):
        memento = Memento("")

        self.assertEqual(memento.get_state(), "")

    def test_menyimpan_perubahan_state(self):
        memento1 = Memento("Teks pertama")
        memento2 = Memento("Teks kedua")

        self.assertEqual(memento1.get_state(), "Teks pertama")
        self.assertEqual(memento2.get_state(), "Teks kedua")


if __name__ == "__main__":
    unittest.main()
