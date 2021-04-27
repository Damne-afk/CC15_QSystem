
def returnAppropriateMod():
    return "main_Admin"

## DONT PUT THIS IN THE TOP; INTENDED TO AVOID CIRCULAR IMPORT


from PyQt5.QtWidgets import QComboBox, QFrame, QHBoxLayout
from functions_UI import UIFunctions
from animated_toggle import AnimatedToggle
from main_Admin import *

class Admin_UIFunctions(UIFunctions):

## STUDENT_USER FUNCS | START
#def
## STUDENT_USER FUNCS | END

## FACULTY_USER FUNCS | START
    def addSched():
        pass
            

"""
        schedFrame = QFrame()
        schedFrame.setFrameShape(QFrame.StyledPanel)
        schedFrame.setFrameShadow(QFrame.Raised)
        schedLayout = QHBoxLayout()
        schedLayout.setSpacing(12)
        schedLayout.setContentsMargins(0, 3, 3, 0)

        colorList = ["Red","Indigo","Yellow"]
        colorCombobox = QComboBox()
        colorCombobox.addItems(colorList)
        colorCombobox.setCurrentIndex(0)
        colorCombobox.activated[str].connect(lambda: frameBorderColor())
        dayList = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
        dayCombobox = QComboBox()
        dayCombobox.addItems(dayList)
        dayCombobox.setPlaceholderText("Day Available")
        timeList = ["7:30-9:00","9:00-10:30","10:30-12:00","12:00-1:30","1:30-3:00","3:00-4:30","4:30-6:00"]
        timeCombobox = QComboBox()
        timeCombobox.addItems(timeList)
        timeCombobox.setPlaceholderText("Time Available")
"""



#self.ui.verticalLayout_fac_avl_scrollArea_contents.addWidget()
## FACULTY_USER FUNCS | END

## ADMIN_USER FUNCS | START
#def
## ADMIN_USER FUNCS | END