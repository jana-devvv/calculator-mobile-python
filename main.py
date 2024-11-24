from kivy.app import App
from kivy.uix.boxlayout import BoxLayout

class CalculatorLayout(BoxLayout):
    def clear_input(self):
        self.ids.input_text.text = ""

    def append_input(self, value):
        self.ids.input_text.text += value

    def calculate_result(self):
        try:
            expression = self.ids.input_text.text
            result = str(eval(expression))
            self.ids.input_text.text = result
        except Exception:
            self.ids.input_text.text = "Error"

class SimpleCalculatorApp(App):
    def build(self):
        return CalculatorLayout()
    
if __name__ == "__main__":
    SimpleCalculatorApp().run()