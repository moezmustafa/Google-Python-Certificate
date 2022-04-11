from tkinter.messagebox import RETRY


def func(hours, minutes ,seconds):
    """This code returns the ammount of seconds in total"""
    return hours*3600+minutes*60+seconds

print(func(1,2,3))

help(func)  #this will return the docstring that is saved in the funciton block , the indentation do matter here






from tkinter.messagebox import RETRY


def func(self , name , hours, minutes ,seconds):
    self.name = name
    """This code returns the ammount of seconds in total {}""".format(self.name)
    return hours*3600+minutes*60+seconds

print(func("moeez",1,2,3))

help(func)  #this will return the docstring that is saved in the funciton block , the indentation do matter here 