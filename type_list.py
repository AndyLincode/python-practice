class TypeList:
    def __init__(self, example_element, initial_list):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument must be a list.")
        for element in initial_list:
            self.__check(element)
        self.element = initial_list[:]  # copy by value

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempting to add an element of incorrect type")
