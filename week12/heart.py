# Heart class for composition
class Heart:
    def __init__(self, beats_per_minute=72):
        self.__beats_per_minute = beats_per_minute
    
    @property
    def beats_per_minute(self):
        return self.__beats_per_minute
    
    @beats_per_minute.setter
    def beats_per_minute(self, beats_per_minute):
        self.__beats_per_minute = beats_per_minute

    def beat(self):
        print("Lub-dub")

    def __str__(self):
        return f"Heart is beating at {self.beats_per_minute} bpm), "
    
    def __del__(self):
        print("Heart is deleted by a destructor")