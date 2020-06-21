from gui import *

if __name__ == "__main__":
    g = gui()
    main = g.mainPage()
    if main[0] is not None:  
        if main[0] == 'button_single':
            select = g.selectPage()

            if select[0] == 'button_rock':
                result = g.resultPage(1)
            elif select[0] == 'button_paper':
                result = g.resultPage(2)
            elif select[0] == 'button_scissors':
                result = g.resultPage(3)
        elif main[0] == 'button_multi':
            sg.popup('Not now !', 'There is no multiplayer right now.')
    sg.Window.close()
    
    
