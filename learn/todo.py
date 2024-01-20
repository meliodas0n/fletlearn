import flet as ft

class TodoApp(ft.UserControl):
  def build(self):
    self.new_task = ft.TextField(hint_text = "Whats needs to be done?", expand = True)
    self.tasks = ft.Column()
    return ft.Column(
        width = 600,
        controls = [
          ft.Row(
            controls = [
              self.new_task,
              ft.FloatingActionButton(icon = ft.icons.ADD, on_click = self.add_clicked),
              ],
            ),
            self.tasks,
          ],
        )

  def add_clicked(self, e):
    self.tasks.controls.append(ft.Checkbox(label = self.new_task.value))
    self.new_task.value = ""
    self.update()

def main(page: ft.Page):
  page.title = "Todo App"
  page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
  page.update()
  todo = TodoApp()
  page.add(todo)

class App():
  def __init__(self):
    self.app = ft.app(target = main)
