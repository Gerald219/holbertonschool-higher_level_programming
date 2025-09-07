#!/usr/bin/python3

# prints all possible different combinations of two digits
for i in range(0, 10):
    # only print unique, ascending combinations
    # and automatically skip reversed duplicates
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print("{}{}".format(i, j))
        else:
            print(
                "{}{}".format(i, j),
                end=", "
            )
