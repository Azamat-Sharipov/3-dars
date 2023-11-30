# # String Qoshtirnoqlar turlari...
# name = "Azamat"
# age = '16'
# adress = """Boston 18-uy"""
# adress1 = '''Boston 18-uy'''
# print(name, age, adress, adress1)
#
# # \n - Joy tashlash uchun...
# person = "name:Azamat \nage: 17 \nphone_number: 95 110 19 16"
# print(person)
#
# # \t - Tap vazifasini bajaradi... 4 ta spesga tueng
# person = "name:Azamat \tage: 17 \tphone_number: 95 110 19 16"
# print(person)
#
# # f"{O'ziga ozlashtirvoladi}" - Onson
# a = 16
# print(f"Men {a} yoshdaman")
#
# S = 6
# A = 7
# print(f"Gipatenuzzasi: {((S ** 2) + (A ** 2)) ** (1/2)} ga teng!")
#
# # Qiyinroq varyanti...
# age = 17
# print("Men: " + str(age) + " yoshdaman")
#
# name = input("Juft son kiriting: ")
# if name == "74":
#     print(f"Rahmat! {name}\nDostub berildi!")
#
# else:
#   print("Bu son juft emas!")




# name = input('Ism: ')
# surname = input('Familiya: ')
# age = int(input('Yosh: '))
#
# if name == "Azamat" and surname == "Sharipov" or age == 16:
#     print("Здраствуйте")
#
# else:
#     print("Ты не админстратор!")
#
#     name = input("ism: ")
#     username = input("familya: ")
#     age = int(input("yosh: "))
#
#     if name == "Azamat" and username == "Sharipov" and age == 17:
#         print("Salom: ")
#
#     else:
#         print("natogri: ")

# 1 - Task
# name = input("Juft son kiriting: ")
# if name == "12":
#     print("Rahmat😍")
#
#
# else:
#     print("Afsuski bu juft son emas😒")

# 2 - Task
name = input("Yoshingiz: ")
age = input("Sizning yoshingiz: ")
a = input("18 - yoshdan kattamisiz: ")
b = input("18 - yoshdan kichikmisiz: ")
if name == "62" and age == "2" and a == "Yoq" and "Yoq":
      print(f"Sizlar uchun muzeyga kiring bepul: {name}")
      print(f"Sizlar uchun muzeyga kirish bepul: {age}")
      print(f"Siz uchun tolov 100.000 bo'ladi!: {a}")
      print(f"Siz uchun tolov 300.000 bo'ladi!: {b}")

else:
    print(f"Agar yolg'on malumot bersangiz shitrafimiz bor!!!")

# else:
#     print(f"Agar yolg'on malumot bersangiz shitrafimiz bor: {a}")
#
# else:
#     print("Afsuski sizga mumkun emas!!!")