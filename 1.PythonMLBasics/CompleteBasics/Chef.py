class Chef:

    def __init__(self, chicken_name, salad_name, dish_name):
        self.chicken_name = chicken_name
        self.salad_name = salad_name
        self.dish_name = dish_name

    def make_chicken(self):
        print("Chef is making a " + self.chicken_name + " chicken")

    def make_salad(self):
        print("Chef is making a " + self.salad_name + " salad")

    def make_special_dish(self):
        print("Chef is making a " + self.dish_name + " special dish")