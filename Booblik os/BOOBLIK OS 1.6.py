import time
import os
import tkinter as tk

print("СТАРТ ОС")
time.sleep(1)
print("▢")
time.sleep(1)
print("▢▢")
time.sleep(1)
print("▢▢▢")
time.sleep(1)
print("▢▢▢▢")
time.sleep(1)
ram1 = "128gb"
rom1 = "1tb"
print("RAM:" + ram1)
print("ROM:" + rom1)
time.sleep(1)
print("--------------")
print("напишите инфа")
print("--------------")
while True:
	command1 = input("веддите команду>")
	if command1 == "система":
		print("-------------------------------")
		print("BOOBLIK OS 1.0")
		print("v 1.0")
		print("realis version")
		print("видеокарта RTX4090 TI")
		print("процесор INTEL CORE I9 13900KF)")
		print("-------------------------------")
	if command1 == "калькулятор":
		calc1 = float (input("ведите 1 число "))
		calc2 = float (input("ведите 2 число "))
		calc3 = input("что хотите сделать(+,-,/,*): ")
		if calc3 == "+":
		   answer1 = (calc1 + calc2)
		   print(str(answer1))
		   print("решено")
		if calc3 == "-":
		   answer1 = (calc1 - calc2)
		   print(str(answer1))
		   print("решено")
		if calc3 == "/":
		   answer1 = (calc1 / calc2)
		   print(str(answer1))
		   print("решено")
		if calc3 == "*":
		   answer1 = (calc1 * calc2)
		   print(str(answer1))
		   print("решено")
	if command1 == "выход":
		q-exit
	if command1 == "сайт":
		os.system("start "+"link.py")
	if command1 == "Handy":
		os.system("start "+"Handy.py")
	if command1 == "игра":
		os.system("start "+"zmeyka.py")
	if command1 == "инфа":
		print("-----------------")
		print("выход")
		print("калькулятор")
		print("система")
		print("сайт")
		print("Handy(инет)")
		print("игра (змейка)")
		print("-----------------")