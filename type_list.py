class TypeList(list):
    def __init__(self, example_element, initial_list):
        self.type = type(example_element)
        if not isinstance(initial_list, list):
            raise TypeError("Second argument must be a list.")
        for element in initial_list:
            self.__check(element)

        super().__init__(initial_list)

    def __check(self, element):
        if type(element) != self.type:
            raise TypeError("Attempting to add an element of incorrect type")

    def __setitem__(self, i, element):
        self.__check(element)
        super().__setitem__(i, element)

    def __getitem__(self, i):
        return super().__getitem__(i)


x = TypeList('', ["foo", "bar", "baz"])
print(x)

y = TypeList('', [''] * 5)
y[3] = "1"
y[4] = "Hi"
print(y)

print(x + y)

# ['foo', 'bar', 'baz']
# ['', '', '', '1', 'Hi']
# ['foo', 'bar', 'baz', '', '', '', '1', 'Hi']
