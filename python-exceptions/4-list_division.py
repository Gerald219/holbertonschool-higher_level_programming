#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    new_list = []  # store results
    for i in range(list_length):  # loop through positions
        result = 0  # default value
        try:
            result = my_list_1[i] / my_list_2[i]  # divide items
        except ZeroDivisionError:  # if divisor is 0
            print("division by 0")
        except (TypeError, ValueError):  # if the items not numbers
            print("wrong type")
        except IndexError:  # if index not in list
            print("out of range")
        finally:
            new_list.append(result)  # save result
    return new_list  # list of results
