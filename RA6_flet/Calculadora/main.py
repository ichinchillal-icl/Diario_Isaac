import flet as ft 

def main(page: ft.Page):
    page.title = "Calculadora"
    
    result = ft.Text (value = "0", size = 20)
    
    button = ft.Container(
        content = ft.Text ("7"),
        width = 60,
        height = 60,
        alignment = ft.alignment.center,
    )
    page.add (result, button)
ft.run (main)