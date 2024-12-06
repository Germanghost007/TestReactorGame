import copy
from time import time, sleep

class SimManager:

    ticks_per_second: float

    next_frame = {}
    current_frame = {}

    tickables = []

    delta: float

    def __init__(self, tps: int):
        self.ticks_per_second = 1 / tps

    def init_simulation(self):
        # save components
        pass

    def sim_step(self, delta: float):
        for tickable in self.tickables:
            try:
                tickable.tick(delta)
            except:
                pass

        self.current_frame = copy.deepcopy(self.next_frame)

    def game_loop(self):
        simRunning = True

        while(simRunning):
            frame_start = time()
            self.sim_step(self.delta)
            self.delta = time() - frame_start
            sleep(self.delta)
        