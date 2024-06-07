import unittest


class TestImportLib(unittest.TestCase):
    def test_imports(self):
        import {{cookiecutter.__import_slug}}
        self.assertTrue(isinstance({{cookiecutter.__import_slug}}.__version__, str))
