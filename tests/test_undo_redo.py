import unittest
from text_editor import TextEditor


class TestUndoRedo(unittest.TestCase):

    def setUp(self):
        self.editor = TextEditor()

    def test_edit_teks(self):
        self.editor.edit("Halo Dunia")

        self.assertEqual(
            self.editor.get_text(),
            "Halo Dunia"
        )

    def test_undo(self):
        self.editor.edit("Teks pertama")
        self.editor.edit("Teks kedua")

        self.editor.undo()

        self.assertEqual(
            self.editor.get_text(),
            "Teks pertama"
        )

    def test_redo(self):
        self.editor.edit("Teks pertama")
        self.editor.edit("Teks kedua")

        self.editor.undo()
        self.editor.redo()

        self.assertEqual(
            self.editor.get_text(),
            "Teks kedua"
        )

    def test_undo_dan_redo_berulang(self):
        self.editor.edit("A")
        self.editor.edit("B")
        self.editor.edit("C")

        self.editor.undo()
        self.editor.undo()

        self.assertEqual(self.editor.get_text(), "A")

        self.editor.redo()

        self.assertEqual(self.editor.get_text(), "B")

    def test_edit_baru_menghapus_riwayat_redo(self):
        self.editor.edit("A")
        self.editor.edit("B")

        self.editor.undo()
        self.editor.edit("C")

        self.editor.redo()

        self.assertEqual(self.editor.get_text(), "C")


if __name__ == "__main__":
    unittest.main()
