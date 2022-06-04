import random


x = int(input("Enter the number of keywords you want"))
i = 1
pass_list = []
for i in range(x):
    inp = input("Enter your keyword")
    if i % 2 == 0:
        inp = inp.lower()
        pass_list.append(inp)
    else:
        inp = inp.upper()
        pass_list.append(inp)

num = random.randint(1, 100100)
num2 = random.randint(69,420)
num = str(num)
num2 = str(num2)
pass_list.append(num)
pass_list.append(num2)
rand_list = random.choice(['!', '#', '$', '%', '^', '&', '*', '?',  '+', '/', ':', ';', '<', '>','|'])
rand_list2 = random.choice(['!', '#', '$', '%', '^', '&', '*', '?',  '+', '/', ':', ';', '<', '>','|'])
email_list = random.choice(['@gmail.com', '@yahoo.com', '@hotmail.com', '@aol.com','@live.com', '@rediffmail.com', '@free.fr','@msn.com', '@wanadoo.com'])
pass_list.extend(rand_list)
pass_list.extend(rand_list2)
pass_list.extend(email_list)

c = " "

for n in range(len(pass_list)):
    c = c + pass_list[n]

print("Your fresh new email is:", c)
