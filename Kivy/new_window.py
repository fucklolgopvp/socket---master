# ! -*- coding:utf-8 -*-


from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.config import Config
from main import Server
from time import sleep

Config.set('graphics','resizable',0)
Config.set('graphics','width',600)
Config.set('graphics','height',900)


class FirstWind(Screen):
    pass

class ThrWind(Screen):
    pass

class SecondWind(Screen):
    def change_text(self):
        try:
            self.text_label.text = "Введіть інформацію в поля"
            arr = self.text_widget.text
            arr1 = self.text_widget2.text
            arr2 = self.text_widget3.text
            arr3 = self.text_widget4.text
            arr4 = self.text_widget5.text
            arr5 = self.text_widget6.text
            arrr = [arr,arr1,arr2,arr3,arr4,arr5]

            if "" in arrr:
                print("Don't have text in textEdit")
                self.text_label.text = "Заповніть всі поля"
                sleep(1.5)


                return None

            server.push_info(what_is=arr,place=arr1,data_time=arr2,person_name=arr3,phone=arr4,desc=arr5)
            self.text_label.text = "Інформація відправлена"
            print(arr,arr1,arr2,arr3,arr4,arr5)
            self.text_widget.text = ""
            self.text_widget2.text = ""
            self.text_widget3.text = ""
            self.text_widget4.text = ""
            self.text_widget5.text = ""
            self.text_widget6.text = ""



        except Exception as e:
            print(e)



class Wind(ScreenManager):
    pass


kv = Builder.load_file('new_window.kv')



class MyLayout(Widget):
    pass

class SearchApp(App):
    def build(self):
        return kv



if __name__=='__main__':
    server = Server()
    SearchApp().run()

  # Label:
  #           markup: True
  #           text: "        [color=#041413][size=35][b]Ви загубили [sup]речі[/sup] або [sub]знайшли??[/sub][/size][/color]\n    [size=48][u]Тоді ви попали по адресі!!![/size][/b][/u]"
  #           font_size: 40
  #           size_hint: .20, .20
  #           pos: 250,700
  #           color:(1,0,0,1)