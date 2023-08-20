from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.screenmanager import ScreenManager, Screen, NoTransition
from kivy.uix.image import Image
from kivy.uix.video import Video
from kivy.core.audio import SoundLoader
from kivy.utils import platform
from kivy.graphics import Rectangle
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button, ButtonBehavior
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.popup import Popup
from kivy.clock import Clock
import random

Builder.load_string('''
<TransparentButton@Button>:
    background_color: [0, 0, 0, 0]
    canvas.before:
        Color:
            rgba: [0, 0, 0, 0]
        RoundedRectangle:
            pos: self.pos
            size: self.size
''')

class LoadingScreen(Screen):
	def on_enter(self):
		self.image = Image(source='data/homeloading.gif', anim_delay=1 / 20, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.image)
		Clock.schedule_once(self.load_main_content, 11)

	def load_main_content(self, dt):
		self.manager.current = 'list'

	def on_leave(self, *args):
		self.remove_widget(self.image)
		super(LoadingScreen, self).on_leave(*args)
	pass
	
class SignTopiaManager(ScreenManager):
	def __init__(self, *args, **kwargs):
		super(SignTopiaManager, self).__init__(*args, **kwargs)
		self.add_widget(LoadingScreen())
		self.transition = NoTransition(duration=.5)

	def start_list(self):
		if self.has_screen('list'):
			self.remove_widget(self.get_screen('list'))
		self.add_widget(ListScreen())
		self.current = 'list'

	def start_main(self):
		if self.has_screen('main'):
			self.remove_widget(self.get_screen('main'))
		self.add_widget(MainScreen())
		self.current = 'main'

	def start_deaf(self):
		if self.has_screen('deaf'):
			self.remove_widget(self.get_screen('deaf'))
		self.add_widget(DeafScreen())
		self.current = 'deaf'
	
	def start_nondeaf(self):
		if self.has_screen('nondeaf'):
			self.remove_widget(self.get_screen('nondeaf'))
		self.add_widget(NonDeafScreen())	
		self.current = 'nondeaf'

	def start_deaflessons(self):
		if self.has_screen('deaflessons'):
			self.remove_widget(self.get_screen('deaflessons'))
		self.add_widget(DeafLessonsScreen())	
		self.current = 'deaflessons'

	def start_nondeaflessons(self):
		if self.has_screen('nondeaflessons'):
			self.remove_widget(self.get_screen('nondeaflessons'))
		self.add_widget(NonDeafLessonsScreen())	
		self.current = 'nondeaflessons'

	def start_deafassessments(self):
		if self.has_screen('deafassessments'):
			self.remove_widget(self.get_screen('deafassessments'))
		self.add_widget(DeafAssessmentsScreen())	
		self.current = 'deafassessments'

	def start_deafassessments2(self):
		if self.has_screen('deafassessments2'):
			self.remove_widget(self.get_screen('deafassessments2'))
		self.add_widget(DeafAssessmentsScreen2())	
		self.current = 'deafassessments2'

	def start_nondeafassessments(self):
		if self.has_screen('nondeafassessments'):
			self.remove_widget(self.get_screen('nondeafassessments'))
		self.add_widget(NonDeafAssessmentsScreen())	
		self.current = 'nondeafassessments'

	def start_nondeafassessments2(self):
		if self.has_screen('nondeafassessments2'):
			self.remove_widget(self.get_screen('nondeafassessments2'))
		self.add_widget(NonDeafAssessmentsScreen2())	
		self.current = 'nondeafassessments2'

	def start_deafnoloading(self):
		if self.has_screen('deafnoloading'):
			self.remove_widget(self.get_screen('deafnoloading'))
		self.add_widget(DeafNoLoadingScreen())
		self.current = 'deafnoloading'	

	def start_deafnolesson1(self):
		if self.has_screen('deafnolesson1'):
			self.remove_widget(self.get_screen('deafnolesson1'))
		self.add_widget(DeafNumberLessonScreen1())
		self.current = 'deafnolesson1'

	def start_deafnolesson2(self):
		if self.has_screen('deafnolesson2'):
			self.remove_widget(self.get_screen('deafnolesson2'))
		self.add_widget(DeafNumberLessonScreen2())
		self.current = 'deafnolesson2'

	def start_deafnolesson3(self):
		if self.has_screen('deafnolesson3'):
			self.remove_widget(self.get_screen('deafnolesson3'))
		self.add_widget(DeafNumberLessonScreen3())
		self.current = 'deafnolesson3'

	def start_deafnolesson4(self):
		if self.has_screen('deafnolesson4'):
			self.remove_widget(self.get_screen('deafnolesson4'))
		self.add_widget(DeafNumberLessonScreen4())
		self.current = 'deafnolesson4'
	
	def start_deafnolesson5(self):
		if self.has_screen('deafnolesson5'):
			self.remove_widget(self.get_screen('deafnolesson5'))
		self.add_widget(DeafNumberLessonScreen5())
		self.current = 'deafnolesson5'

	def start_deafnolesson6(self):
		if self.has_screen('deafnolesson6'):
			self.remove_widget(self.get_screen('deafnolesson6'))
		self.add_widget(DeafNumberLessonScreen6())
		self.current = 'deafnolesson6'

	def start_deafnolesson7(self):
		if self.has_screen('deafnolesson7'):
			self.remove_widget(self.get_screen('deafnolesson7'))
		self.add_widget(DeafNumberLessonScreen7())
		self.current = 'deafnolesson7'

	def start_deafnolesson8(self):
		if self.has_screen('deafnolesson8'):
			self.remove_widget(self.get_screen('deafnolesson8'))
		self.add_widget(DeafNumberLessonScreen8())
		self.current = 'deafnolesson8'
	
	def start_deafnolesson9(self):
		if self.has_screen('deafnolesson9'):
			self.remove_widget(self.get_screen('deafnolesson9'))
		self.add_widget(DeafNumberLessonScreen9())
		self.current = 'deafnolesson9'

	def start_deafnolesson10(self):
		if self.has_screen('deafnolesson10'):
			self.remove_widget(self.get_screen('deafnolesson10'))
		self.add_widget(DeafNumberLessonScreen10())
		self.current = 'deafnolesson10'
			
	def start_deafnoloadingas(self):
		if self.has_screen('deafnoloadingas'):
			self.remove_widget(self.get_screen('deafnoloadingas'))
		self.add_widget(DeafNoLoadingAsScreen())
		self.current = 'deafnoloadingas'

	def start_deafnoassessment(self):
		if self.has_screen('deafnoassessment'):
			self.remove_widget(self.get_screen('deafnoassessment'))
		self.add_widget(DeafNumberAssessmentScreen())
		self.current = 'deafnoassessment'

	def start_nondeafnoloading(self):
		if self.has_screen('nondeafnoloading'):
			self.remove_widget(self.get_screen('nondeafnoloading'))
		self.add_widget(NonDeafNoLoadingScreen())
		self.current = 'nondeafnoloading'	

	def start_nondeafnolesson1(self):
		if self.has_screen('nondeafnolesson1'):
			self.remove_widget(self.get_screen('nondeafnolesson1'))
		self.add_widget(NonDeafNumberLessonScreen1())
		self.current = 'nondeafnolesson1'

	def start_nondeafnolesson2(self):
		if self.has_screen('nondeafnolesson2'):
			self.remove_widget(self.get_screen('nondeafnolesson2'))
		self.add_widget(NonDeafNumberLessonScreen2())
		self.current = 'nondeafnolesson2'

	def start_nondeafnolesson3(self):
		if self.has_screen('nondeafnolesson3'):
			self.remove_widget(self.get_screen('nondeafnolesson3'))
		self.add_widget(NonDeafNumberLessonScreen3())
		self.current = 'nondeafnolesson3'

	def start_nondeafnolesson4(self):
		if self.has_screen('nondeafnolesson4'):
			self.remove_widget(self.get_screen('nondeafnolesson4'))
		self.add_widget(NonDeafNumberLessonScreen4())
		self.current = 'nondeafnolesson4'
	
	def start_nondeafnolesson5(self):
		if self.has_screen('nondeafnolesson5'):
			self.remove_widget(self.get_screen('nondeafnolesson5'))
		self.add_widget(NonDeafNumberLessonScreen5())
		self.current = 'nondeafnolesson5'

	def start_nondeafnolesson6(self):
		if self.has_screen('nondeafnolesson6'):
			self.remove_widget(self.get_screen('nondeafnolesson6'))
		self.add_widget(NonDeafNumberLessonScreen6())
		self.current = 'nondeafnolesson6'

	def start_nondeafnolesson7(self):
		if self.has_screen('nondeafnolesson7'):
			self.remove_widget(self.get_screen('nondeafnolesson7'))
		self.add_widget(NonDeafNumberLessonScreen7())
		self.current = 'nondeafnolesson7'

	def start_nondeafnolesson8(self):
		if self.has_screen('nondeafnolesson8'):
			self.remove_widget(self.get_screen('nondeafnolesson8'))
		self.add_widget(NonDeafNumberLessonScreen8())
		self.current = 'nondeafnolesson8'
	
	def start_nondeafnolesson9(self):
		if self.has_screen('nondeafnolesson9'):
			self.remove_widget(self.get_screen('nondeafnolesson9'))
		self.add_widget(NonDeafNumberLessonScreen9())
		self.current = 'nondeafnolesson9'

	def start_nondeafnolesson10(self):
		if self.has_screen('nondeafnolesson10'):
			self.remove_widget(self.get_screen('nondeafnolesson10'))
		self.add_widget(NonDeafNumberLessonScreen10())
		self.current = 'nondeafnolesson10'
		
	def start_nondeafnoloadingas(self):
		if self.has_screen('nondeafnoloadingas'):
			self.remove_widget(self.get_screen('nondeafnoloadingas'))
		self.add_widget(NonDeafNoLoadingAsScreen())
		self.current = 'nondeafnoloadingas'

	def start_nondeafnoassessment(self):
		if self.has_screen('nondeafnoassessment'):
			self.remove_widget(self.get_screen('nondeafnoassessment'))
		self.add_widget(NonDeafNumberAssessmentScreen())
		self.current = 'nondeafnoassessment'

	def start_deafalloading(self):
		if self.has_screen('deafalloading'):
			self.remove_widget(self.get_screen('deafalloading'))
		self.add_widget(DeafAlLoadingScreen())
		self.current = 'deafalloading'	

	def start_deafallesson1(self):
		if self.has_screen('deafallesson1'):
			self.remove_widget(self.get_screen('deafallesson1'))
		self.add_widget(DeafAlLessonScreen1())
		self.current = 'deafallesson1'	

	def start_deafallesson2(self):
		if self.has_screen('deafallesson2'):
			self.remove_widget(self.get_screen('deafallesson2'))
		self.add_widget(DeafAlLessonScreen2())
		self.current = 'deafallesson2'	

	def start_deafallesson3(self):
		if self.has_screen('deafallesson3'):
			self.remove_widget(self.get_screen('deafallesson3'))
		self.add_widget(DeafAlLessonScreen3())
		self.current = 'deafallesson3'	

	def start_deafallesson4(self):
		if self.has_screen('deafallesson4'):
			self.remove_widget(self.get_screen('deafallesson4'))
		self.add_widget(DeafAlLessonScreen4())
		self.current = 'deafallesson4'	

	def start_deafallesson5(self):
		if self.has_screen('deafallesson5'):
			self.remove_widget(self.get_screen('deafallesson5'))
		self.add_widget(DeafAlLessonScreen5())
		self.current = 'deafallesson5'	

	def start_deafallesson6(self):
		if self.has_screen('deafallesson6'):
			self.remove_widget(self.get_screen('deafallesson6'))
		self.add_widget(DeafAlLessonScreen6())
		self.current = 'deafallesson6'	

	def start_deafallesson7(self):
		if self.has_screen('deafallesson7'):
			self.remove_widget(self.get_screen('deafallesson7'))
		self.add_widget(DeafAlLessonScreen7())
		self.current = 'deafallesson7'	

	def start_deafallesson8(self):
		if self.has_screen('deafallesson8'):
			self.remove_widget(self.get_screen('deafallesson8'))
		self.add_widget(DeafAlLessonScreen8())
		self.current = 'deafallesson8'	

	def start_deafallesson9(self):
		if self.has_screen('deafallesson9'):
			self.remove_widget(self.get_screen('deafallesson9'))
		self.add_widget(DeafAlLessonScreen9())
		self.current = 'deafallesson9'	

	def start_deafallesson10(self):
		if self.has_screen('deafallesson10'):
			self.remove_widget(self.get_screen('deafallesson10'))
		self.add_widget(DeafAlLessonScreen10())
		self.current = 'deafallesson10'	

	def start_deafallesson11(self):
		if self.has_screen('deafallesson11'):
			self.remove_widget(self.get_screen('deafallesson11'))
		self.add_widget(DeafAlLessonScreen11())
		self.current = 'deafallesson11'	

	def start_deafallesson12(self):
		if self.has_screen('deafallesson12'):
			self.remove_widget(self.get_screen('deafallesson12'))
		self.add_widget(DeafAlLessonScreen12())
		self.current = 'deafallesson12'	

	def start_deafallesson13(self):
		if self.has_screen('deafallesson13'):
			self.remove_widget(self.get_screen('deafallesson13'))
		self.add_widget(DeafAlLessonScreen13())
		self.current = 'deafallesson13'	

	def start_deafallesson14(self):
		if self.has_screen('deafallesson14'):
			self.remove_widget(self.get_screen('deafallesson14'))
		self.add_widget(DeafAlLessonScreen14())
		self.current = 'deafallesson14'	

	def start_deafallesson15(self):
		if self.has_screen('deafallesson15'):
			self.remove_widget(self.get_screen('deafallesson15'))
		self.add_widget(DeafAlLessonScreen15())
		self.current = 'deafallesson15'	

	def start_deafallesson16(self):
		if self.has_screen('deafallesson16'):
			self.remove_widget(self.get_screen('deafallesson16'))
		self.add_widget(DeafAlLessonScreen16())
		self.current = 'deafallesson16'	

	def start_deafallesson17(self):
		if self.has_screen('deafallesson17'):
			self.remove_widget(self.get_screen('deafallesson17'))
		self.add_widget(DeafAlLessonScreen17())
		self.current = 'deafallesson17'	

	def start_deafallesson18(self):
		if self.has_screen('deafallesson18'):
			self.remove_widget(self.get_screen('deafallesson18'))
		self.add_widget(DeafAlLessonScreen18())
		self.current = 'deafallesson18'	

	def start_deafallesson19(self):
		if self.has_screen('deafallesson19'):
			self.remove_widget(self.get_screen('deafallesson19'))
		self.add_widget(DeafAlLessonScreen19())
		self.current = 'deafallesson19'	

	def start_deafallesson20(self):
		if self.has_screen('deafallesson20'):
			self.remove_widget(self.get_screen('deafallesson20'))
		self.add_widget(DeafAlLessonScreen20())
		self.current = 'deafallesson20'	

	def start_deafallesson21(self):
		if self.has_screen('deafallesson21'):
			self.remove_widget(self.get_screen('deafallesson21'))
		self.add_widget(DeafAlLessonScreen21())
		self.current = 'deafallesson21'	

	def start_deafallesson22(self):
		if self.has_screen('deafallesson22'):
			self.remove_widget(self.get_screen('deafallesson22'))
		self.add_widget(DeafAlLessonScreen22())
		self.current = 'deafallesson22'	

	def start_deafallesson23(self):
		if self.has_screen('deafallesson23'):
			self.remove_widget(self.get_screen('deafallesson23'))
		self.add_widget(DeafAlLessonScreen23())
		self.current = 'deafallesson23'	

	def start_deafallesson24(self):
		if self.has_screen('deafallesson24'):
			self.remove_widget(self.get_screen('deafallesson24'))
		self.add_widget(DeafAlLessonScreen24())
		self.current = 'deafallesson24'	

	def start_deafallesson25(self):
		if self.has_screen('deafallesson25'):
			self.remove_widget(self.get_screen('deafallesson25'))
		self.add_widget(DeafAlLessonScreen25())
		self.current = 'deafallesson25'	

	def start_deafallesson26(self):
		if self.has_screen('deafallesson26'):
			self.remove_widget(self.get_screen('deafallesson26'))
		self.add_widget(DeafAlLessonScreen26())
		self.current = 'deafallesson26'	

	def start_deafalloadingas(self):
		if self.has_screen('deafalloadingas'):
			self.remove_widget(self.get_screen('deafalloadingas'))
		self.add_widget(DeafAlLoadingAsScreen())
		self.current = 'deafalloadingas'	

	def start_deafalassessment(self):
		if self.has_screen('deafalassessment'):
			self.remove_widget(self.get_screen('deafalassessment'))
		self.add_widget(DeafAlphabetAssessmentScreen())
		self.current = 'deafalassessment'

	def start_nondeafalloading(self):
		if self.has_screen('nondeafalloading'):
			self.remove_widget(self.get_screen('nondeafalloading'))
		self.add_widget(NonDeafAlLoadingScreen())
		self.current = 'nondeafalloading'	

	def start_nondeafallesson1(self):
		if self.has_screen('nondeafallesson1'):
			self.remove_widget(self.get_screen('nondeafallesson1'))
		self.add_widget(NonDeafAlLessonScreen1())
		self.current = 'nondeafallesson1'	

	def start_nondeafallesson2(self):
		if self.has_screen('nondeafallesson2'):
			self.remove_widget(self.get_screen('nondeafallesson2'))
		self.add_widget(NonDeafAlLessonScreen2())
		self.current = 'nondeafallesson2'	

	def start_nondeafallesson3(self):
		if self.has_screen('nondeafallesson3'):
			self.remove_widget(self.get_screen('nondeafallesson3'))
		self.add_widget(NonDeafAlLessonScreen3())
		self.current = 'nondeafallesson3'	

	def start_nondeafallesson4(self):
		if self.has_screen('nondeafallesson4'):
			self.remove_widget(self.get_screen('nondeafallesson4'))
		self.add_widget(NonDeafAlLessonScreen4())
		self.current = 'nondeafallesson4'	

	def start_nondeafallesson5(self):
		if self.has_screen('nondeafallesson5'):
			self.remove_widget(self.get_screen('nondeafallesson5'))
		self.add_widget(NonDeafAlLessonScreen5())
		self.current = 'nondeafallesson5'	

	def start_nondeafallesson6(self):
		if self.has_screen('nondeafallesson6'):
			self.remove_widget(self.get_screen('nondeafallesson6'))
		self.add_widget(NonDeafAlLessonScreen6())
		self.current = 'nondeafallesson6'	

	def start_nondeafallesson7(self):
		if self.has_screen('nondeafallesson7'):
			self.remove_widget(self.get_screen('nondeafallesson7'))
		self.add_widget(NonDeafAlLessonScreen7())
		self.current = 'nondeafallesson7'	

	def start_nondeafallesson8(self):
		if self.has_screen('nondeafallesson8'):
			self.remove_widget(self.get_screen('nondeafallesson8'))
		self.add_widget(NonDeafAlLessonScreen8())
		self.current = 'nondeafallesson8'	

	def start_nondeafallesson9(self):
		if self.has_screen('nondeafallesson9'):
			self.remove_widget(self.get_screen('nondeafallesson9'))
		self.add_widget(NonDeafAlLessonScreen9())
		self.current = 'nondeafallesson9'	

	def start_nondeafallesson10(self):
		if self.has_screen('nondeafallesson10'):
			self.remove_widget(self.get_screen('nondeafallesson10'))
		self.add_widget(NonDeafAlLessonScreen10())
		self.current = 'nondeafallesson10'	

	def start_nondeafallesson11(self):
		if self.has_screen('nondeafallesson11'):
			self.remove_widget(self.get_screen('nondeafallesson11'))
		self.add_widget(NonDeafAlLessonScreen11())
		self.current = 'nondeafallesson11'	

	def start_nondeafallesson12(self):
		if self.has_screen('nondeafallesson12'):
			self.remove_widget(self.get_screen('nondeafallesson12'))
		self.add_widget(NonDeafAlLessonScreen12())
		self.current = 'nondeafallesson12'	

	def start_nondeafallesson13(self):
		if self.has_screen('nondeafallesson13'):
			self.remove_widget(self.get_screen('nondeafallesson13'))
		self.add_widget(NonDeafAlLessonScreen13())
		self.current = 'nondeafallesson13'	

	def start_nondeafallesson14(self):
		if self.has_screen('nondeafallesson14'):
			self.remove_widget(self.get_screen('nondeafallesson14'))
		self.add_widget(NonDeafAlLessonScreen14())
		self.current = 'nondeafallesson14'	

	def start_nondeafallesson15(self):
		if self.has_screen('nondeafallesson15'):
			self.remove_widget(self.get_screen('nondeafallesson15'))
		self.add_widget(NonDeafAlLessonScreen15())
		self.current = 'nondeafallesson15'	

	def start_nondeafallesson16(self):
		if self.has_screen('nondeafallesson16'):
			self.remove_widget(self.get_screen('nondeafallesson16'))
		self.add_widget(NonDeafAlLessonScreen16())
		self.current = 'nondeafallesson16'	

	def start_nondeafallesson17(self):
		if self.has_screen('nondeafallesson17'):
			self.remove_widget(self.get_screen('nondeafallesson17'))
		self.add_widget(NonDeafAlLessonScreen17())
		self.current = 'nondeafallesson17'	

	def start_nondeafallesson18(self):
		if self.has_screen('nondeafallesson18'):
			self.remove_widget(self.get_screen('nondeafallesson18'))
		self.add_widget(NonDeafAlLessonScreen18())
		self.current = 'nondeafallesson18'	

	def start_nondeafallesson19(self):
		if self.has_screen('nondeafallesson19'):
			self.remove_widget(self.get_screen('nondeafallesson19'))
		self.add_widget(NonDeafAlLessonScreen19())
		self.current = 'nondeafallesson19'	

	def start_nondeafallesson20(self):
		if self.has_screen('nondeafallesson20'):
			self.remove_widget(self.get_screen('nondeafallesson20'))
		self.add_widget(NonDeafAlLessonScreen20())
		self.current = 'nondeafallesson20'	

	def start_nondeafallesson21(self):
		if self.has_screen('nondeafallesson21'):
			self.remove_widget(self.get_screen('nondeafallesson21'))
		self.add_widget(NonDeafAlLessonScreen21())
		self.current = 'nondeafallesson21'	

	def start_nondeafallesson22(self):
		if self.has_screen('nondeafallesson22'):
			self.remove_widget(self.get_screen('nondeafallesson22'))
		self.add_widget(NonDeafAlLessonScreen22())
		self.current = 'nondeafallesson22'	

	def start_nondeafallesson23(self):
		if self.has_screen('nondeafallesson23'):
			self.remove_widget(self.get_screen('nondeafallesson23'))
		self.add_widget(NonDeafAlLessonScreen23())
		self.current = 'nondeafallesson23'	

	def start_nondeafallesson24(self):
		if self.has_screen('nondeafallesson24'):
			self.remove_widget(self.get_screen('nondeafallesson24'))
		self.add_widget(NonDeafAlLessonScreen24())
		self.current = 'nondeafallesson24'	

	def start_nondeafallesson25(self):
		if self.has_screen('nondeafallesson25'):
			self.remove_widget(self.get_screen('nondeafallesson25'))
		self.add_widget(NonDeafAlLessonScreen25())
		self.current = 'nondeafallesson25'	

	def start_nondeafallesson26(self):
		if self.has_screen('nondeafallesson26'):
			self.remove_widget(self.get_screen('nondeafallesson26'))
		self.add_widget(NonDeafAlLessonScreen26())
		self.current = 'nondeafallesson26'

	def start_nondeafalloadingas(self):
		if self.has_screen('nondeafalloadingas'):
			self.remove_widget(self.get_screen('nondeafalloadingas'))
		self.add_widget(NonDeafAlLoadingAsScreen())
		self.current = 'nondeafalloadingas'	

	def start_nondeafalassessment(self):
		if self.has_screen('nondeafalassessment'):
			self.remove_widget(self.get_screen('nondeafalassessment'))
		self.add_widget(NonDeafAlphabetAssessmentScreen())
		self.current = 'nondeafalassessment'	

	def start_deafwoloading(self):
		if self.has_screen('deafwoloading'):
			self.remove_widget(self.get_screen('deafwoloading'))
		self.add_widget(DeafWoLoadingScreen())
		self.current = 'deafwoloading'

	def start_deafwolesson1(self):
		if self.has_screen('deafwolesson1'):
			self.remove_widget(self.get_screen('deafwolesson1'))
		self.add_widget(DeafWordLessonScreen1())
		self.current = 'deafwolesson1'

	def start_deafwolesson2(self):
		if self.has_screen('deafwolesson2'):
			self.remove_widget(self.get_screen('deafwolesson2'))
		self.add_widget(DeafWordLessonScreen2())
		self.current = 'deafwolesson2'

	def start_deafwolesson3(self):
		if self.has_screen('deafwolesson3'):
			self.remove_widget(self.get_screen('deafwolesson3'))
		self.add_widget(DeafWordLessonScreen3())
		self.current = 'deafwolesson3'

	def start_deafwolesson4(self):
		if self.has_screen('deafwolesson4'):
			self.remove_widget(self.get_screen('deafwolesson4'))
		self.add_widget(DeafWordLessonScreen4())
		self.current = 'deafwolesson4'
	
	def start_deafwolesson5(self):
		if self.has_screen('deafwolesson5'):
			self.remove_widget(self.get_screen('deafwolesson5'))
		self.add_widget(DeafWordLessonScreen5())
		self.current = 'deafwolesson5'

	def start_deafwolesson6(self):
		if self.has_screen('deafwolesson6'):
			self.remove_widget(self.get_screen('deafwolesson6'))
		self.add_widget(DeafWordLessonScreen6())
		self.current = 'deafwolesson6'

	def start_deafwolesson7(self):
		if self.has_screen('deafwolesson7'):
			self.remove_widget(self.get_screen('deafwolesson7'))
		self.add_widget(DeafWordLessonScreen7())
		self.current = 'deafwolesson7'

	def start_deafwolesson8(self):
		if self.has_screen('deafwolesson8'):
			self.remove_widget(self.get_screen('deafwolesson8'))
		self.add_widget(DeafWordLessonScreen8())
		self.current = 'deafwolesson8'
	
	def start_deafwolesson9(self):
		if self.has_screen('deafwolesson9'):
			self.remove_widget(self.get_screen('deafwolesson9'))
		self.add_widget(DeafWordLessonScreen9())
		self.current = 'deafwolesson9'

	def start_deafwolesson10(self):
		if self.has_screen('deafwolesson10'):
			self.remove_widget(self.get_screen('deafwolesson10'))
		self.add_widget(DeafWordLessonScreen10())
		self.current = 'deafwolesson10'
		
	def start_deafwoloadingas(self):
		if self.has_screen('deafwoloadingas'):
			self.remove_widget(self.get_screen('deafwoloadingas'))
		self.add_widget(DeafWoLoadingAsScreen())
		self.current = 'deafwoloadingas'

	def start_deafwoassessment(self):
		if self.has_screen('deafwoassessment'):
			self.remove_widget(self.get_screen('deafwoassessment'))
		self.add_widget(DeafWordAssessmentScreen())
		self.current = 'deafwoassessment'

	def start_nondeafwoloading(self):
		if self.has_screen('nondeafwoloading'):
			self.remove_widget(self.get_screen('nondeafwoloading'))
		self.add_widget(NonDeafWoLoadingScreen())
		self.current = 'nondeafwoloading'

	def start_nondeafwolesson1(self):
		if self.has_screen('nondeafwolesson1'):
			self.remove_widget(self.get_screen('nondeafwolesson1'))
		self.add_widget(NonDeafWordLessonScreen1())
		self.current = 'nondeafwolesson1'

	def start_nondeafwolesson2(self):
		if self.has_screen('nondeafwolesson2'):
			self.remove_widget(self.get_screen('nondeafwolesson2'))
		self.add_widget(NonDeafWordLessonScreen2())
		self.current = 'nondeafwolesson2'

	def start_nondeafwolesson3(self):
		if self.has_screen('nondeafwolesson3'):
			self.remove_widget(self.get_screen('nondeafwolesson3'))
		self.add_widget(NonDeafWordLessonScreen3())
		self.current = 'nondeafwolesson3'

	def start_nondeafwolesson4(self):
		if self.has_screen('nondeafwolesson4'):
			self.remove_widget(self.get_screen('nondeafwolesson4'))
		self.add_widget(NonDeafWordLessonScreen4())
		self.current = 'nondeafwolesson4'
	
	def start_nondeafwolesson5(self):
		if self.has_screen('nondeafwolesson5'):
			self.remove_widget(self.get_screen('nondeafwolesson5'))
		self.add_widget(NonDeafWordLessonScreen5())
		self.current = 'nondeafwolesson5'

	def start_nondeafwolesson6(self):
		if self.has_screen('nondeafwolesson6'):
			self.remove_widget(self.get_screen('nondeafwolesson6'))
		self.add_widget(NonDeafWordLessonScreen6())
		self.current = 'nondeafwolesson6'

	def start_nondeafwolesson7(self):
		if self.has_screen('nondeafwolesson7'):
			self.remove_widget(self.get_screen('nondeafwolesson7'))
		self.add_widget(NonDeafWordLessonScreen7())
		self.current = 'nondeafwolesson7'

	def start_nondeafwolesson8(self):
		if self.has_screen('nondeafwolesson8'):
			self.remove_widget(self.get_screen('nondeafwolesson8'))
		self.add_widget(NonDeafWordLessonScreen8())
		self.current = 'nondeafwolesson8'
	
	def start_nondeafwolesson9(self):
		if self.has_screen('nondeafwolesson9'):
			self.remove_widget(self.get_screen('nondeafwolesson9'))
		self.add_widget(NonDeafWordLessonScreen9())
		self.current = 'nondeafwolesson9'

	def start_nondeafwolesson10(self):
		if self.has_screen('nondeafwolesson10'):
			self.remove_widget(self.get_screen('nondeafwolesson10'))
		self.add_widget(NonDeafWordLessonScreen10())
		self.current = 'nondeafwolesson10'
		
	def start_nondeafwoloadingas(self):
		if self.has_screen('nondeafwoloadingas'):
			self.remove_widget(self.get_screen('nondeafwoloadingas'))
		self.add_widget(NonDeafWoLoadingAsScreen())
		self.current = 'nondeafwoloadingas'

	def start_nondeafwoassessment(self):
		if self.has_screen('nondeafwoassessment'):
			self.remove_widget(self.get_screen('nondeafwoassessment'))
		self.add_widget(NonDeafWordAssessmentScreen())
		self.current = 'nondeafwoassessment'

	def start_deafseloading(self):
		if self.has_screen('deafseloading'):
			self.remove_widget(self.get_screen('deafseloading'))
		self.add_widget(DeafSeLoadingScreen())
		self.current = 'deafseloading'

	def start_deafselesson1(self):
		if self.has_screen('deafselesson1'):
			self.remove_widget(self.get_screen('deafselesson1'))
		self.add_widget(DeafSentenceLessonScreen1())
		self.current = 'deafselesson1'

	def start_deafseloadingas(self):
		if self.has_screen('deafseloadingas'):
			self.remove_widget(self.get_screen('deafseloadingas'))
		self.add_widget(DeafSeLoadingAsScreen())
		self.current = 'deafseloadingas'

	def start_deafseassessment(self):
		if self.has_screen('deafseassessment'):
			self.remove_widget(self.get_screen('deafseassessment'))
		self.add_widget(DeafSentenceAssessmentScreen())
		self.current = 'deafseassessment'

	def start_nondeafseloading(self):
		if self.has_screen('nondeafseloading'):
			self.remove_widget(self.get_screen('nondeafseloading'))
		self.add_widget(NonDeafSeLoadingScreen())
		self.current = 'nondeafseloading'

	def start_nondeafselesson1(self):
		if self.has_screen('nondeafselesson1'):
			self.remove_widget(self.get_screen('nondeafselesson1'))
		self.add_widget(NonDeafSentenceLessonScreen1())
		self.current = 'nondeafselesson1'

	def start_nondeafseloadingas(self):
		if self.has_screen('nondeafseloadingas'):
			self.remove_widget(self.get_screen('nondeafseloadingas'))
		self.add_widget(NonDeafSeLoadingAsScreen())
		self.current = 'nondeafseloadingas'

	def start_nondeafseassessment(self):
		if self.has_screen('nondeafseassessment'):
			self.remove_widget(self.get_screen('nondeafseassessment'))
		self.add_widget(NonDeafSentenceAssessmentScreen())
		self.current = 'nondeafseassessment'

