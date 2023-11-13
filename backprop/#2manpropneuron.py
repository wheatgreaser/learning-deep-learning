import math
class Value:
  def __init__(self, data, _children=(), _op=''):
    self.data = data
    self._prev = set(_children)
    self._op = _op
    self.grad = 0
  def __repr__(self):
    return(f"Value = {self.data}")
    
  def __add__(self, other):
    return(Value(self.data + other.data, (self, other), '+'))
    
  def __mul__(self, other):
    return(Value(self.data * other.data, (self, other), '*'))

  def tanh(self):
    x = self.data
    t = (math.exp(2*x) - 1)/(math.exp(2*x) + 1)
    return(Value(t, (self, ), 'tanh'))

w1 = Value(2.0)
w2 = Value(3.0)
x1 = Value(2.0)
x2 = Value(4.0)
b = Value(1.0)
n = w1 * x1 + w2 * x2 + b
o = n.tanh()
o.grad = 1
n.grad = 1 - (o.data * o.data)
w1.grad = n.grad * x1.data
w2.grad = n.grad * x2.data
print(w1.grad)
print(w2.grad)



    