# Program 76: Sort dictionary by values

data = {"a": 50, "b": 20, "c": 40, "d": 10}

sorted_data = dict(sorted(data.items(), key=lambda item: item[1]))

print("Sorted dictionary by value:", sorted_data)
