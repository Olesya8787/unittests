from User import User
from Admin import Admin
from Developer import Developer

user = User("Bill", 4545) 
print(user.say_hello())   

admin = Admin("Alex",3456)
print(admin.say_hello())
print(admin.mend_something())

developer = Developer("Tom", 5678, "JS")
print(developer.write_code())
print(developer.mend_something())