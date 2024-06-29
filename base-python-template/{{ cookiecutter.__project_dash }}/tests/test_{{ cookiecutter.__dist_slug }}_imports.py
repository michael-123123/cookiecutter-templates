import unittest


class TestImportLib(unittest.TestCase):
    def test_{{ cookiecutter.__dist_slug }}_imports(self):
        import {{ cookiecutter.__import_slug }}
        self.assertTrue(isinstance({{ cookiecutter.__import_slug }}.__version__, str))
