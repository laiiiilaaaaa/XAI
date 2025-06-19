from Chef import Chef

class ChineseChef(Chef):
    def __init__(self, chicken_name, salad_name, dish_name, rice_name):
       super().__init__(chicken_name, salad_name, dish_name)
       self.rice_name = rice_name

    def make_rice(self):
        print("Chef is making a " + self.rice_name + " rice")