class TransparentButton(ButtonBehavior, Image):
    pass

# -*- listscreen -*-
class ListScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()

	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

	def show_instr_popup(self):

		content = BoxLayout(orientation='vertical')
		label = Label(text='Instruction')
		close_button = Button(text='Close')
		content.add_widget(label)
		content.add_widget(close_button)

		popup = Popup(title='Instruction', content=content, size_hint=(None, None), size=(400, 400))

		close_button.bind(on_release=popup.dismiss)

		popup.open()

	def start_instructions(self):
		self.show_instr_popup()

	def show_settings_popup(self):
		content = BoxLayout(orientation='vertical')
		label = Label(text='Settings')
		close_button = Button(text='Close')
		content.add_widget(label)
		content.add_widget(close_button)

		popup = Popup(title='Settings', content=content, size_hint=(None, None), size=(400, 400))

		close_button.bind(on_release=popup.dismiss)

		popup.open()

	def start_settings(self):
		self.show_settings_popup()
# -*- mainscreen -*-
class MainScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

# -*- deaf inside mainscreen -*-
class DeafScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()
# -*- nondeaf inside mainscreen -*-
class NonDeafScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class DeafLessonsScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class NonDeafLessonsScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class DeafAssessmentsScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class DeafAssessmentsScreen2(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class NonDeafAssessmentsScreen(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

class NonDeafAssessmentsScreen2(Screen):
	def on_enter(self):
		self.play_background_sound()

	def play_background_sound(self):
		self.sound = SoundLoader.load('data/sound/signtopia.mp3')
		if self.sound:
			self.sound.loop = True
			self.sound.play()
			
	def on_leave(self):
		self.stop_background_sound()

	def stop_background_sound(self):
		if self.sound:
			self.sound.stop()
			self.sound.unload()

# -*- deaf number Lesson -*-
class DeafNoLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafnolesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNoLoadingScreen, self).on_leave(*args)
	pass
	
class DeafNumberLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='number/1.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)
		self.video.state = 'play'

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen1, self).on_leave(*args)
	pass

class DeafNumberLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/2.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen2, self).on_leave(*args)
	pass

class DeafNumberLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/3.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen3, self).on_leave(*args)
	pass

class DeafNumberLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/4.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen4, self).on_leave(*args)
	pass

class DeafNumberLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/5.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen5, self).on_leave(*args)
	pass

class DeafNumberLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/6.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen6, self).on_leave(*args)
	pass

class DeafNumberLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/7.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen7, self).on_leave(*args)
	pass

class DeafNumberLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/8.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen8, self).on_leave(*args)
	pass

class DeafNumberLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/9.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen9, self).on_leave(*args)
	pass

class DeafNumberLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/10.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNumberLessonScreen10, self).on_leave(*args)
	pass

# -*- deaf number Assessment -*-
class DeafNoLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafnoassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafNoLoadingAsScreen, self).on_leave(*args)
	pass
	
class DeafNumberAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		self.num_items = len(self.answers)
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.video.volume = 0
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=80,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\nYou scored {score_percentage}%.\n{grade}',
            color=(0, 0, 0, 1),
            font_size='60sp',
            bold=True,
            size_hint=(None, None),
            halign='center',
            valign='middle'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.77})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.28})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(DeafNumberAssessmentScreen, self).on_leave(*args)
	pass

# -*- nondeaf number Lesson -*-
class NonDeafNoLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafnolesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNoLoadingScreen, self).on_leave(*args)
	pass
	
class NonDeafNumberLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='number/1.mp4', options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)
		self.video.state = 'play'

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen1, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/2.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen2, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/3.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen3, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/4.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen4, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/5.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen5, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/6.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen6, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/7.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen7, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/8.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen8, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/9.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen9, self).on_leave(*args)
	pass

class NonDeafNumberLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='number/10.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNumberLessonScreen10, self).on_leave(*args)
	pass

# -*- nondeaf number assessment -*-
class NonDeafNoLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafnoassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafNoLoadingAsScreen, self).on_leave(*args)
	pass
	
class NonDeafNumberAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
		self.num_items = len(self.answers)
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=80,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\nYou scored {score_percentage}%.\n{grade}',
            color=(0, 0, 0, 1),
            font_size='60sp',
            bold=True,
            size_hint=(None, None),
            halign='center',
            valign='middle'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.77})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.28})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(NonDeafNumberAssessmentScreen, self).on_leave(*args)
	pass

class DeafAlLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafallesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLoadingScreen, self).on_leave(*args)
	pass
	
class DeafAlLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='alphabet/a.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen1, self).on_leave(*args)
	pass

class DeafAlLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/b.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen2, self).on_leave(*args)
	pass

class DeafAlLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/c.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen3, self).on_leave(*args)
	pass

class DeafAlLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/d.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen4, self).on_leave(*args)
	pass

class DeafAlLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/e.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen5, self).on_leave(*args)
	pass

class DeafAlLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/f.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen6, self).on_leave(*args)
	pass

class DeafAlLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/g.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen7, self).on_leave(*args)
	pass

class DeafAlLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/h.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen8, self).on_leave(*args)
	pass

class DeafAlLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/i.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen9, self).on_leave(*args)
	pass

class DeafAlLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/j.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen10, self).on_leave(*args)
	pass

class DeafAlLessonScreen11(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/k.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen11, self).on_leave(*args)
	pass

class DeafAlLessonScreen12(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/l.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen12, self).on_leave(*args)
	pass

class DeafAlLessonScreen13(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/m.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen13, self).on_leave(*args)
	pass

class DeafAlLessonScreen14(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/n.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen14, self).on_leave(*args)
	pass

class DeafAlLessonScreen15(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/o.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen15, self).on_leave(*args)
	pass

class DeafAlLessonScreen16(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/p.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen16, self).on_leave(*args)
	pass

class DeafAlLessonScreen17(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/q.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen17, self).on_leave(*args)
	pass

class DeafAlLessonScreen18(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/r.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen18, self).on_leave(*args)
	pass

class DeafAlLessonScreen19(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/s.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen19, self).on_leave(*args)
	pass

