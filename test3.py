input = "A1B"

def myfunc(s):
    i = 0

    while i < len(s) and (s[i] < "0" or "9" < s[i]):
        i = i + 1
        print("i now equals: ", i)

myfunc(input)
