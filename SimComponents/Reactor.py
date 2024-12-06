import SimManager


class Reactor:

    sim_state: dict
    reactor_state: dict
    id: int


    def __init__(self, manager: SimManager, id: int):
        # create dict entry
        self.id = id
        
    def init_subcomponents(self):
        pass

    def tick(self, delta: float):
        # run subcomponents and itself
        pass

class SimPoint:
    pass

class SuperFuelChannel:
    # this class represents a parent of a group of fuel channels outputting to the same steam generator
    # used for calculating the water temp raise and water flow
    pass

class FuelChannel:
    pass

class FuelBundle:
    pass

class ControlRod:
    pass

class ControLRodSection:
    pass