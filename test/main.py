# import required modules
from kivymd.app import MDApp
from kivymd.uix.button import MDFloatingActionButton, MDFlatButton
from kivymd.uix.screen import Screen
from kivymd.icon_definitions import md_icons
from kivy.uix.label import Label

class DemoApp(MDApp):
    def build(self):
		
        # create screen object
        screen = Screen()

        # create buttons
        btn1 = MDFlatButton(text='Hello GFG', pos_hint={'center_x': 0.5, 
                                                        'center_y': 0.8})
        btn = MDFloatingActionButton(icon="android",
                                    pos_hint={'center_x': 0.5, 
                                            'center_y': 0.5},
                                    )
		
        lbl = Label(text ="Label is Added on screen !!:):)",
                    pos_hint={'center_x': 0.5, 
                            'center_y': 0.2},
                    color =(0.41, 0.42, 0.74, 1)
                    )

        # add buttons
        screen.add_widget(btn1)
        screen.add_widget(btn)
        screen.add_widget(lbl)
		
        return screen

	
# run application
DemoApp().run()
