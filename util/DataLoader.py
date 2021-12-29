

class DataFile:
    def __init__(self, path_file=None):
        self.path = path_file
        self.list = []

    @staticmethod
    def clean_line(value):
        value = value.replace("\n", "")
        return value

    def load_basic_list (self, transform_to_int = False):
        with open(self.path) as f:
            lines = f.readlines()

        for line in lines:
            value = self.clean_line(line)
            value = int(value)
            self.list.append(value)

    def load_basic_number_list(self):
        self.load_basic_list(True)