
#pylint:disable= Duplicates found in MROs (MDNavigationDrawer), (MDCard, ThemableBehavior, BackgroundColorBehavior, RectangularElevationBehavior, CommonElevationBehavior, FocusBehavior, HoverBehavior, ButtonBehavior, BoxLayout, Layout, Widget, WidgetBase, WidgetBase, RectangularRippleBehavior, CommonRipple, object), (MDCard) for <ClassDef.MDNavigationDrawer l.359 at 0xabfc7210>.
import kivy
from kivy.metrics import dp
import kivymd
from kivy.uix.screenmanager import ScreenManager
from kivymd.uix.screen import MDScreen
from kivymd.app import MDApp
from kivy.uix.image import Image
from kivymd.uix.button import MDFillRoundFlatIconButton, MDFillRoundFlatButton
from kivymd.uix.textfield import MDTextField
from kivymd.uix.label import MDLabel
from kivymd.uix.toolbar import MDToolbar
from kivymd.uix.navigationdrawer import *
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.scrollview import ScrollView
from kivymd.uix.list import *
from kivy.uix.widget import Widget
from kivymd.uix.behaviors import  *					

class RectangularRippleButton(RectangularRippleBehavior,BackgroundColorBehavior  ):
	md_bg_color=(0,181.0/255.0,226.0/255.0,1)
	

