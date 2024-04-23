#
# #with parameters/args  without return type
# def fan(a,b):
#
#     print( a+b )
# fan(20,30)
#
# #with parameter/args with return type
# def fan1(a,b):
#
#     return( a+b )
# print(fan1(30,40))
#
#
# # without parameters/args without return type
# a=40
# b=30
# def fan2():
#     print( a+b )
# fan2()
#
# #without para/args with return type
# a=40
# b=30
# def fan2():
#     return( a+b )
# print(fan2())


# add,sub,mul,div,exp,fd
#without parameter with return type
# b=int(input("enter a number"))
# c=int(input("enter a number"))
# def demo():
#     return b+c,b-c,b*c,b/c
# print(demo())

# def even():
#     a = int(input("enter number"))
#     for i in range(a):
#         if i % 2==0:
#             print(i)
# even()
#
#
# def odd():
#     for i in range(a):
#         if i % 2==1:
#             print(i)
# odd()

# def prime():
#     a=int(input("enter a number"))
#     for i in range(10):
#         if i%2==1:
#             print(i)
# prime()


n=int(input("enter number"))
def fact():
    f = 1
while n>1:
    f = 1
    f*=n
n-=1
print("fatorial number",f)





