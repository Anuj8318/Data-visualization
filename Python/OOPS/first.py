
def show():
    print("This is the show function outside of the class student")


class Student:
    name ="abc"
    age=0
    # method
    def study(self):  #Self is used to  access and manipulate the instance variables and methods within a class.
        # calling show function outside od the class
        show()
        # clling show methos inside the class
        self.show()
        print("Study 9 hour",self.name)
    
    def show(self):
        print("This is the show method inside of the class student")

# here we made an object (with name obj). 
obj = Student()
obj.study()



class A:
    name="Anant"
    def show(self):
        print("This is A class show method")
    
class B:
    pass