"""Files tests simple file read related operations"""

class SimpleFile(object):
    """SimpleFile tests using file read api to do some simple math"""
    def __init__(self, file_path):
        self.numbers = []
        """
        TODO: reads the file by path and parse content into two
        dimension array (numbers)
        """
        with open(file_path) as f:
            temp = list(map(lambda n: n.split(), f.readlines()))
            self.numbers = [list(map(int, x)) for x in temp]

    def get_mean(self, line_number):
        """
        get_mean retrieves the mean value of the list by line_number (starts
        with zero)
        """
        sum = 0
        for i in self.numbers[line_number]:
            sum += i
        return sum/len(self.numbers[line_number])

    def get_max(self, line_number):
        """
        get_max retrieves the maximum value of the list by line_number (starts
        with zero)
        """
        max = self.numbers[line_number][0]
        for i in self.numbers[line_number]:
            if i > max:
                max = i
        return max

    def get_min(self, line_number):
        """
        get_min retrieves the minimum value of the list by line_number (starts
        with zero)
        """
        min = self.numbers[line_number][0]
        for i in self.numbers[line_number]:
            if i < min:
                min = i
        return min

    def get_sum(self, line_number):
        """
        get_sum retrieves the sumation of the list by line_number (starts with
        zero)
        """
        sum = 0
        for i in self.numbers[line_number]:
            sum += i
        return sum


