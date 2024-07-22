
# This is the single inheritance
# print("Single Inheritance")
# class A:
#     name="Ananat"
#     def show(self):
#         print("This is the method inside the class A")


# class B(A):
#     def demo(self):
#         print("This is the methos inside the class B")

# obj = B()
# obj.show()
# obj.show()



# this is the multi layer inheritance
# print("Multi layer Inheritance")
# class A:
#     name="Ananat"
#     def show(self):
#         print("This is the method inside the class A")


# class B(A):
#     def demo(self):
#         print("This is the methos inside the class B")

# class C(B):
#     pass

# obj = C()
# obj.show()
# obj.demo()


# this is hierarchical inheritance
# print("Hierarchy Inheritance")
# class A:
#     name="Ananat"
#     def show(self):
#         print("This is the method inside the class A")


# class B(A):
#     def demo(self):
#         print("This is the methos inside the class B")

# class C(A):
#     pass

# obj = C()
# obj.show()



# this is multiple inheritance
# print("multiple Inheritance")
# class A:
#     name="Ananat"
#     def show(self):
#         print("This is the method inside the class A")


# class B():
#     def demo(self):
#         print("This is the methos inside the class B")

# class C(A,B):
#     pass

# obj = C()
# obj.show()
# obj.demo()



# this is hybrid inheritance
print("Hybrid Inheritance")
class A:
    name="Ananat"
    def show(self):
        print("This is the method inside the class A")


class B(A):
    def demo(self):
        print("This is the methos inside the class B")

class C(A):
    def f(self):
        print("this is class c")

class D(B,C):
    pass


obj = D()
obj.show()
obj.demo()
obj.f()
