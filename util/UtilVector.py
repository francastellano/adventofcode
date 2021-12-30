from util import UtilMatrix


class UtilVector:
    def __init__(self):

        self.from_x = None
        self.from_y = None

        self.to_x = None
        self.to_y = None

        self.vector_type = None

    def get_vector_type(self):
        if self.from_x == self.to_x:
            self.vector_type = "Vertical"
        elif self.from_y == self.to_y:
            self.vector_type = "Horizontal"
        else:
            self.vector_type = "Oblique"

    def iterate_vector(self):

        if self.vector_type is None:
            self.get_vector_type()

        points = {}

        if self.vector_type == "Vertical":

            point_for = min (self.from_y, self.to_y)
            point_to = max (self.from_y, self.to_y)

            for point_y in range(point_for, point_to + 1):
                points = UtilMatrix.set_value_matrix (points, self.from_x, point_y, True)

        if self.vector_type == "Horizontal":
            point_for = min (self.from_x, self.to_x)
            point_to = max (self.from_x, self.to_x)

            for point_x in range(point_for, point_to + 1):
                points = UtilMatrix.set_value_matrix (points, point_x, self.from_y, True)

        if self.vector_type == "Oblique":

            if self.from_x < self.to_x:
                point_for_x = self.from_x
                point_to_x = self.to_x

                point_for_y = self.from_y
                if self.from_y > self.to_y:
                    var = -1
                else:
                    var = 1
            else:
                point_for_x = self.to_x
                point_to_x = self.from_x

                point_for_y = self.to_y
                if self.to_y > self.from_y:
                    var = -1
                else:
                    var = 1

            for point_x in range(point_for_x, point_to_x + 1):
                points = UtilMatrix.set_value_matrix (points, point_x, point_for_y, True)

                point_for_y = point_for_y + var

        return points
