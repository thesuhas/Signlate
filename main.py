import kivy
import cv2
from kivy.app import App
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.graphics.texture import Texture
from kivy.uix.image import Image
import time
import base64
import requests
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
import tensorflow as tf


# Loading model
model = tf.keras.models.load_model("C:/Users/suhas/Documents/College Projects/Signlate/model")
model.make_predict_function()

def predict(img, model):
	pred = model.predict(img)


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
		
		self.translate = Button(text="Translate", size_hint=(0.5, 0.75), pos_hint={"right": 1})
		self.translate.bind(on_press=self.pressed) # Binding Function to Button Press

		self.nextword = Button(text="Next Word", size_hint=(0.5, 0.75), pos_hint={"left": 1})
		self.nextword.bind(on_press=self.nxtword)

		self.inside.add_widget(self.translate)
		self.inside.add_widget(self.nextword)

		self.add_widget(self.inside)
		Clock.schedule_interval(self.update, 1.0/33.0) # Interval to update video stream at

	def update(self, dt):
		ret, frame = self.capture.read()
		buf1 = cv2.flip(frame, 0)
		buf2 = cv2.flip(buf1, 1)
		buf = buf2.tostring()
		self.img = frame
		texture1 = Texture.create(size = (frame.shape[1], frame.shape[0]), colorfmt='bgr')
		texture1.blit_buffer(buf, colorfmt="bgr", bufferfmt="ubyte")
		# texture1 = texture1.fliphorizontal()
		self.img1.texture = texture1

	def nxtword(self, instance):
		self.output.text = ""			


	def updatelabel(self, alphabet):
		if self.output.text == "Translation comes here":
			self.output.text = ""			

		self.output.text = self.output.text +" "+ alphabet

	def pressed(self, instance):
		# URL to send request to
		url = "https://signlate.herokuapp.com/test"
		content_type = 'image/jpeg'
		headers = {'content-type': content_type}
		
		# Request being sent
		#print(self.img)
		cv2.imwrite("test.jpg", self.img)
		img = cv2.imread("test.jpg")
		print(img)
		#_, img_encoded = cv2.imencode('.jpg', img)
		#res = requests.post(url, data=img_encoded.tostring(), headers=headers)
		#res = UrlRequest(url=url, on_success=self.print_res, on_failure=self.print_fail, method='POST', req_body=self.img.tostring(), req_headers=headers)
		#print(res)

		#returns the translation
		for letter in ['a', 'b', 'c', 'd']:
			self.updatelabel(letter)


	# Function that is called on success
	def print_res(self, req, res):
		print(res)

	# Function that is called on failure
	def print_fail(self, req, res):
		print("Request Failed", req, res)


class TestApp(App):

	def build(self):
		return Test()

if __name__ == '__main__':
    TestApp().run()
    cv2.destroyAllWindows()