class DeafAlLessonScreen20(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/t.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen20, self).on_leave(*args)
	pass

class DeafAlLessonScreen21(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/u.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen21, self).on_leave(*args)
	pass

class DeafAlLessonScreen22(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/v.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen22, self).on_leave(*args)
	pass

class DeafAlLessonScreen23(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/w.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen23, self).on_leave(*args)
	pass

class DeafAlLessonScreen24(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/x.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen24, self).on_leave(*args)
	pass

class DeafAlLessonScreen25(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/y.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen25, self).on_leave(*args)
	pass

class DeafAlLessonScreen26(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/z.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLessonScreen26, self).on_leave(*args)
	pass

class DeafAlLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafalassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafAlLoadingAsScreen, self).on_leave(*args)
	pass
	
class DeafAlphabetAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L','M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W', 'X','Y', 'Z']
		self.num_items = 10
		self.total_guesses = 0
		self.correct_guesses = 0
		self.current_answer = None
		self.score_label = Label(text='Score: 0%')
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.video.volume = 0
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=80,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.add_widget(self.layout)
		self.next_question()
		
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\nYou scored {score_percentage}%.\n{grade}',
            color=(0, 0, 0, 1),
            font_size='60sp',
            bold=True,
            size_hint=(None, None),
            halign='center',
            valign='middle'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.77})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.28})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		self.remove_widget(self.background_image)
		self.remove_widget(self.retrybutton)
		super(DeafAlphabetAssessmentScreen, self).on_leave(*args)
	pass

class NonDeafAlLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafallesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLoadingScreen, self).on_leave(*args)
	pass
	
class NonDeafAlLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='alphabet/a.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen1, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/b.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen2, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/c.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen3, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/d.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen4, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/e.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen5, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/f.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen6, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/g.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen7, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/h.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen8, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/i.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen9, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/j.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5),  pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen10, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen11(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/k.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen11, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen12(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/l.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen12, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen13(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/m.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen13, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen14(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/n.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen14, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen15(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/o.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen15, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen16(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/p.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen16, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen17(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/q.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen17, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen18(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/r.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen18, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen19(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/s.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen19, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen20(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/t.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen20, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen21(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/u.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen21, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen22(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/v.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen22, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen23(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/w.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen23, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen24(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/x.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen24, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen25(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/y.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen25, self).on_leave(*args)
	pass

class NonDeafAlLessonScreen26(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='alphabet/z.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLessonScreen26, self).on_leave(*args)
	pass

class NonDeafAlLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafalassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafAlLoadingAsScreen, self).on_leave(*args)
	pass
	
class NonDeafAlphabetAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['A', 'B', 'C', 'D','E', 'F', 'G', 'H','I', 'J', 'K', 'L','M', 'N', 'O', 'P','Q', 'R', 'S', 'T','U', 'V', 'W', 'X','Y', 'Z']
		self.num_items = 10
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=80,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\nYou scored {score_percentage}%.\n{grade}',
            color=(0, 0, 0, 1),
            font_size='60sp',
            bold=True,
            size_hint=(None, None),
            halign='center',
            valign='middle'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.77})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.28})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(NonDeafAlphabetAssessmentScreen, self).on_leave(*args)
	pass
# -*- deaf word Lesson -*-
class DeafWoLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafwolesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWoLoadingScreen, self).on_leave(*args)
	pass
	
class DeafWordLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='word/welcome.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)
	
	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen1, self).on_leave(*args)
	pass

class DeafWordLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/no.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen2, self).on_leave(*args)
	pass

class DeafWordLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/please.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen3, self).on_leave(*args)
	pass

class DeafWordLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/yes.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen4, self).on_leave(*args)
	pass

class DeafWordLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/goodbye.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen5, self).on_leave(*args)
	pass

class DeafWordLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/bathroom.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen6, self).on_leave(*args)
	pass

class DeafWordLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/hello.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen7, self).on_leave(*args)
	pass

class DeafWordLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/thank you.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen8, self).on_leave(*args)
	pass

class DeafWordLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/me.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen9, self).on_leave(*args)
	pass

class DeafWordLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)
		
		self.video = Video(source='word/help.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0
		
		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWordLessonScreen10, self).on_leave(*args)
	pass

# -*- deaf word Assessment -*-
class DeafWoLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafwoassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafWoLoadingAsScreen, self).on_leave(*args)
	pass
	
class DeafWordAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['Help', 'No', 'Please', 'Yes']
		self.num_items = len(self.answers)
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.video.volume = 0
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=80,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\nYou scored {score_percentage}%.\n{grade}',
            color=(0, 0, 0, 1),
            font_size='60sp',
            bold=True,
            size_hint=(None, None),
            halign='center',
            valign='middle'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.77})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.28})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(DeafWordAssessmentScreen, self).on_leave(*args)
	pass
# -*- nondeaf word Lesson -*-
class NonDeafWoLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafwolesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWoLoadingScreen, self).on_leave(*args)
	pass
	
class NonDeafWordLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='word/welcome.mp4', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'
	
	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen1, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen2(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/no.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)

		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)

		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)

		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen2, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen3(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/please.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen3, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen4(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/yes.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen4, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen5(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/goodbye.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen5, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen6(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/bathroom.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen6, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen7(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/hello.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen7, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen8(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/thank you.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen8, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen9(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/me.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen9, self).on_leave(*args)
	pass

class NonDeafWordLessonScreen10(Screen):
	def __init__(self, **kwargs):
		super().__init__(**kwargs)

		self.video = Video(source='word/help.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWordLessonScreen10, self).on_leave(*args)
	pass

# -*- nondeaf word assessment -*-
class NonDeafWoLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafwoassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafWoLoadingAsScreen, self).on_leave(*args)
	pass
	
class NonDeafWordAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['Welcome', 'No', 'Please', 'Yes', 'Goodbye', 'Bathroom']
		self.num_items = 10
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=50,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)
    
		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1


		self.random_answers = random.sample(list(self.answers), k=2)
		while self.current_answer in self.random_answers:
			self.random_answers = random.sample(list(self.answers), k=2)
		random.shuffle(self.random_answers)
		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
    

		correct_button = random.choice(self.buttons)
		correct_button.text = self.current_answer

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\n\nYou scored {score_percentage}%.\n\n{grade}',
            color=(0.7, 0.2, 0.4, 1),
            font_size='65sp',
            bold=True,
            size_hint=(None, None),
	    	text_size= (700, None),
            halign='center',
            valign='middle',
			font_name='data/font/Pusa.otf'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.8})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.26})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(NonDeafWordAssessmentScreen, self).on_leave(*args)
	pass

class DeafSeLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafselesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafSeLoadingScreen, self).on_leave(*args)
	pass
	
class DeafSentenceLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='sentence/1.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})
		self.video.volume = 0

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafSentenceLessonScreen1, self).on_leave(*args)
	pass

class DeafSeLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'deafseassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(DeafSeLoadingAsScreen, self).on_leave(*args)
	pass
	
class DeafSentenceAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['Have a nice day(Have nice day)','Hello','No',]
		self.num_items = 10
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.video.volume = 0
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=50,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)

		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1

        # Exclude the current answer from the random choices
		remaining_answers = [answer for answer in self.answers if answer != self.current_answer]
		self.random_answers = random.sample(remaining_answers, k=2)

        # Randomly select a button index for the correct answer
		correct_button_index = random.randint(0, 1)

		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
			self.buttons[i].font_size = 25
			self.buttons[i].text_size = self.buttons[i].size
			self.buttons[i].halign = 'center'
			self.buttons[i].valign = 'center'

        # Assign the correct answer to the correct button
		self.buttons[correct_button_index].text = self.current_answer
		self.buttons[correct_button_index].font_size = 20
		self.buttons[correct_button_index].text_size = self.buttons[correct_button_index].size
		self.buttons[correct_button_index].halign = 'center'
		self.buttons[correct_button_index].valign = 'center'

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\n\nYou scored {score_percentage}%.\n\n{grade}',
            color=(0.7, 0.2, 0.4, 1),
            font_size='65sp',
            bold=True,
            size_hint=(None, None),
	    	text_size= (700, None),
            halign='center',
            valign='middle',
			font_name='data/font/Pusa.otf'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.8})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.26})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(DeafSentenceAssessmentScreen, self).on_leave(*args)
	pass

class NonDeafSeLoadingScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafselesson1'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafSeLoadingScreen, self).on_leave(*args)
	pass
	
class NonDeafSentenceLessonScreen1(Screen):
	def on_enter(self):
		self.video = Video(source='sentence/1.mp4', state='play',options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.41, 'center_y': 0.6})

		self.play_button = TransparentButton(size_hint=(0.1, 0.1), pos_hint={'center_x': 0.4, 'center_y': 0.35}, source='data/btn/PLAY.png', allow_stretch=True, keep_ratio=False)
		self.play_button.bind(on_press=self.play_video)
		
		self.pause_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.5, 'center_y': 0.35}, source='data/btn/PAUSE.png', allow_stretch=True, keep_ratio=False)
		self.pause_button.bind(on_press=self.pause_video)
		
		self.repeat_button = TransparentButton(size_hint=(0.10, 0.10), pos_hint={'center_x': 0.6, 'center_y': 0.35}, source='data/btn/REPLAY.png', allow_stretch=True, keep_ratio=False)
		self.repeat_button.bind(on_press=self.repeat_video)
		
		self.add_widget(self.video)
		self.add_widget(self.play_button)
		self.add_widget(self.pause_button)
		self.add_widget(self.repeat_button)

	def play_video(self, instance):
		self.video.state = 'play'

	def pause_video(self, instance):
		self.video.state = 'pause'
	
	def repeat_video(self, instance):
		self.video.state= 'stop'
		self.video.state= 'play'

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafSentenceLessonScreen1, self).on_leave(*args)
	pass

class NonDeafSeLoadingAsScreen(Screen):
	def on_enter(self):
		self.video = Video(source='data/loading2.mp4', play=True, allow_stretch=True, keep_ratio=False, pos= self.pos, size= self.size)
		self.add_widget(self.video)
		Clock.schedule_once(self.load_main_content, 8)

	def load_main_content(self, dt):
		self.manager.current = 'nondeafseassessment'

	def on_leave(self, *args):
		self.video.state = 'stop'
		self.remove_widget(self.video)
		super(NonDeafSeLoadingAsScreen, self).on_leave(*args)
	pass
	
