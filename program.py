from myfunc import test_function

def variable_test():
    global var
    print(var)
    var = "changed"

print("main procedure")

var = "Hello, World!"
variable_test()
test_function(var)
print("Everything's successful!!")
