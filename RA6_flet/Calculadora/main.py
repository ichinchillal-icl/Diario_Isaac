from dataclasses import field

import flet as ft 


    
@ft.control
class CalcButton (ft.Button):
    expand: int = field(default_factory=lambda: 1)
    
@ft.control
class DigitButton (CalcButton):
    bgcolor: ft.Colors = ft.Colors.WHITE_24
    color: ft.Colors = ft.Colors.WHITE

@ft.control
class ActionButton (CalcButton):
    bgcolor: ft.Colors = ft.Colors.ORANGE
    color: ft.Colors = ft.Colors.WHITE
    
@ft.control
class ExtraActionButton (CalcButton):
    bgcolor: ft.Colors = ft.Colors.BLUE_GREY_100
    color: ft.Colors = ft.Colors.BLACK
    

@ft.control
class CalculatorApp (ft.Container):
    def init (self): 
        self.width = 350
        self.bgcolor = ft.Colors.BLACK
        self.border_radius = ft.BorderRadius.all (20)
        self.padding = 20
        self.result = ft.Text (value = "0", color = ft.Colors.WHITE, size = 20)
        self.content = ft.Column (
            controls = [
            ft.Row (
                controls = [self.result], 
                alignment = ft.MainAxisAlignment.END
            ),
            
            ft.Row (
                controls = [
                    ExtraActionButton (content = "AC"), 
                    ExtraActionButton (content = "+/-"), 
                    ExtraActionButton (content = "%"), 
                    ActionButton (content = "/"),
                ]
            ),
            
            ft.Row (
                controls = [
                    DigitButton (content = "7"), 
                    DigitButton (content = "8"), 
                    DigitButton (content = "9"), 
                    ActionButton (content = "*")
                ]
            ),
            
            ft.Row (
                controls = [
                    DigitButton (content = "4"), 
                    DigitButton (content = "5"), 
                    DigitButton (content = "6"), 
                    ActionButton (content = "-")
                ]
            ),
            
            ft.Row (
                controls = [
                    DigitButton (content = "1"), 
                    DigitButton (content = "2"), 
                    DigitButton (content = "3"), 
                    ActionButton (content = "+")
                ]
            ),
            
            ft.Row (
                controls = [
                    DigitButton (content = "0", expand = 2), 
                    DigitButton (content = "."), 
                    ActionButton (content = "=")
                ]
            ),
        ]
    )

def button_clicked (self, e):
    data = e.control.content
    print (f"Button clicked with data = {data}")
    if self.result.value == "Error" or data == "AC":
        self.result.value = "0"
        self.reset ()
        
    elif data in ("1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "."):
        if self.result.value == "0" or self.new_operand:
            self.result.value = data
            self.new_operand = False
            
        else:
            self.result.value = self.result.value + data
        
    elif data in ("+", "-", "*", "/"):
        self.result.value = self.calculate(
            self.operand1, float(self.result.value), self.operator
        )
        self.operator = data
        if self.result.value == "Error":
            self.operand1 = 0
            
        else:
            self.operand1 = float (self.result.value)
            
        self.new_operand = "0"

    elif data in ("="):
        self.result.value = self.calculate (
            self.operand1, float (self.result.value), self.operator
        )
        self.reset()
        
    elif data in ("%"):
        self.result.value = float (self.result.value) / 100
        self.reset ()
        
def main(page: ft.Page):
    page.title = "Calc App"
    calc1 = CalculatorApp ()
    #calc2 = CalculatorApp ()
    page.add (calc1)

ft.run (main)