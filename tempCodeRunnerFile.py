ef string_length(s):
    print("String_length : got called with arguments ", s)
    return len(s)

def int_length(i):
    print("intLength : got called wth argument")
    return string_length(str(i))


def get_length_of_elements(t):
    return length_of_elements_iterator_factory(t)


class length_of_elements_iterator_factory:
    def __init__(self, t):
        self.t = t
        self.index = 0

    def __iter__(self):
        # Reset index to allow re-iteration if needed
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.t):
            raise StopIteration
        elem = self.t[self.index]
        self.index += 1

        if isinstance(elem, int):
            return int_length(elem)
        if isinstance(elem, str):
            return string_length(elem)
        # Fallback for other types (e.g., float)
        return string_length(str(elem))


a = (10, 20, "good", 2.33, "Ujjain is the city of gods")
b = get_length_of_elements(a)
print()
print("Called Length of elements")
for i in b:
    print(i)

print(string_length("Great"))
print(int_length(3030))