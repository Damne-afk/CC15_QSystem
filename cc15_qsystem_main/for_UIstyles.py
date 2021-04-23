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

# Standard style for buttons dynamically added

class Style():

    style_bt_standard = (
    """
    QPushButton {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(37, 39, 77);
        background-color: rgb(37, 39, 77);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton[Active=true] {
        background-image: ICON_REPLACE;
        background-position: left center;
        background-repeat: no-repeat;
        border: none;
        border-left: 28px solid rgb(37, 39, 77);
        background-color: rgb(37, 39, 77);
        text-align: left;
        padding-left: 45px;
    }
    QPushButton:hover {
        background-color: rgb(48, 51, 102);
        border-left: 28px solid rgb(48, 51, 102);
    }
    QPushButton:pressed {
        background-color: rgb(85, 170, 255);
        border-left: 28px solid rgb(85, 170, 255);
    }
    """
    )
