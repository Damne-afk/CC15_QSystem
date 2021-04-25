
def returnAppropriateMod():
    return "main_Student"

## DONT PUT THIS IN THE TOP; INTENDED TO AVOID CIRCULAR IMPORT

from functions_UI import *

class Student_UIFunctions(UIFunctions):
    def someFunc(self):
        pass

    