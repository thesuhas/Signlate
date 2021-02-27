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

class Test(BoxLayout):
	def __init__(self, **kwargs):
		super(Test, self).__init__(**kwargs)
		self.cols = 1
		self.img1 = Image()

		# Inside
		self.inside = BoxLayout()
		self.inside.cols = 1
		self.capture = cv2.VideoCapture(0)
		self.play = Button(text="Play")
		self.inside.add_widget(self.play)
		self.add_widget(self.inside)
		#cv2.namedWindow("CV2 Image")
		Clock.schedule_interval(self.update, 1.0/33.0)

		self.add_widget(self.img1)

	def update(self, dt):
		ret, frame = self.capture.read()
		#cv2.imshow("CV2 Image", frame)
		buf1 = cv2.flip(frame, 0)
		buf = buf1.tostring()
		texture1 = Texture.create(size = (frame.shape[1], frame.shape[0]), colorfmt='bgr')
		texture1.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
		self.img1.texture = texture1


class CamApp(App):

	def build(self):
		return Test()

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()