import unittest
from unittest.mock import Mock
import flet as ft
from app import main, App

class TestApp(unittest.TestCase):
    def test_main(self):
        # Mock the page object
        page = Mock(spec=ft.page)
        main(page)
        # Verify that the add method was called with a Text object
        page.add.assert_called_once()

    def test_app_init(self):
        app = App()
        # Verify that the app attribute is an instance of ft.app
        self.assertIsInstance(app.app, ft.app)

if __name__ == '__main__':
    unittest.main()