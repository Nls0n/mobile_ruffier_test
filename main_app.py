# напиши здесь свое приложение
from instructions import *
from ruffier import *
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
name = ''
age = 0
p1 = 0
p2 = 0
p3 = 0
blue = (0,255,255, 1)
yellow = (255,255,0,1)
Window.clearcolor = blue
def check(x):
    try:
        return int(x)
    except:
        return False
        
class Instr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        txt1='[color=#000000]'+'Введите имя'+'[/color]'
        label1=Label(text=txt1, markup=True, halign='right')
        self.in_name=TextInput(multiline=False)
        txt2='[color=#000000]'+'Введите возраст:'+'[/color]'
        label2=Label(text=txt2, markup=True, halign='right')
        self.in_age=TextInput(multiline=False)
        txt3='[color=#000000]'+'Начать'+'[/color]'
        self.btn = Button(text=txt3, markup=True, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = yellow
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(label1)
        line1.add_widget(self.in_name)
        line2.add_widget(label2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global name
        global age
        name = self.in_name.text
        age = check(self.in_age.text)
        if age == False or age <7:
            
            self.in_age.text='error'
        else:
            self.manager.current = 'pulse1'

#zxc        
class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test1)
        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        txt4='[color=#000000]'+'Введите результат'+'[/color]'
        label_result = Label(text=txt4, markup=True, halign='right')
        self.in_result = TextInput(text='0', multiline = False)
        line.add_widget(label_result)
        line.add_widget(self.in_result)
        txt5='[color=#000000]'+'Продолжить'+'[/color]'
        self.btn = Button(text=txt5, markup=True, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = yellow
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p1 
        p1  = check(self.in_result.text)
        if p1 == False or p1 <=0:
            
            self.in_result.text='error'
        else:
            self.manager.current = 'sits'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        txt6='[color=#000000]'+'Продолжить'+'[/color]'
        self.btn = Button(text=txt6, markup=True, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = yellow
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse2'
class PulseScr2(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        txt7='[color=#000000]'+'Результат:'+'[/color]'
        label_result1 = Label(text=txt7, markup=True, halign = 'right')
        self.in_result1 = TextInput(text='0', multiline = False)
        line1.add_widget(label_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        txt8='[color=#000000]'+'Результат после отдыха:'+'[/color]'
        label_result2 = Label(text=txt8, markup=True, halign = 'right')
        self.in_result2 = TextInput(text='0', multiline = False)
        line2.add_widget(label_result2)
        line2.add_widget(self.in_result2)
        txt9='[color=#000000]'+'Завершить'+'[/color]'
        self.btn = Button(text=txt9, markup=True, size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        self.btn.background_color = yellow
        outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p2, p3
        p2 = check(self.in_result1.text)
        p3 = check(self.in_result2.text)
        if (p2 == False or p2 <=0) or (p3 == False or p3 <=0) :
            self.in_result1.text='error'
            self.in_result2.text='error'
        else:
            self.manager.current = 'result'
class Result(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation = 'vertical', padding = 8, spacing = 8)
        self.instr = Label(text='')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1,p2,p3,age)

class MyApp(App):
  def build(self):
      sm = ScreenManager()
      sm.add_widget(Instr(name='main'))
      sm.add_widget(PulseScr(name='pulse1'))
      sm.add_widget(CheckSits(name='sits'))
      sm.add_widget(PulseScr2(name='pulse2'))
      sm.add_widget(Result(name='result'))
      return sm
#app = MyApp()
MyApp().run()
