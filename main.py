from kivy.app import App
from random import randint
from kivy.uix.scatter import Scatter
from kivy.uix.label import Label
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.properties import ListProperty
from kivy.config import Config
#Config.set('graphics', 'width', '1920')
#Config.set('graphics', 'height', '1080')
#Config.set('graphics', 'fullscreen', 'fake')
Config.set('graphics', 'fullscreen', 'auto')
Config.set('modules', 'inspector', "")

class WordLabel(Scatter):
    my_string = StringProperty('')
    pressed = ListProperty([0,0])
    def __init__(self, text, **kw):
        super(WordLabel, self).__init__(**kw)
        self.my_string = text
        def on_touch_down(self, touch):
	    	if self.collide_point(*touch.pos):
	    		if touch.is_double_tap:
	    			self.pressed = touch.pos
	    			return True
	    	return super(WordLabel, self).on_touch_down(touch)
        def on_pressed(self, instance, pos):
            print ('pressed at {pos}'.format(pos=pos))

#the BoxLayout contains the FloatLayout and the TextInput
class Test(BoxLayout):
    #words to be removed from the input
    stopword_list = ['i', 'oh', 'an', 'now', 'the', 'that', 'to', 'as', 'there', 'has', 'and', 'or', 'is', 'not', 'a', 'of', 'but', 'in', 'by', 'on', 'are', 'it', 'if', 'I', ',', '.']
    f = ObjectProperty(None)
    #function triggered when pressing enter on the TextInput
    def GenerateLabel(self, command):
        #remove all the undesirable words from the user input
        new_list = [stopword for stopword in command.split() if stopword not in self.stopword_list]
        #for each word in the list, create a new Scatter+Label, and add them to the FloatLayout
        for word in new_list:
            self.f.add_widget(WordLabel(word))      
#build
class ExpeApp(App):
    def build(self):
        return Test()
#run
if __name__ == '__main__':
    ExpeApp().run()