class MyException(Exception):

    def __init__(self, message=None):
        super().__init__(message)
        self.message = message
  

class MyClass:
    
    def __init__(self):
        self.value = 0
    
    def set_value(self, new_value):
        if new_value < 0:
            raise MyException("The value cannot be less than 0")
        self.value = new_value

my_class = MyClass()

try:
    my_class.set_value(-5)
except MyException as e:
    print(f"error: {e}")