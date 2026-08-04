import flet as ft


def main (page: ft.Page):
    page.title = "Mi primera app con flet"
    mensaje = ft.Text ("Aquí va un mensaje")
    nombre = ft.TextField (label = "Escriba su nombre", autofocus = True)
    
    def mostrar_mensaje (txt_mensaje):
        dialogo = ft.AlertDialog (
            title=ft.Text ("Mensaje"),
            content=ft.Text (txt_mensaje)
        )
        page.show_dialog (dialogo)
        
    def saludar (e):
        if nombre.value == "":
            mensaje.value = "Hola, desconocido"
            
        else:
            mensaje.value = "Hola, " + nombre.value
            page.update
            
        mostrar_mensaje (mensaje.value)
        
    page.add(ft.Text("Hola Isaac!"),
    ft.Button ("Click aquí!", on_click = saludar),
    mensaje,
    nombre
    
    )
    

ft.run(main)