#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = []
    for j in range(list_length):
        try:
            answer = my_list_1[j] / my_list_2[j]
        except TypeError:
            answer = 0
            print("wrong type")
        except IndexError:
            answer = 0
            print("out of range")
        except ZeroDivisionError:
            answer = 0
            print("division by 0")
        finally:
            result.append(ans)

    return result
