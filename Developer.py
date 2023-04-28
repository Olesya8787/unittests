class Developer:
    def __init__(self, name, password, skill):
      self._name = name
      self._password = password
      self._skill = skill

    def say_hello(self):
     return "Hello world"

    def mend_something(self):
      return "01101101"
    
    def write_code(self):
      return [0,1,0,0,1,0]