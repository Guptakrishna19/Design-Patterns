def decorator_function(original_function):
    def wrapper_function():
        print("Wrapper executed before", original_function.__name__) # This line will be executed before the original function 
        return original_function()
    return wrapper_function

@decorator_function # This is equivalent to say_hello = decorator_function(say_hello)
def say_hello():
    print("Hello, World!")

say_hello()
