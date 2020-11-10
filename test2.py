# Labsheet 4a
def three_copies():
    myin = str(input())
    i = 0

    while i < 3:
      print(myin, end = "")
      i = i + 1
    print()

def n_copies():
    mystring = str(input())
    i = 0
    myint = int(input())

    while i < myint:
      print(mystring, end = "")
      i = i + 1
    print()

three_copies()
n_copies()
