from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window





Kv = '''
MDFloatLayout:
    md_bg_color: "red" 
    MDLabel:
        text: "Do You Know How Much I Love You Blessing?"
        halign: "center"
        pos_hint: {'center_x': .5,'center_y': .75}
        font_size: "30dp"
        color: "white"
    
    MDLabel:
        id:hide
        text: "Click The Button Below To Know"
        font_size: "20px"
        halign: "center"
        color: "orange"

    MDLabel:
        id: result
        text: ""
        font_size: "80px"
        halign: "center"
        color: "orange"

    MDRectangleFlatButton:
        text: "Click To Find Out"
        pos_hint: {"center_x": .5, "center_y": .3}
        md_bg_color: "black"
        text_theme_color: "Custom"
        text_color: "orange"
        on_release : app.change(self)
''' 
Window.size = (400, 600)

class Bless(MDApp):
    def build(self):
        return Builder.load_string(Kv)

    def change(self, event):
        self.root.ids.result.text = "100%"
        self.root.ids.hide.text = ""
Bless().run()