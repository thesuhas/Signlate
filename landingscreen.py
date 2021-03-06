import kivy
import cv2
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
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
		self.orientation = 'vertical'
		self.img1 = Image(pos_hint={"top": 1}, size_hint=(1, 0.9))
		self.add_widget(self.img1)
		self.output = Label(text="Translation comes here", pos_hint={'bottom': 1}, size_hint=(1, 0.1))
		self.add_widget(self.output)

		# Inside
		self.inside = FloatLayout(size_hint=(1, 0.1))
		self.inside.cols = 2
		self.capture = cv2.VideoCapture(0) # Video Capture
		self.translate = Button(text="Translate", size_hint=(1, 1))
		self.translate.bind(on_press=self.pressed) # Binding Function to Button Press
		self.inside.add_widget(self.translate)
		self.add_widget(self.inside)
		Clock.schedule_interval(self.update, 1.0/33.0) # Interval to update video stream at

	def update(self, dt):
		ret, frame = self.capture.read()
		buf1 = cv2.flip(frame, 0)
		buf = buf1.tostring()
		texture1 = Texture.create(size = (frame.shape[1], frame.shape[0]), colorfmt='bgr')
		texture1.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
		self.img1.texture = texture1

	def pressed(self, instance):
		# URL to send request to
		url = "https://signlate.herokuapp.com/"
		# Request being sent
		req = UrlRequest(url=url, on_success=self.print_res, on_failure=self.print_fail)

	# Function that is called on success
	def print_res(self, req, res):
		print(res)

	# Function that is called on failure
	def print_fail(self, req, res):
		print("Request Failed")


class CamApp(App):

	def build(self):
		return Test()

if __name__ == '__main__':
    CamApp().run()
    cv2.destroyAllWindows()