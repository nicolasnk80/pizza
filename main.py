from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout


class Manager(ScreenManager):
	pass


class Main(Screen):
	pass


class Login(Screen):
	pass


class Pizzas(BoxLayout):
	pass


class Test(App):
	def build(self):
		return Manager()


Test().run()
