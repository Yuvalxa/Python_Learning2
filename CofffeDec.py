class Abstract_Coffee(object):
## how to add to coffe extra's like suger, milk , by quntity and more
## decorator perpose is to "wrap" extra varibles to the main class in this case coffee


## abstart func
    def get_cost(self):
        pass
## abstart func
    def get_ingredients(self):
        pass

    def get_tax(self):
        return 0.1 * self.get_cost()


class Concrete_Coffee(Abstract_Coffee):

    def get_cost(self):
        return 1.00

    def get_ingredients(self):
        return 'coffee'


##decorator class
##in python ur able to warp functiom in function
class Abstract_Coffee_Decorator(Abstract_Coffee):

    ##geting the decorated_coffee from child
    def __init__(self, decorated_coffee):
        self.decorated_coffee = decorated_coffee

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients()


##Sugar Wrap (adding Sugar)
class Sugar(Abstract_Coffee_Decorator):

    #send the decorated coffee and Wrap the Sugar
    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost()

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', sugar'


##wrap Milk(adding Milk)
class Milk(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.25

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', milk'


##wrap Valnila(add vanilla)
class Vanilla(Abstract_Coffee_Decorator):

    def __init__(self, decorated_coffee):
        Abstract_Coffee_Decorator.__init__(self, decorated_coffee)

    def get_cost(self):
        return self.decorated_coffee.get_cost() + 0.75

    def get_ingredients(self):
        return self.decorated_coffee.get_ingredients() + ', vanilla'

##just coffee
myCoffee = Concrete_Coffee()
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
##cofffe++ Milk
myCoffee = Milk(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
## coffe + Mile +vanilla
myCoffee = Vanilla(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
## coffee + milk + vanilla +sugar
myCoffee = Sugar(myCoffee)
print('Ingredients: '+myCoffee.get_ingredients()+
   '; Cost: '+str(myCoffee.get_cost())+'; sales tax = '+str(myCoffee.get_tax()))