class NonDeafSentenceAssessmentScreen(Screen):
	def on_enter(self, *args):
		self.answers = ['Have a nice day','Hello','No',]
		self.num_items = 10
		self.total_guesses = 0
		self.correct_guesses = 0
		self.layout = BoxLayout(orientation='vertical')
		self.video = Video(source='', state='play', options={'eos': 'loop'}, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.6})
		self.add_widget(self.video)
		self.answer_label = Label(text='')
		self.layout.add_widget(self.answer_label)
		self.retrybutton = TransparentButton()
		self.background_image = Image()
		self.image_widget = Image()
		self.button_layout = BoxLayout(orientation='horizontal', size_hint=(0.3, 0.3), pos_hint={'center_x': 0.5, 'center_y': 0}, spacing=50)
		self.layout.add_widget(self.button_layout)
		self.buttons = []
		self.current_answer = None
		self.random_answers = random.sample(list(self.answers), k=2)
		for answer in self.random_answers:
			button = Button(background_normal='data/btn/BLANKBUTTON.png', text=answer, font_size=50,
                on_press=self.check_answer, size_hint=(0.5, 0.5), pos_hint={'center_x': 0.5, 'center_y': 0.99},
                padding=(0, 0), font_name='data/font/coiny.ttf')
			self.buttons.append(button)
			self.button_layout.add_widget(button)
		self.score_label = Label(text='Score: 0%')
		self.add_widget(self.layout)
		self.next_question()
	
	def is_answer_correct(self, selected_answer):
		if self.current_answer.lower() in self.video.source.lower() and selected_answer == self.current_answer:
			return True
		return False

	def next_question(self):
		previous_answer = self.current_answer
		self.current_answer = random.choice(self.answers)
		while self.current_answer == previous_answer:
			self.current_answer = random.choice(self.answers)

		self.video.source = f'assessment/{self.current_answer.lower()}.mp4'
		self.answer_label.text = ''
		self.total_guesses += 1

        # Exclude the current answer from the random choices
		remaining_answers = [answer for answer in self.answers if answer != self.current_answer]
		self.random_answers = random.sample(remaining_answers, k=2)

        # Randomly select a button index for the correct answer
		correct_button_index = random.randint(0, 1)

		for i, answer in enumerate(self.random_answers):
			self.buttons[i].text = answer
			self.buttons[i].font_size = 25
			self.buttons[i].text_size = self.buttons[i].size
			self.buttons[i].halign = 'center'
			self.buttons[i].valign = 'center'

        # Assign the correct answer to the correct button
		self.buttons[correct_button_index].text = self.current_answer
		self.buttons[correct_button_index].font_size = 20
		self.buttons[correct_button_index].text_size = self.buttons[correct_button_index].size
		self.buttons[correct_button_index].halign = 'center'
		self.buttons[correct_button_index].valign = 'center'

		self.enable_buttons()

	def check_answer(self, instance):
		self.disable_buttons()
		if instance.text == self.current_answer:
			image_source2 = "data/CORRECT.png"
			self.show_popup(image_source2)
			self.correct_guesses += 1
		else:
			image_source2 = "data/WRONG.png"
			self.show_popup(image_source2)
		self.score_label.text = f'Score: {round(self.correct_guesses / self.total_guesses * 100, 2)}%'

		if self.total_guesses < self.num_items:
			self.next_question()
		else:
			self.end_game()

	def show_popup(self, image_source2):
		popup = Popup(title="", separator_height=0, background_color=[0, 0, 0, 0], background='')

		content_layout = BoxLayout(orientation='vertical')

		image = Image(source=image_source2, size_hint=(1, 1))

		image.bind(on_touch_down=lambda instance, touch: popup.dismiss() if image.collide_point(*touch.pos) else False)

		content_layout.add_widget(image)

		popup.content = content_layout

		popup.open()

	def disable_buttons(self):
		for button in self.buttons:
			button.disabled = True

	def enable_buttons(self):
		for button in self.buttons:
			button.disabled = False

	def end_game(self):
		self.video.source = ''
		score_percentage = round(self.correct_guesses / self.num_items * 100, 2)
		score_text = f'{self.correct_guesses} / {self.num_items}'

		grade = ""
		image_source = ""

		if score_percentage >= 90:
			grade = "I get it, and don't need any help!"
			image_source = "data/3stars.png"
		elif score_percentage >= 80:
			grade = "I get it, and made a couple of mistakes."
			image_source = "data/2stars.png"
		elif score_percentage >= 70:
			grade = "I need help, and am making some mistakes."
			image_source = "data/1stars.png"
		else:
			grade = "I am struggling."
			image_source = "data/0stars.png"
		
		background_image_source = 'data/bluebox.png'

		self.background_image = Image(source=background_image_source, size_hint=(0.68,0.68), pos_hint={'center_x': 0.5, 'center_y': 0.5} , keep_ratio=True, allow_stretch=True)

		self.add_widget(self.background_image)

		self.answer_label = Label(
            text=f'Game over!\n{score_text}\n\nYou scored {score_percentage}%.\n\n{grade}',
            color=(0.7, 0.2, 0.4, 1),
            font_size='65sp',
            bold=True,
            size_hint=(None, None),
	    	text_size= (700, None),
            halign='center',
            valign='middle',
			font_name='data/font/Pusa.otf'
        )
		self.answer_label.pos_hint = {'center_x': 0.5, 'center_y': 0.5}
		self.add_widget(self.answer_label)

		self.image_widget = Image(source=image_source, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.8})
		self.add_widget(self.image_widget)

		self.disable_buttons()

		self.retrybutton = TransparentButton(source='data/btn/RETRY.png', on_press=self.restart_game, size_hint=(1, 1), pos_hint={'center_x': 0.5, 'center_y': 0.26})
		self.add_widget(self.retrybutton)

	def _update_background(self, instance, value):
		self.background_image.size = self.size
		self.background_image.pos = self.pos
	
	def restart_game(self, instance):
		self.total_guesses = 0
		self.correct_guesses = 0
		self.answer_label.text = ''
		self.score_label.text = 'Score: 0%'
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.image_widget)
		self.next_question()

	def on_leave(self, *args):	
		self.video.state = 'stop'
		self.remove_widget(self.video)
		self.remove_widget(self.retrybutton)
		self.remove_widget(self.background_image)
		self.remove_widget(self.answer_label)
		self.remove_widget(self.image_widget)
		super(NonDeafSentenceAssessmentScreen, self).on_leave(*args)
	pass

class signtopia(App):
	def build(self):
		sm = SignTopiaManager()
		sm.add_widget(LoadingScreen(name='loading'))
		sm.add_widget(ListScreen(name='list'))
		# -*- lesson -*-
		sm.add_widget(DeafNoLoadingScreen(name='deafnoloading'))
		sm.add_widget(DeafNumberLessonScreen1(name='deafnolesson1'))

		sm.add_widget(NonDeafNoLoadingScreen(name='nondeafnoloading'))
		sm.add_widget(NonDeafNumberLessonScreen1(name='nondeafnolesson1'))

		sm.add_widget(DeafAlLoadingScreen(name='deafalloading'))
		sm.add_widget(DeafAlLessonScreen1(name='deafallesson1'))

		sm.add_widget(NonDeafAlLoadingScreen(name='nondeafalloading'))
		sm.add_widget(NonDeafAlLessonScreen1(name='nondeafallesson1'))

		sm.add_widget(DeafWoLoadingScreen(name='deafwoloading'))
		sm.add_widget(DeafWordLessonScreen1(name='deafwolesson1'))

		sm.add_widget(NonDeafWoLoadingScreen(name='nondeafwoloading'))
		sm.add_widget(NonDeafWordLessonScreen1(name='nondeafwolesson1'))

		sm.add_widget(DeafSeLoadingScreen(name='deafseloading'))
		sm.add_widget(DeafSentenceLessonScreen1(name='deafselesson1'))

		sm.add_widget(NonDeafSeLoadingScreen(name='nondeafseloading'))
		sm.add_widget(NonDeafSentenceLessonScreen1(name='nondeafselesson1'))
		# -*- assessment -*-
		sm.add_widget(DeafNoLoadingAsScreen(name='deafnoloadingas'))
		sm.add_widget(DeafNumberAssessmentScreen(name='deafnoassessment'))

		sm.add_widget(NonDeafNoLoadingAsScreen(name='nondeafnoloadingas'))
		sm.add_widget(NonDeafNumberAssessmentScreen(name='nondeafnoassessment'))

		sm.add_widget(DeafAlLoadingAsScreen(name='deafalloadingas'))
		sm.add_widget(DeafAlphabetAssessmentScreen(name='deafalassessment'))

		sm.add_widget(NonDeafAlLoadingAsScreen(name='nondeafalloadingas'))
		sm.add_widget(NonDeafAlphabetAssessmentScreen(name='nondeafalassessment'))

		sm.add_widget(DeafWoLoadingAsScreen(name='deafwoloadingas'))
		sm.add_widget(DeafWordAssessmentScreen(name='deafwoassessment'))

		sm.add_widget(NonDeafWoLoadingAsScreen(name='nondeafwoloadingas'))
		sm.add_widget(NonDeafWordAssessmentScreen(name='nondeafwoassessment'))

		sm.add_widget(DeafSeLoadingAsScreen(name='deafseloadingas'))
		sm.add_widget(DeafSentenceAssessmentScreen(name='deafseassessment'))

		sm.add_widget(NonDeafSeLoadingAsScreen(name='nondeafseloadingas'))
		sm.add_widget(NonDeafSentenceAssessmentScreen(name='nondeafseassessment'))		
		return sm
	
	def on_pause(self):
		return True
	def on_resume(self):
		pass

if __name__=='__main__':
    signtopia().run()