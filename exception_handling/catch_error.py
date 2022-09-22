def div(a, b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Can not divide by 0")
    except TypeError:
        print("Plese input a valid integer or float, not a string!")


print(div(10, 5))
print(div(25, 0))
print(div(35, 7))
print(div("100", 8))
