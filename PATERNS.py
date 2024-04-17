
# a=int(input("enter a number"))
# for i in range (a):
#     for j in range (a-i):
#
#         print("*",end=" ")
#     print()


# for i in range (5):
#     for j in range (7):
#         if(i==0 and j==3) or (i==1 and j in{2,4}) or (i==2 and j in {1,3,5})  or (i==3 and j in{0,2,4,6}):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()
# for i in range(5):
#     for j in range(7):
#         if(i==0 and j in{0,2,4,6}) or (i==1 and j in{1,3,5}) or (i==2 and j in{2,4}) or (i==3 and j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(5):
#     for j in range(1,5-i):
#         print(j,end=" ")
#     print()

# for i in range(5):
#     for j in range(1,5-i):
#         print(j+i,end=" ")
#     print()

# for i in range(5):
#     for j in range(1,i+1):
#         print(i+j-1,end=" ")
#     print()
#
# for i in range(4,8):
#     for j in range(8-i):
#         print(i+j,end=" ")
#     print()

# for i in range(7):
#     for j in range(7):
#         if(i==0 and j==3) or (i==1 and j in{2,4}) or (i==2 and j in{1,3,5}) or (i==3 and j in{0,2,4,6}) or (i==4 and j in{1,3,5}) or (i==5 and j in{2,4}) or (i==6 and j==3):
#             print("*",end=" ")
#         else:
#             print(" ",end=" ")
#     print()


# for i in range(5):
#     for j in range(5-i):
#         print(chr(65+j),end=" ")
#     print()

# for i in range(4):
#     for j in range(i+1):
#         print(chr(65+i+j),end=" ")
#     print()

# for i in range(7):
#     for j in range(7):
#         if(i==0 and j==2):
#             print(chr(65), end=" ")
#         elif(i==1 and j==1):
#             print(chr(66), end=" ")
#         elif (i == 1 and j==3):
#             print(chr(67), end=" ")
#         elif(i==2 and j==0):
#             print(chr(67), end=" ")
#         elif (i == 2 and j==2):
#             print(chr(68), end=" ")
#         elif (i == 2 and j==4):
#             print(chr(69), end=" ")
#         elif(i==3 and j==1):
#             print(chr(66),end=" ")
#         elif (i == 3 and j == 3):
#             print(chr(67),end=" ")
#         elif (i == 4 and j == 2):
#             print(chr(65), end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# for i in range(5):
#     for j in range(7):
#          if(i==0 and j==2):
#             print(chr(65), end=" ")
#          elif(i==1 and j==1):
#              print(chr(65),end=" ")
#          elif(i==2 and j==0):
#             print(chr(65), end=" ")
#          elif(i==2 and j==2):
#             print(chr(66), end=" ")
#          elif (i == 3 and j == 1):
#             print(chr(66), end=" ")
#          elif (i == 4 and j == 2):
#              print(chr(67), end=" ")
#          else:
#              print(" ",end=" ")
#     print()

for i in range(6):
     for j in range(10):
          if(i==0 and j==5) or (i==1 and j in{4,6}) or (i==2 and j in{3,5,7}) or (i==3 and j in{2,8}) or (i==4 and j in{1,9}):
             print('*', end="")
          else:
             print(" ",end="")
     print()




















