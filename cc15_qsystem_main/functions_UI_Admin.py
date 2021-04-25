
def returnAppropriateMod():
    return "main_Admin"

## DONT PUT THIS IN THE TOP; INTENDED TO AVOID CIRCULAR IMPORT

from functions_UI import *

class Admin_UIFunctions(UIFunctions):

    ## Extends the addNewMenu method by giving a popup to choose between the 2 users (student or faculty)
    ## Only for non-admin specific functions (i.e Appointments)
    def addNewMenu(self, name, objName, icon, isTopMenu):
        super().addNewMenu(name, objName, icon, isTopMenu)

        if name == 'APPOINTMENTS':
            button.setMenu(self.ui.popMenu_appointments)
        
        if name == 'TASKS':
            button.setMenu(self.ui.popMenu_special_services)
            
        if name == 'ROOM RESERVATION':
            button.setMenu(self.ui.popMenu_roomNkey)