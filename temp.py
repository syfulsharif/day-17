import builtins

# print(dir(builtins))

builtins_array = dir(builtins)

for item in builtins_array:
    if item == "webbrowser":
        print("webrowser found")
    else:
        print("Not found")
