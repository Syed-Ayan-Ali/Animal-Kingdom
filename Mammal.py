from Animal import Animal
    
class Mammal(Animal):
    def __init__(self):
        super().__init__()
        self.has_eggs = False

    