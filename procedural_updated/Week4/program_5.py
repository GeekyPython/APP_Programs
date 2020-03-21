gl = [21, 24, 12, 34, 10, 15, 41]
print("Given list:" , gl)

db4 = list(filter(lambda x: (x%4 == 0),gl))
print("Elements divisible by 4: ", db4)