class ConverterApp(MDApp):	


	def flip(self):
		self.converted.text = ""
		self.label.text = ""
		self.input.text = ""
		if self.state == 0 and self.topic == 0:
			self.state = 1
        	self.toolbar.title = "Decimal to Binary"
        	self.input.hint_text = "enter a decimal number"
        elif self.state == 1 and self.topic ==0:
        	self.state = 0
        	self.toolbar.title = "Binary to Decimal"
        	self.input.hint_text = "enter a binary number"
        elif self.state == 0 #ynd self.topic == 1:
	        self.state = 1
	        self.toolbar.title = "Decimal to Octal"
	        self.input.hint_text = "enter a decimal number"
	    elif self.state==1 and self.topic==1:
	    	self.state = 0
	        self.toolbar.title = "Octal to Decimal"
	        self.input.hint_text = "enter a octal number"
	 
        elif self.state == 0 and self.topic == 2:
            self.state = 1
            self.toolbar.title = "Decimal to Hexadecimal"
            self.input.hint_text = "enter a decimal number"
        elif self.state == 1 and self.topic == 2:
            self.state = 0
            self.toolbar.title = "Hexadecimal to Decimal"
            self.input.hint_text = "enter a hexadecimal number"
        elif self.state == 0 and self.topic == 3:
            self.state = 1
            self.toolbar.title = "Binary to Octal"
            self.input.hint_text = "enter a binary number"
        elif self.state == 1 and self.topic == 3:
            self.state = 0
            self.toolbar.title = "Octal to Binary"
            self.input.hint_text = "enter a octal number"
        elif self.state == 0 and self.topic == 4:
            self.state = 1
            self.toolbar.title = "Binary to Hexadecimal"
            self.input.hint_text = "enter a binary number" 
        elif self.state == 1 and self.topic == 4:
            self.state = 0
            self.toolbar.title = "Hexadecimal to Binary"
            self.input.hint_text = "enter a hexadecimal number"
        elif self.state == 0 and self.topic == 5:
            self.state = 1
            self.toolbar.title = "Octal to Hexadecimal"
            self.input.hint_text = "enter a octal number"
        else:
        	self.state = 0
        	self.toolbar.title = "Hexadecimal to Octal"
        	self.input.hint_text = "enter a hexadecimal number"
       
    def convert(self, args):
        # a method to find the decimal/binary equivallent
        try:
            if "." not in self.input.text:
                # if the user-provided number is not a fraction
                if self.state == 0:
                    # binary to decimal
                    val = str(int(self.input.text,2))
                    self.label.text = "in decimal is:"
                else:
                    # decimal to binary
                    val = bin(int(self.input.text))[2:]
                    self.label.text = "in binary is:"
                self.converted.text = val
            else:
                #if the user provided number is a fraction
                whole, fract = self.input.text.split(".")

                if self.state == 0:
                    #convert binary to decimal
                    whole = int(whole, 2)
                    floating = 0
                    for idx, digit in enumerate(fract):
                        floating += int(digit)*2**(-(idx+1))
                    self.label.text = "in decimal is:"
                    self.converted.text = str(whole + floating)
                else:
                    #convert decimal to binary
                    decimal_places = 10
                    whole = bin(int(whole))[2:]
                    fract = float("0."+fract)
                    floating = []
                    for i in range(decimal_places):
                        if fract*2 < 1:
                            floating.append("0")
                            fract *= 2
                        elif fract*2 > 1:
                            floating.append("1")
                            fract = fract*2 - 1
                        elif fract*2 == 1.0:
                            floating.append("1")
                            break
                    self.label.text = "in binary is:"
                    self.converted.text = whole + "." + "".join(floating)
        except ValueError:
            #if the user-provided value is invalid
            self.converted.text = ""
            if self.state == 0:
                #binary to decimal
                self.label.text = "please enter a valid binary number"

            else:
                #decimal to binary
                self.label.text = "please enter a valid decimal number"
    def item0_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 0
    	self.toolbar.title = 'Binary to Decimal'
    	self.input.hint_text = "enter a binary number"
    def item1_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 1
    	self.toolbar.title = "Octal to Decimal"
    	self.input.hint_text = "enter a octal number"
    def item2_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 2
    	self.toolbar.title = "Decimal to Hexadecimal"
    	self.input.hint_text = "enter a decimal number"
    def item3_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 3
    	self.toolbar.title = "Binary to Octal"
    	self.input.hint_text = "enter a binary number"
    def item4_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 4
    	self.toolbar.title = "Binary to Hexadecimal"
    	self.input.hint_text = "enter a binary number"
    def item5_func(self,*args):
    	self.nav_drawer.set_state('close')
    	self.nav_drawer.closing_time=0.2
    	self.topic = 5
    	self.toolbar.title = "Octal to Hexadecimal"
    	self.input.hint_text = "enter a octal number"
    
	def set_color_item(self,instance_item):
		for item in self.children:
			if item.text_color == self.theme_cls.primary_color:
				item.text_color==self.theme_cls.text_color
				break
		instance_item.text_color = self.theme_cls.primary_color
	    

    def build(self):
        self.state = 0 #initial state
        self.topic = 0
        self.theme_cls.primary_palette = "Blue"
  
        
        #navigation layout
        nav_layout=NavigationLayout()
        screen_manager=ScreenManager()
        nav_layout.add_widget(screen_manager)
        screen = MDScreen()
        screen_manager.add_widget(screen)        
        self.box_layout=MDBoxLayout(orientation='vertical')
        screen.add_widget(self.box_layout)
        
        # top toolbar
        self.toolbar = MDToolbar(title="Binary to Decimal")
        self.toolbar.pos_hint = {"top": 1}
        self.toolbar.right_action_items = [
            ["rotate-3d-variant", lambda x: self.flip()]]
        self.toolbar.left_action_items = [[ "menu", lambda x:self.nav_drawer.set_state()]]        
        self.box_layout.add_widget(self.toolbar)
        
        self.float_layout=MDFloatLayout()
        self.box_layout.add_widget(self.float_layout)
        
        self.nav_drawer = MDNavigationDrawer(
        opening_time=0.15,closing_time=0.2,close_on_click=True,swipe_distance=10,
        )
        nav_layout.add_widget(self.nav_drawer)
        
        #navigation layout widget
        nav_boxlayout=MDBoxLayout(
        orientation='vertical',spacing=0,padding=[0,0,0,int(dp(108))]
        )
        self.nav_drawer.add_widget(nav_boxlayout)
        nav_img=Image(source='logo.png')
        nav_boxlayout.add_widget(nav_img)
        
        list=MDList()
        nav_boxlayout.add_widget(list)
                     
        list_item0=OneLineIconListItem(on_release=self.item0_func,self.set_color_item,text='Binary To Decimal',divider=None, )      
        icon=IconLeftWidget(icon='cached')
        list_item0.add_widget(icon)
        list.add_widget(list_item0)        
        list_item1=OneLineIconListItem(on_release=self.item1_func,text='Octal To Decimal',divider=None, )      
        icon=IconLeftWidget(icon='cached')
        list_item1.add_widget(icon)
        list.add_widget(list_item1)          
      
        list_item3=OneLineIconListItem(on_release=self.item2_func,text='Decimal To Hexadecimal',divider=None, )
        icon=IconLeftWidget(icon='cached')
        list_item3.add_widget(icon)
        list.add_widget(list_item3)
        
        list_item5=OneLineIconListItem(on_release=self.item3_func,text='Binary To Octal',divider=None, )  
        icon=IconLeftWidget(icon='cached')
        list_item5.add_widget(icon)
        list.add_widget(list_item5)
    
        list_item7=OneLineIconListItem(on_release=self.item4_func,text='Binary To Hexadecimal',divider=None, )   
        icon=IconLeftWidget(icon='cached')
        list_item7.add_widget(icon)
        list.add_widget(list_item7)
    
        list_item9=OneLineIconListItem(on_release=self.item5_func,text='Octal To Hexadecimal',divider=None, )
        icon=IconLeftWidget(icon='cached')
        list_item9.add_widget(icon)    
        list.add_widget(list_item9)
    
        
        # logo
        self.float_layout.add_widget(Image(
            source="logo.png",
            pos_hint = {"center_x": 0.5, "center_y":0.7}
            ))

        #collect user input
        self.input = MDTextField(
            size_hint = (0.8,1),
            pos_hint = {"center_x": 0.5, "center_y":0.5},
            on_text_validate = self.convert
        )
        self.input.hint_text ="enter a binary number"
        self.float_layout.add_widget(self.input)

        #secondary + primary labels
        self.label = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.35},
            theme_text_color = "Secondary"
        )

        self.converted = MDLabel(
            halign="center",
            pos_hint = {"center_x": 0.5, "center_y":0.3},
            theme_text_color = "Primary",
            font_style = "H5"
        )
        self.float_layout.add_widget(self.label)
        self.float_layout.add_widget(self.converted)

        # "CONVERT" button
        self.float_layout.add_widget(MDFillRoundFlatButton(
            text="    CONVERT    ",
            font_size = 25,
            pos_hint = {"center_x": 0.5, "center_y":0.15},
            on_press = self.convert
        ))
        
        self.root = nav_layout
        

if __name__ == '__main__':
    ConverterApp().run()
