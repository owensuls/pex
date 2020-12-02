# See https://adventofcode.com/2020
valid = 0

f=open("aoc_2_1.txt", "r")

f1 = f.readlines()
for s in f1:
    mylist = s.split()
    policy_list = mylist[0].split("-")
    policy_min = int(policy_list[0])
    policy_max = int(policy_list[1])

    policy_char = mylist[1].strip(":")
    password = mylist[2]

    found = password.count(policy_char)

    '''
    print("Policy_char: ", policy_char)
    print("Found: ", found)
    print("policy_min: ", policy_min)
    print("policy_max: ", policy_max)
    print()
    a = input()
    '''

    if((found >= policy_min) & (found <= policy_max)):
        valid = valid + 1
        #print("Valid")

print("Number of valid passwords: ", valid)
