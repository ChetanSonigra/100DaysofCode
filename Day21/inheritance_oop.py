
class Animal:
    def __init__(self) -> None:
        self.num_eyes=2
        
    def breathe(self):
        print('Inhale, exhale')



class Fish(Animal):
    def __init__(self):
        super().__init__()
        
    def swim(self):
        print('Moving in water.')
        
    def breathe(self):                    # Method overriding.
        super().breathe()
        print('Under Water.')
        
fish=Fish()
fish.swim()
fish.breathe()