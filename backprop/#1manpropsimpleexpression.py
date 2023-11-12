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

a = Value(10)
b = Value(15)
d = Value(3)
c = a + b
e = c * d

e.grad = 1
c.grad = d.data
d.grad = c.data
a.grad = c.grad * 1
b.grad = c.grad * 1
    