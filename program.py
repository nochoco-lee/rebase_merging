from myfunc import test_function

def variable_test():
    global var
    print(var)
    var = "changed"

var = "Hello, World!"
variable_test()
test_function(var)

print("main procedure")
