
class Calculator(object):

    def __init__(self):
        self._last_answser = 0.0

    def cadd(self, x, y):
        return x + y
    
    def csubtract(self, x, y):
        return x - y
    
    def cmultiply(self, x, y):
        return x * y
    
    def cdivide(self, x, y):
        return x / y