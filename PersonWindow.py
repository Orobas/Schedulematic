import pyforms
from   pyforms          import BaseWidget
from   pyforms.Controls import ControlText
from   pyforms.Controls import ControlButton
from   pyforms.Controls import ControlCheckBoxList
from   pyforms.Controls import ControlCheckBox
from   Person           import Person

class PersonWindow(BaseWidget):

    def __init__(self):
        Person.__init__(self, '', '', '')
        BaseWidget.__init__(self, 'Person Window')
        #super(SimpleExample1,self).__init__('Simple example 1')

        #Definition of the forms fields
        self.mainmenu = [
            { 
                'File': [
                    {'Open': self.__dummyevent},
                    '-',
                    {'Save': self.__dummyevent},
                    {'Save as': self.__dummyevent}
                ]
            },
            {
                'Settings': [
                    {'Workplaces': self.__openWork},
                    {'Employees': self.__openemployees}
        ]
        self._firstname     = ControlText('First name', 'John')
        self._lastname      = ControlText('Last name', 'Doe')
        self._fullname      = ControlText('Full name')
        self._button        = ControlButton('Press this button')
        self._alldays       = ControlCheckBox('All days')
        self._alldays.changed_event = self.__alldaysAction
        self._days          = ControlCheckBoxList('Days')
        self._days         += ('Monday', True)
        self._days         += ('Tuesday', True)
        self._days         += ('Wednesday', True)
        self._days         += ('Thursday', True)
        self._days         += ('Friday', True)
        self._days         += ('Saturday', True)
        self._days         += ('Sunday', True)
        self._allshifts     = ControlCheckBox('All shifts')
        self._allshifts.changed_event = self.__allshiftsAction
        self._shifts        = ControlCheckBoxList('Shifts')
        self._shifts       += ('Mornings', True)
        self._shifts       += ('Evenings', True)
        self._shifts       += ('Nights', True)
        self._alljobs       = ControlCheckBox('All positions')
        self._alljobs.changed_event = self.__alljobsAction
        self._jobs          = ControlCheckBoxList('Positions')
        self._jobs         += ('Cashier', True)
        self._jobs         += ('Stocker', True)
        self._jobs         += ('Deli', True)
        self._button.value = self.__buttonAction
        self._testbox       = ControlText()
    
    def __openjobs(self):
        self._testbox.hide()
    
    def __buttonAction(self):
        """Button action event"""
        self._fullname.value = self._firstname.value + " " + self._middlename.value + \
        " " + self._lastname.value
        
        if self.parent!=None: self.parent.addPerson(self)
       
    def __alldaysAction(self):
        self._testbox.show()
        
    def __allshiftsAction(self):
        self._testbox.hide()
       
    def __alljobsAction(self):
        self._testbox.hide()

class SimpleExample2(BaseWidget):

    def __init__(self):
        super(SimpleExample2,self).__init__('Simple example 2')
        
        self._secondname    = ControlText('Second name', 'Hello')
        self._secondmiddlename     = ControlText('Second middle name')
        self._secondlastname    = ControlText('Second last name')
        self._secondfullname    = ControlText('Second full name')
        self._secondbutton        = ControlButton('Press this button plz')

def __alljobsActions(self):
    self._textbox.hide()
        
if __name__ == "__main__":   pyforms.start_app( PersonWindow )
#if __name__ == "__main__":     pyforms.start_app( SimpleExample2 )