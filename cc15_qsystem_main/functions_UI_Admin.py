
def returnAppropriateMod():
    return "main_Admin"

## DONT PUT THIS IN THE TOP; INTENDED TO AVOID CIRCULAR IMPORT

from functions_UI import UIFunctions

class Admin_UIFunctions(UIFunctions):

    ## Extends the addNewMenu method by giving a popup to choose between the 2 users (student or faculty)
    ## Only for non-admin specific functions (i.e Appointments)
    def addNewMenu(self, name, objName, icon, isTopMenu):
        super().addNewMenu()
        