

class Tank:
    # represents a tank, mostly used for pressure
    input: bool
    output: bool
    pump: Pump

    max_volume: float # volume of the tank (cubic meters)
    volume: float # volume of water currently in the tank (cubic meters)
    max_height: float # height of the top of the tank (meters)
    min_height: float # height of the bottom of the tank (meters)
    level: float # relative height of water in the tank
    pressure: float # pressure created by the water height

    def tick(self):
        self.level = self.volume / self.max_volume * (self.max_height - self.min_height)
        self.pressure = (self.level + self.min_height) * 10

    pass

class MagicTank:

    pressure: float

class Pipe:
    # a simple pipe, part of the PipeManager
    class Pump:
        # creates differential pressure
        pass

    # calculate own diff pressure

    pass


class PipeManager:
    
    tanks: list
    atmosphere: MagicTank

    def tick(self):
        for i in range(len(self.tanks)):
            j = i
            while j < len(self.tanks):
                # flow for every tank combination



    pass
