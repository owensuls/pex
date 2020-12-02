# See https://adventofcode.com/2020
valid = 0

f=open("aoc_2_1.txt", "r")
#f=open("tmp.txt", "r")

f1 = f.readlines()
for s in f1:
    pos_1_match = 0
    pos_2_match = 0

    mylist = s.split()
    policy_list = mylist[0].split("-")
    policy_pos_1 = int(policy_list[0])
    policy_pos_2 = int(policy_list[1])

    policy_char = mylist[1].strip(":")
    password = mylist[2]

    '''
    print("Policy_char: ", policy_char)
    print("policy_pos_1: ", policy_pos_1)
    print("policy_pos_2: ", policy_pos_2)
    print()
    a = input()
    '''

    if(password[policy_pos_1 - 1] == policy_char):
        pos_1_match = 1

    if(password[policy_pos_2 - 1] == policy_char):
        pos_2_match = 1

    if((pos_1_match + pos_2_match) == 1):
        valid = valid + 1

print("Number of valid passwords: ", valid)
