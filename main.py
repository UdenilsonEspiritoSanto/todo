import flet as ft
import sqlite3
class Todo:
    def __init__(self,page:ft.Page):
        self.page = page
        self.page.bgcolor = ft.colors.WHITE
        self.page.window_width=400
        self.page.window_height=450
        self.page.window_resizable = False
        self.page.window_always_on_top = True
        self.page.title = 'TodoApp'
        self.db_execute('CREATE TABLE IF NOT EXISTS tasks(name,status)')
        self.task=""
        self.main_page()
    
    def db_execute(self,query,params=[]):
         with sqlite3.connect('database.db')as con:
              cur = con.cursor()
              cur.execute(query,params)
              con.commit()
              return cur.fetchall()
              
         
    def tasks_container(self):

        return ft.Container(
            height=self.page.height *0.8,
            content=ft.Column(
                controls=[
                    ft.Checkbox(label='Tarefa-1',value=True)
                ]
            )
        )
    def set_value(self,e):
         self.task = e.control.value
    #funcao inserir dados
    def add(self,e,input_task):
        name = self.task
        status = "incompleto"
        if name:
             self.db_execute(query = 'INSERT INTO tasks VALUES(?,?)',params=[name,status])
             input_task.value = ""
    def main_page(self):
           input_task = ft.TextField(hint_text="Dgite a Tarefa",expand=True,
                                     on_change=self.set_value)

           input_bar = ft.Row(
                controls=[
                     input_task,
                     ft.FloatingActionButton(icon=ft.icons.ADD,
                                             on_click=lambda e:self.add(e,input_task))
                ]
           )
           tab = ft.Tabs(
               selected_index=0,
               tabs=[
                   ft.Tab(text='Tarefas'),
                   ft.Tab(text='Em Andamento'),
                   ft.Tab(text='Realizadas')                                 
                 
                   
               ]
           )
           tasks = self.tasks_container()
           self.page.add(
                
                input_bar,
                tab,
                tasks

           )
ft.app(target=Todo)