import os
import logic
import shutil
from kivy.app import App
from functools import lru_cache
from kivy.core.window import Window
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.actionbar import ActionBar
from kivy.core.clipboard import Clipboard
from kivy.uix.screenmanager import ScreenManager, Screen

# Remove the '#' when creating the app.
#------------------------------------------------------------------
# from android.permissions import request_permissions, Permission
# request_permissions([Permission.WRITE_EXTERNAL_STORAGE,
#                      Permission.READ_EXTERNAL_STORAGE])

# from android.storage import primary_external_storage_path
# SD_CARD = primary_external_storage_path()
#------------------------------------------------------------------

@lru_cache(maxsize=10)

class SomeMenu_ActionBar(ActionBar):
    def exporta(self):
        # caminho = os.path.join(SD_CARD,'PG-Passwords') #Phone
        caminho = os.path.join(os.getcwd(),'PG-Passwords') #PC

        os.makedirs(caminho,mode=511, exist_ok=True)
        
        for file_name in os.listdir('passwords'):
            full_file_name = os.path.join('passwords', file_name)
            if os.path.isfile(full_file_name):
                shutil.copy(full_file_name, caminho)

class First(Screen):

    def logic(self,digitos,screen):

        try:

            if screen.ids.all.active == True or screen.ids.numbers.active == True and screen.ids.letters.active == True and screen.ids.symbols.active == True or screen.ids.numbers.active == True and screen.ids.letters.active == True and screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True or screen.ids.numbers.active == True and screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.todos(digitos))
                
            elif screen.ids.letters.active == True and screen.ids.numbers.active == True or screen.ids.numbers.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.NumLet(digitos))

            elif screen.ids.lower.active == True and screen.ids.numbers.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.NumSymLow(digitos))  
                
            elif screen.ids.upper.active == True and screen.ids.numbers.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.NumSymUpp(digitos))  

            elif screen.ids.symbols.active == True and screen.ids.numbers.active == True:
                
                self.display.text = str(logic.NumSym(digitos))

            elif screen.ids.letters.active == True and screen.ids.symbols.active == True or screen.ids.symbols.active == True and screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.LetSym(digitos)) 
                
            elif screen.ids.lower.active == True and screen.ids.numbers.active == True:
                
                self.display.text = str(logic.NumLow(digitos))  
                
            elif screen.ids.numbers.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.NumUpp(digitos)) 

            elif screen.ids.lower.active == True and screen.ids.symbols.active == True:
                
                self.display.text = str(logic.LowSym(digitos)) 

            elif screen.ids.symbols.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.UppSym(digitos)) 

            elif screen.ids.letters.active == True or screen.ids.lower.active == True and screen.ids.upper.active == True:
                
                self.display.text = str(logic.letters(digitos))
                
            elif screen.ids.numbers.active == True:
                
                self.display.text = str(logic.numbers(digitos))

            elif screen.ids.symbols.active == True:
                
                self.display.text = str(logic.symbols(digitos))  

            elif screen.ids.lower.active == True:
                
                self.display.text = str(logic.LowerCase(digitos))

            elif screen.ids.upper.active == True:
                
                self.display.text = str(logic.UpperCase(digitos)) 

        
        except Exception:
            self.display.text = "Error"
    
    def copy(self,condicao):
        Clipboard.copy(condicao)

class Option(Screen):

    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,Window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "first"
            return True

    def leave(self):
        Window.unbind(on_keyboard=self.voltar)

if not 'passwords' in os.listdir():
    os.mkdir('./passwords')

class Save(Screen):
    
    def __init__(self,passwords = os.listdir('passwords'), **kwargs):
        super().__init__(**kwargs)

        for i in passwords:
            
            a = i
            b = ".txt"
            a = a.replace(b,"")

            self.ids.boxsave.add_widget(Remove(text=a))

    def addWidget(self):
        texto = self.ids.datasave.text
        self.ids.boxsave.add_widget(Remove(text=texto))
        
    def copy(self,condicao):
        Clipboard.copy(condicao)
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,Window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "first"
            return True

    def leave(self):
        Window.unbind(on_keyboard=self.voltar)

class Remove(BoxLayout):

    def __init__(self, text = '',**kwargs):
        super().__init__(**kwargs)
        self.ids.arquivo.text = text
    
    def RemoveFile(self,file):
        try:
            os.remove('passwords//'+file+'.txt')
        except Exception:
            pass

    def read(self,file):
        f = open('passwords//'+file+'.txt')
        self.copyy = f.read()

    def copy(self):
        Clipboard.copy(self.copyy)

class SaveText(Screen):

    def escrever(self,nome,data):
        escrever = [data]
        with open(f'passwords//{nome}.txt','w') as arquivos:
            for valor in escrever:
                arquivos.write(str(valor))
    
    def addWidget(self,c):
        texto = self.ids.name.text
        c.ids.boxsave.add_widget(Remove(text=texto))

    def RemoveFile(self,file):
        try:
            os.remove('passwords//'+file+'.txt')
        except Exception:
            pass
    
    def creator(self,resto):

        for i in os.listdir('passwords'):
            
            a = i
            b = ".txt"
            ab = a.replace(b,"")

            resto.ids.boxsave.add_widget(Remove(text=ab))
    
    def on_pre_enter(self):
        Window.bind(on_keyboard=self.voltar)

    def voltar(self,Window,key,*args):
        if key == 27:
            App.get_running_app().root.current = "first"
            return True

    def leave(self):
        Window.unbind(on_keyboard=self.voltar)

class app(App):

    def build(self):
        
        sm = ScreenManager()
        sm.add_widget(First(name='first'))
        sm.add_widget(Option(name='option'))
        sm.add_widget(Save(name='save'))
        sm.add_widget(SaveText(name='savetext'))
        return sm

if __name__ == "__main__":
    app().run()
