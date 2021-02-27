import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class AditiApp(App):
	def build(self):
		return AditiGrid()
		
class AditiGrid(GridLayout):
	def __init__(self, **kwargs): #**as many keywords args
		
		super(AditiGrid, self).__init__(**kwargs)
		
		self.cols = 1
		
		self.inside = GridLayout()
		self.inside.cols = 2
		
		self.inside.add_widget(Label(text="Name: "))
		self.name = TextInput(multiline=False)
		self.inside.add_widget(self.name)
		
		self.inside.add_widget(Label(text="Age: "))
		self.age = TextInput(multiline=False)
		self.inside.add_widget(self.age)	
		
		self.inside.add_widget(Label(text="Date of Birth: "))
		self.dob = TextInput(multiline=False)
		self.inside.add_widget(self.dob)
		
		self.add_widget(self.inside)
		
		self.submit = Button(text="Submit here!", font_size=30)
		self.submit.bind(on_press=self.pressed)
		self.add_widget(self.submit)
		
	def pressed(self, instance):
		print("Button was pressed")
		name = self.name.text
		age = self.age.text
		dob = self.dob.text
		
		print("Name, Age, DOB", name, age, dob)
		self.name.text = ""
		self.age.text = ""
		
	
	
if __name__ == "__main__":
	AditiApp().run()
