while True:
    tmp = input()
    if tmp == "0":
        break
    if tmp == tmp[::-1]:
        print("yes")
    else:
        print("no")