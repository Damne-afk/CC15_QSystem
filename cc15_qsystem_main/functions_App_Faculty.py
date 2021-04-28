################################################################################
##
## BY: WANDERSON M.PIMENTA
## PROJECT MADE WITH: Qt Designer and PySide2
## V: 1.0.0
##
## This project can be used freely for all uses, as long as they maintain the
## respective credits only in the Python scripts, any information in the visual
## interface (GUI) can be modified without any implication.
##
## There are limitations on Qt licenses if you want to use your products
## commercially, I recommend reading them on the official website:
## https://doc.qt.io/qtforpython/licenses.html
##
################################################################################

## ==> GUI FILE
from main_Faculty import *

class AppFunctions(MainWindow):

    def setDayAvlText(self,text):
        dayLex = {'Monday' : 0, 'Tuesday' : 1, 'Wednesday' : 2, 'Thursday' : 3, 'Friday' : 4, 'Saturday' : 5}
        
        #listofDaySelections = ['Tuesday','Thursday','Monday','Saturday','Friday']
        #listofDaySelections.sort(key=lambda x: dayLex[x])
        #print(listofDaySelections)

        #listofTimeSelections = ["3:00-4:30","9:00-10:30","4:30-6:00","12:00-1:30","7:30-9:00"]
        #listofTimeSelections.sort(key=lambda x: timeLex[x])
        #print(listofTimeSelections)
        
        print(text)
    def setTimeAvlText(self,text):
        timeLex = {"7:30-9:00" : 0,"9:00-10:30" : 1,"10:30-12:00" : 2,"12:00-1:30" : 3,
                   "1:30-3:00" : 4, "3:00-4:30" : 5, "4:30-6:00" : 6}

    def setColorT(self,text):
        if text == "Red":
            self.ui.day_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid red; border-bottom: 4px solid red;")

            self.ui.time_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid red; border-bottom: 4px solid red;")

            return

        if text == "Blue":
            self.ui.day_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid blue; border-bottom: 4px solid blue;")

            self.ui.time_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid blue; border-bottom: 4px solid blue;")
            
            return

        if text == "Yellow":
            self.ui.day_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid yellow; border-bottom: 4px solid yellow;")

            self.ui.time_avl_l2.setStyleSheet("font-size:9pt; margin-top:4px;\n"
            "border-top: 4px solid yellow; border-bottom: 4px solid yellow;")

            return

