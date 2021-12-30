from util import UtilMatrix


class UtilVector:
    def __init__(self):

        self.from_x = None
        self.from_y = None

        self.to_x = None
        self.to_y = None

        self.vector_type = None

    def reorder (self):
        if self.from_x > self.to_x:
            temp = self.from_x
            self.from_x = self.to_x
            self.to_x = temp

        if self.from_y > self.to_y:
            temp = self.from_y
            self.from_y = self.to_y
            self.to_y = temp

    def get_vector_type(self):
        if self.from_x == self.to_x:
            self.vector_type = "Vertical"
        elif self.from_y == self.to_y:
            self.vector_type = "Horizontal"
        else:
            self.vector_type = "Oblique"

    def iterate_vector(self):
        points = {}
        if self.vector_type == "Vertical":
            for point_y in range(self.from_y, self.to_y + 1):
                points = UtilMatrix.set_value_matrix (points, self.from_x, point_y, True)
                print (f"Point [{self.from_x}] [{point_y}]")

        if self.vector_type == "Horizontal":
            for point_x in range(self.from_x, self.to_x + 1):
                print (f"Point [{point_x}] [{self.from_y}]")

                points = UtilMatrix.set_value_matrix (points, point_x, self.from_y, True)

        if self.vector_type == "Oblique":
            var = self.from_y
            for point_x in range(self.from_x, self.to_x + 1):
                print(f"Point [{point_x}] [{var}]")

                points = UtilMatrix.set_value_matrix (points, point_x, var, True)

                var += 1

        return points
