from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.popup import Popup
import chempy
from chempy import balance_stoichiometry

class ChemicalReactionApp(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(orientation='vertical', padding=10, spacing=10, **kwargs)
        self.background_color = (0,0,0, 1)  # Màu nền 
        
        self.add_widget(Label(text='Nhập chất phản ứng :', color=(1, 11, 0, 1)))  # Màu chữ vàngvàng
        self.reactants_input = TextInput(multiline=False, background_color=(1, 1, 1, 1), foreground_color=(0, 0, 0, 1))
        self.add_widget(self.reactants_input)
        
        self.add_widget(Label(text='Nhập sản phẩm :', color=(1, 11, 0, 1)))
        self.products_input = TextInput(multiline=False, background_color=(1,11,11,1), foreground_color=(0, 0, 0, 1))
        self.add_widget(self.products_input)
        
        self.balance_button = Button(text='Cân bằng phương trình', size_hint=(1, 0.2), background_color=(0,0,0, 1))
        self.balance_button.bind(on_press=self.balance_equation)
        self.add_widget(self.balance_button)
        
        self.result_label = Label(text='', size_hint=(1, 0.2), color=(11, 11, 0, 1))
        self.add_widget(self.result_label)
    
    def balance_equation(self, instance):
        reactants = self.reactants_input.text.split('+')
        products = self.products_input.text.split('+')
        try:
            balanced_eq = balance_stoichiometry(set(reactants), set(products))
            result_text = " + ".join(f"{v} {k}" for k, v in balanced_eq[0].items()) + " -> " + " + ".join(f"{v} {k}" for k, v in balanced_eq[1].items())
            self.result_label.text = result_text
        except Exception as e:
            popup = Popup(title='Lỗi', content=Label(text=f'Không thể cân bằng phản ứng: {e}', color=(0, 0, 0, 1)), size_hint=(0.8, 0.4))
            popup.open()

class ChemicalReactionAppMain(App):
    def build(self):
        return ChemicalReactionApp()

if __name__ == '__main__':
    ChemicalReactionAppMain().run()
