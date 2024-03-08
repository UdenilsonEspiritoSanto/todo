import flet as ft

class Todo:
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width=400
        self.page.window_height=450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'TodoApp'
        self.main_page()

   
    def main_page(self):
           input_task = ft.TextField(hint_text="Dgite a Tarefa")

           input_bar = ft.Row(
                controls=[
                     input_task,
                     ft.FloatingActionButton(icon=ft.icons.ADD)
                ]
           )
           self.page.add(
                
                input_bar

           )
ft.app(target=Todo)
