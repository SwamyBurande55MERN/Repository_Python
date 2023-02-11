# a1 = int(input())  #input
# a2 = int(input())  #input
# a3 = int(input())  #input
# d = (a2 - a1)      #common difference
n = int(input())
for i in range(1, n+1, 1):
      [x, y] = list(map(int, input().split()))
      if (x > 0 and y > 0):
            print("Q1")
      elif (x < 0 and y > 0):
            print("Q2")
      elif(x < 0 and y < 0):
            print("Q3")
      elif (x > 0 and y < 0):
            print("Q4")
