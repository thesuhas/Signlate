import kivy
import cv2
from kivy.clock import Clock
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import time

from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout


class Signlate(App):
	def build(self):
		return CameraClick() #need to find a better way to do this

class CameraClick(FloatLayout):
	def capture(self):
		camera = self.ids['camera']
		timestr = time.strftime("%Y%m%d_%H%M%S")
		camera.export_to_png("cam_{}.png".format(timestr))
		print("Capturedddddd")

# class Controller(FloatLayout):
# 	def __init__(self, **kwargs):
# 		super(Controller, self).__init__(**kwargs)
# 		self.camera = Camera()
# 		self.add_widget(self.camera, )

# 	def generate(self):
# 		print("HELLO")


		
		
		
if __name__ == "__main__":
	Signlate().run()
