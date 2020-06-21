import PySimpleGUI as sg
from bot import *


class gui:
     
    theme = 'DarkAmber'
    
    
    def __init__(self):
        sg.theme(self.theme) 
        
    def selectPage(self):

        layout = [
            [sg.Text("Get a choice to CREATE A MATCH !!!")],
            [
            sg.Button('Rock', key='button_rock'),
            sg.Button('Paper', key='button_paper'),
            sg.Button('Scissors', key='button_scissors')],
            ] 
        window = sg.Window('ROCKK ITTTT !', layout)
        event, value = window.read()
        return event, value


    def mainPage(self):
        layout = [
            [sg.Text("Select how you want to play ?!")],
            [
            sg.Button('Multiplayer', key='button_multi'),
            sg.Button('Singleplayer', key='button_single')
            ]
        ]
        window = sg.Window('How you want play ?!', layout)
        event, value = window.read()
        return event, value


    def resultPage(self, type1 ):
        
        x = bot()
        type2 = int(x.randomBot())
        result = None
        
        if ( type1 == 1 ):

            if ( type2 == 1 ):
                result = "Game is Draw"
            elif ( type2 == 2 ):
                result = "You'r Lost !!!!"
            elif ( type2 == 3 ):
                result = "You'r WIIIIIINNNN !!!"

        elif ( type1 == 2 ):

            if ( type2 == 1 ):
                result = "WIN"
            elif ( type2 == 2 ):
                result = "DRAW"
            elif ( type2 == 3 ):
                result = "LOST"
        
        elif ( type1 == 3 ):

            if ( type2 == 1 ):
                result = "LOST"
            elif ( type2 == 2 ):
                result = "WIN"
            elif ( type2 == 3 ):
                result = "DRAW"
        
        layout = [
            [
                sg.Image(r'/home/sepehr/Projects/rpsGame/images/%i.png' %type1),
                sg.Text(" VS "),
                sg.Image(r'/home/sepehr/Projects/rpsGame/images/%i.png' %type2),
            ],
            [sg.Text(result, font=("Helvetica", 25))],
        ]
        
        window = sg.Window(result, layout)
        event, value = window.read()
        
        
        