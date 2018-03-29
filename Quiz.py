print("Who was the Founder of github?")
answer = input()

if answer == "Tom Preston":
	print(" :) ")
else:
	print(" :( ")

print("Thank you for playing!")


print('''
Q1 - Who was the Founder of github?
a - Tom Preston
b - Sundar pichai
c - satya nadela
''')
answer = input().lower()

if answer == "a":
	print("Yes,you are absolutely correct.")
elif answer == "b":
	print("Wrong,He is the current CEO of google.")
elif answer == "c":
	print("Wrong,He is the current CEO of microsoft.")
else:
	print(" You didn't choose a, b or c :( ")
