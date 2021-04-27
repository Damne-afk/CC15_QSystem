
def returnAppropriateMod():
    return "main_Faculty"
    
## DONT PUT THIS IN THE TOP; INTENDED TO AVOID CIRCULAR IMPORT
from functions_UI import UIFunctions

class Faculty_UIFunctions(UIFunctions):
    def someFunc(self):
        pass

    