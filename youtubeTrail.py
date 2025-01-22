# while True:
#     print("who are you ?")
#     name = input ("name:")
#     if name == "joe":
#         continue
#     print("enter the password")
#     password = input("pass:")
#     if password == "abc":
#         break 
# print("access granted")

# import random 
# def randomnum(answer):
#     if answer == 1:
#         return("bad try")
#     elif answer == 2:
#         return("right guess")
#     elif answer == 3:
#         return("oops")
#     elif answer == 4:
#         return("try again")
#     elif answer == 5:
#         return("try again")
#     else:
#         return ("invalid")
    
# r = random.randint(1,5)
# print(r)
# number = randomnum(r)
# print(number)


# def student_marks():
#     tamil=int(input("enter the tamil marks:"))
#     english=int(input("enter the english marks:"))
#     maths=int(input("enter the maths marks:"))
#     science=int(input("enter the science marks:"))
#     social=int(input("enter the social marks:"))

#     total = [tamil,english,maths,science,social]
#     print(total)
#     marks=sum(total)
#     result =[]
#     for i in total:
#         if i <= 50:
#             result.append('failed')

#         else:
#             if sum(total) <= 250:
#                 result.append('failed')
#             else:   
#                 result.append('passed')
    
#     if "failed" in result:
#         print("HE IS Failed")
#     else:
#         print("HE IS Passed")

# student_marks()  