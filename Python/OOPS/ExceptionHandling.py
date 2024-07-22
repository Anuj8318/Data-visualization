print("Line 1")
print("Line 2")
print("Line 3")
print("Line 4")
try:
    print(100/0)
    open("files.txt")
except ZeroDivisionError as e:
    print(e)
except FileNotFoundError:
    print("file not found")
    
print("Line 1")
print("Line 1")
print("Line 1")
print("Line 1")
print("Line 1")