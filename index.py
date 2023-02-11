# [x, y] = list(map(int, input().split())) # input the inputs
# nums = input()
# len1 = len(nums)
# answer = ""
# newArr = nums[len1: 1: -1]
# if int(nums) < 0:
#       newArr = nums[-1: -len1: -1]
#       answer += "-"
#       answer += newArr
# else:
#       answer += newArr

# answer = int(answer)
# print(answer, type(answer))

# [a, b] = [int (x) for x in input().split(" ")];


# -3
# 5
# -28
# -3
# 124
# -3
# 8
  
#[n, x, y] = [int (x) for x in input().split(" ")]

# str = "acb&*123^%hJK";
# count = 0;
# for i in range(len(str)+1):
#             count += 1;
# print(count);
"""
6
16
17
4
3
5
2
"""
""" [1,2,3,4,5,6,7], 3 inputs for function """


# def find_leaders(A):
#     leaders = []
#     for i in range(len(A)-1, -1, -1):
#         flag = 0
#         for j in range(i+1, len(A)):
#             if A[i] <= A[j]:
#                 flag = 1
#                 break
#         if flag == 0:
#             leaders.append(A[i])
#     for i in reversed (leaders):
#       print(i);

# n = int(input());
# A = [];
# for i in range(0, n):
#       A.append(int(input()));
# (find_leaders(A))







# list1 = [int(x) for x in input().split(" ")];
# n = int(input());
#


# def sum_of_multiples (list1, n):
#       sum = 0;
#       for i in range(len(list1)):
#             if(list1[i] % n == 0):
#               sum += list1[i];
#       return(sum);


# list1 = [int(x) for x in input().split(" ")];
# n = int(input());
# print(sum_of_multiples(list1, n));

# str = "aabbaabcncnn";
# mp = {};
# for i in str:
#       if(mp.get(i) == None):      #if mp doesnt have (i)
#             mp.update({i : 1});       # update mp with {i : 1} for i = element and 1 as initial count;
#       else:
#             count = mp.get(i);    #else count = mp.get = ({element : occurance value})
#             mp.update({i : count + 1});   #when element is present, update count with previous count + 1; 

# # print(mp)
# final_count = 0
# for value in mp.values():
#       if(value % 3 == 0):
#             final_count += 1;
# print(final_count);



# def count_elements(arr): #count ele's greater than all left elements
#     count = 1
#     max = arr[0]
#     for i in range(1, len(arr)):
#         if arr[i] > max:
#             count += 1
#             max = arr[i]
#     return count

# arr = [7,4,8,2,9]
# print(count_elements(arr))

str = input();
product = 1;
for i in str:
      product *= int(i);
print(product);

curtains = "aabbaaabbbbaa";