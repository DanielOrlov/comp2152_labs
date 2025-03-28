# Heart class for composition
class Heart:
    def __init__(self, bpm=72):
        self.__bpm = bpm
    
    @property
    def bpm(self):
        return self.__bpm
    
    @bpm.setter
    def bpm(self, bpm):
        self.__bpm = bpm

    def beat(self):
        print("Lub-dub")

    def __str__(self):
        return f"Heart is beating at {self.bpm} bpm), "