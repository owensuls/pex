#test_array = [1721,979,366,299,675,1456]
i = 0
j = 0
answer = 0

f=open("aoc_1.txt", "r")

f1 = f.readlines()
for i in f1:
  for j in f1:
    for k in f1:
      if((int(i)+int(j)+int(k)) == 2020):
        answer = int(i) * int(j) * int(k)

print("Answer is: ", answer)
