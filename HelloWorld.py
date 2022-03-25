print("Hello world!")


class Human:

    def __init__(self, name, age, is_male=True):
        self.name = name
        self.age = age
        self.is_male = is_male
    
    def __str__(self):
        return "Human<name={}, age={}, is_male={}>".format(
            self.name,
            self.age,
            self.is_male
        )

prerit = Human("Prerit Dayal", 22)
print(prerit)