from random import random


class Reactor:

    fuel_bundles = []

    def __init__(self):
        # x, y position ranging from 0 to 1

        # create control rods

        # create fuel bundles
        max_width = 24
        for x in range(round(max_width*1.273)):
            for y in range(round(max_width*1.273)):
                for z in range(1):
                    x_pos = x / max_width
                    y_pos = y / max_width
                    z_pos = z
                    fuel = random()

                    x_center_dist = x_pos - 0.5
                    y_center_dist = x_pos - 0.5
                    if pow(x_center_dist, 2) + pow(y_center_dist, 2) > 0.25:
                        continue

                    self.fuel_bundles.append(FuelBundle(x_pos, y_pos, z_pos, fuel))


class FuelBundle:
    fuel = 1
    iodine = 0
    xenon = 0
    x = 0
    y = 0
    z = 0
    rod_sections = {}

    def __init__(self, x: float, y: float, z: float, fuel: float):
        self.x = x
        self.y = y
        self.z = z
        self.fuel = fuel

class ControlRod:
    sections = []
    coords = (0, 0, 0)
    delta_z = 0
    insertion = 1.0

    def __init__(self, rod_begin_coords: tuple, rod_end_coords: tuple, num_of_sections: int):
        self.coords = rod_begin_coords

        for i in range(num_of_sections):
            delta_x = i * (rod_end_coords[0] - rod_begin_coords[0]) / num_of_sections
            delta_y = i * (rod_end_coords[1] - rod_begin_coords[1]) / num_of_sections
            delta_z = i * (rod_end_coords[2] - rod_begin_coords[2]) / num_of_sections

            section_coords = (
                rod_begin_coords[0] + delta_x,
                rod_begin_coords[1] + delta_y,
                rod_begin_coords[2] + delta_z,
            )

            section = ControlRodSection(section_coords)
            self.sections.append(section)

    def set_insertion(self, insertion: float):
        section_capacity = 1 / len(self.sections)

        for section in self.sections:
            if insertion >= section_capacity:
                section.insertion = 1
                insertion -= section_capacity
            else:
                section.insertion = insertion / section_capacity  # Partially fill
                insertion = 0.0  # Remaining insertion used up

class ControlRodSection:

    coord = (0, 0, 0)
    insertion = 1

    def __init__(self, coord: tuple):
        self.coord = coord