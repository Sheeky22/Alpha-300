x=-5
# if x<0:
#     raise Exception("X should be positive")

# assert instead of if

# assert(x>0),"X should be positive"

# try:
#     x=6/0
# # except Exception as e:
# #     print(e)
# except ZeroDivisionError:
#     print("Number can't be divied by 0!")
# else:
#     print("Eveyerhitn is fine!")
# finally:
#     print("Clean Up")

# class ValueTooHighError(Exception):
#     pass

# class ValueTooSmallError(Exception):
#     def __init__(self,message,value):
#         self.message=message
#         self.value=value

# def check(x):
#     if x>100:
#         raise ValueTooHighError("Value Too High")
#     if x<5:
#         raise ValueTooSmallError("Value Too Small",x)

# try:
#     check(4)
# except Exception as e:
#     print(e.message, e.value)