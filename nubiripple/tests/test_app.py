import unittest

from nubiripple.app import app


class TestApp(unittest.TestCase):

    def test_database_connection(self):

        test_app = app.test_client()
        r = test_app.get('/')
        self.assertEqual(r.status_code, 200)


if __name__ == '__main__':
    unittest.main()
