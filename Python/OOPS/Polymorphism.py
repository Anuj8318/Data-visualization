print("This is Polymorphism")
# this is method overloding
# def setData(name,age):
#     print("Name is ",name)
#     print("Age is ",age)


# def setData(sid,name,age):
#     print("Name is ",name)
#     print("Age is ",age)
#     print("sid is ",sid)


# # setData("anuj",25)
# setData(101,"anuj",20)


# this is method overriding
class parent:
    def house(self):
        print("This is parent house")

class child(parent):
    def show(self):
        print("this is the show method")
    def house(self):
        print("This is the child house")


obj = child()
obj.show()
obj.house()

obj1= parent()
obj1.house()