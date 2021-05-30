import kivy
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.config import Config
from kivy.uix.label import Label
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder

Config.set('graphics','resizable',0)
Config.set('graphics','width',600)
Config.set('graphics','height',900)



Builder.load_string("""
<MenuScreen>:
    BoxLayout:
        Button:
            text: 'Если нашол'
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current = 'settings'
        Button:
            text: 'В поиске'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'settings'

<SettingsScreen>:
    BoxLayout:
        Button:
            text: 'Вернуться в меню вибора'
            on_press:
                root.manager.transition.direction = 'right'
                root.manager.current = 'menu'
""")

class SearchApp(App):
    def build(self):
        g1 = BoxLayout(orientation = 'vertical')
        self.lbl2 = Label(text = "Привіт \nвибери один із пунктом \nкоторие тебя інтересуют", font_size = 50)


        bl = GridLayout(cols = 4,spacing = 3,padding = [35])
        #bl.add_widget(Button(text = 'Нажми', on_press = lambda x:set_screen('set2')))





        g1.add_widget(self.lbl2)
        #g1.add_widget(bl)
        g1.add_widget(sm)

        return g1


class MenuScreen(Screen):
    pass

class Setting(Screen):
    def __init__(self, **kw):
        super(Setting, self).__init__(**kw)
        bg = BoxLayout(orientation = 'vertical')
        bg2 = Label(text = 'TEXT')
        bg.add_widget(bg2)
        #return bg



class SettingsScreen(Screen):

    def __init__(self, **kw):
        super(SettingsScreen, self).__init__(**kw)
        box = BoxLayout(orientation='vertical',padding= [200])
        lb1 = Label(text = "Окно ")

        box.add_widget(lb1)

        self.add_widget(box)


def set_screen(name_screen):
    sm.current = name_screen

sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(Setting(name = 'set2'))

if __name__ == '__main__':
    SearchApp().run()
