import flet as ft

def main(page: ft.page):
  page.add(ft.Text(value = "Hello, World!"))

class App():
  def __init__(self):
    self.app = ft.app(target = main)