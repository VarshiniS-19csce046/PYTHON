name=[str(letter) for letter in input ("Enter names:").split()]
age=[int(num) for num in input("Enter ages:").split()]
while(1):
	x=int(input("Enter 1 to continue:"))
	if(x==1):
		choice=int(input("1.Append \n2.Insert \n3.Extend \n4.Remove \n5.Pop \n6.Reverse \n7.Length \n8.Minimum \n9.Maximum \n10.Count \n11.Sort \n12.Index \n13.Datatype \n14.Concatenation \n15.Multiplication \nChoice:"))
		if(choice==1):
			option=int(input("Select option to append:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter name to add in the back of the name list:"))
				name.append(a)
				print(name)
			elif(option==2):
				b=int(input("Enter age to add in the back of the age list:"))
				age.append(b)
				print(age)
			else:
				print("Invalid Input")
		elif(choice==2):
			option=int(input("Select option to insert:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter name to be added:"))
				b=int(input("Enter position number to add the name:"))
				name.insert(b,a)
				print(name)
			elif(option==2):
				a=int(input("Enter age to be added:"))
				b=int(input("Enter position to add the age:"))
				age.insert(b,a)
				print(age)
			else:
				print("Invalid Input")
		elif(choice==3):
			option=int(input("Select option to extend:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter names to extend in the name list:"))
				name.extend(a)
				print(name)
			elif(option==2):
				b=int(input("Enter ages to extend in the the age list:"))
				age.extend(b)
				print(age)
			else:
				print("Invalid Input")
		elif(choice==4):
			option=int(input("Select option to remove:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter name to remove in the name list:"))
				name.remove(a)
				print(name)
			elif(option==2):
				b=int(input("Enter ages to remove in the the age list:"))
				age.remove(b)
				print(age)
			else:
				print("Invalid Input")
		elif(choice==5):
			option=int(input("Select option to pop:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=int(input("Enter position number to pop in the name list:"))
				name.pop(a)
				print(name)
			elif(option==2):
				b=int(input("Enter position number to pop in the age list:"))
				name.pop(b)
				print(age)
			else:
				print("Invalid Input")
		elif(choice==6):
			name.reverse()
			print(name)
			age.reverse()
			print(age)
		elif(choice==7):
			print(len(name))
			print(len(age))
		elif(choice==8):
			print(min(age))
		elif(choice==9):
			print(max(age))
		elif(choice==10):
			option=int(input("Select option to count:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter name to count in the name list:"))
				print(name.count(a))
			elif(option==2):
				b=int(input("Enter ages to count in the the age list:"))
				print(name.count(b))
			else:
				print("Invalid Input")
		elif(choice==11):
			option=int(input("Select option to sort:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				name.sort()
				print(name)
			elif(option==2):
				age.sort()
				print(age)
			else:
				print("Invalid Input")
		elif(choice==12):
			option=int(input("Select option to index- to find the position:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=str(input("Enter name to find the position in the name list:"))
				print(name.index(a))
			elif(option==2):
				b=int(input("Enter ages to find the position in the the age list:"))
				print(age.index(b))
			else:
				print("Invalid Input")
		elif(choice==13):
			print(type(name))
			print(type(age))
		elif(choice==14):
			add=name+age
			print(add)
		elif(choice==15):
			option=int(input("Select option to Multiply:\n1.Name\n2.Age\nOption:"))
			if(option==1):
				a=int(input("How many times you wish to display names in the name list:"))
				print(name*a)
			elif(option==2):
				b=int(input("How many times you wish to display ages in the age list:"))
				print(age*b)
			else:
				print("Invalid Input")
		else:
			print("Invalid Input")
	else:
		break
