# === Factory ===
class BurgerF:
    def __init__(self, name, ingredients):
        self.name = name
        self.ingredients = ingredients
        
    def print(self):
        print(f"One {self.name} with {self.ingredients} ready to be picked up!")
        
class BurgerFactory:
    def createCheeseBurger(self):
        ingredients = ["Cheese", "Patty", "Buns", "Lettuce", "Tomato"]
        return BurgerF("Cheeseburger", ingredients)
    
    def createDeluxeBurger(self):
        ingredients = ["Premium Cheese", "Double Patty", "Brioche Buns", "Romainne Lettuce", "Sliced Tomato"]
        return BurgerF("Deluxe Burger", ingredients)

    def createVeganBurger(self):
        ingredients = ["Tofu Patty", "Buns", "Lettuce", "Tomato"]   
        return BurgerF("Vegan Burger", ingredients)
    
burger_factory = BurgerFactory()
burger_factory.createCheeseBurger().print()
burger_factory.createDeluxeBurger().print()
burger_factory.createVeganBurger().print()

# === Builder ===
class BurgerB:
    def __init__(self):
        self.buns = None
        self.cheese = None
        self.patty = None
        
    def setCheese(self, cheese: str):
        self.cheese = cheese
        return self
    
    def setPatty(self, patty: str):
        self.patty = patty
        return self
    
    def setBuns(self, buns: str):
        self.buns = buns
        return self
    
    def print(self):
        print(f"One burger with {self.buns}, {self.cheese}, {self.patty} is ready to be picked up!")
    
class BurgerBuilder:
    def __init__(self):
        self.burger = BurgerB()
        
    def addCheese(self, cheese:str):
        self.burger.setCheese(cheese)
        return self
        
    def addBuns(self, buns:str):
        self.burger.setBuns(buns)
        return self
    
    def addPatty(self, patty:str):
        self.burger.setPatty(patty)
        return self  
         
    def build(self):
        return self.burger
    
burger_builder = BurgerBuilder().addPatty("Double patty").addBuns("Toasted buns").addCheese("Cheddar cheese").build().print()