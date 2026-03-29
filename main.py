from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput

class CalculatorApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_had_operator = None
        self.last_button = None
        
        main_layout = BoxLayout(orientation="vertical", padding=10, spacing=5)
        
        # شاشة العرض
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=55, size_hint=(1, 0.4)
        )
        main_layout.add(self.solution)
        
        # الأزرار
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        
        from kivy.uix.gridlayout import GridLayout
        grid_layout = GridLayout(cols=4, spacing=5)
        
        for row in buttons:
            for label in row:
                button = Button(text=label, font_size=30, background_color=(0.2, 0.2, 0.2, 1))
                button.bind(on_press=self.on_button_press)
                grid_layout.add(button)
        
        main_layout.add(grid_layout)
        
        equals_button = Button(text="=", font_size=35, size_hint=(1, 0.2), background_color=(0, 0.7, 0.3, 1))
        equals_button.bind(on_press=self.on_solution)
        main_layout.add(equals_button)
        
        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text
        if button_text == "C":
            self.solution.text = ""
        else:
            self.solution.text += button_text

    def on_solution(self, instance):
        if self.solution.text:
            try:
                self.solution.text = str(eval(self.solution.text))
            except:
                self.solution.text = "Error"

if __name__ == "__main__":
    CalculatorApp().run()