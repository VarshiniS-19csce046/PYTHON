s1={7,8,4,10.2,"python",(1,2,3)}
s2=set([10,8,6,4,2,7])

print("s1 : ",s1)
print("s2 : ",s2,"\n")

print("         SET OPERATIONS        ")
print("---------------------------------")
print("\n1. print set elements \n2. datatype of t1 \n3. add an element to s1 \n4. update elements  \n5. discard \n6. remove \n7. clear s1 \n8. union of s1 and s2 \n9. intersection of s1 and s2 \n10. difference of s1 and s2 \n11. symmetric difference of s1 and s2 \n12. check  s2 is disjoint of s1 \n13. check  s2 is subset of s1 \n14. pop operation \n15. copy \n16. display elements in s1 using for loop \n17. display maximum value \n18. display minimum value \n19. sum of elements in set \n20. sort operation \n21. length of the set")

n=int(input("\nenter your choice : "))

if(n==1):
  print("s1 elements : ",s1)
  print("s1 elements : ",s2)
elif(n==2):
  print("datatype of s1 : ",type(s1))
  print("datatype of s2 : ",type(s2))
elif(n==3):
  e=str(input("enter a string element to be added to the s1 : "))
  s1.add(e)
  print(s1)
elif(n==4):
  s2.update([11,22,33,44,55])
  print("updated elements in s2 : ",s2)
elif(n==5):
  s2.discard(2)
  print("2 in s2 is discarded",s2)
elif(n==6):
  s2.remove(4)
  print("element 4 is removed from s2",s2)
elif(n==7):
  s1.clear()
  print("s1 is cleared : ",s1)
elif(n==8):
  print("Union of s1 and s2 : ",s1|s2)
elif(n==9):
  print("Intersection of s1 and s2 : ",s1&s2)
elif(n==10):
  print("difference of s1 and s2 : ",s1-s2)
elif(n==11):
  print("symmetric difference of s1 and s2 : ",s1^s2)
elif(n==12):
  print(" is s2 is disjoint of s1 ? :  ",s1.isdisjoint(s2))
elif(n==13):
  print("is s2 is superset of s1 ? : ",s1.issuperset(s2))
elif(n==14):
  v=s1.pop()
  print("poped element from s1 : ",v)
  print("s1 after poping a random element : ",s1)
elif(n==15):
  s3=s1.copy()
  print("s1 is copied to s3 : ",s3)
elif(n==16):
  print("elements in s1 : ")
  for i in set(s1):
    print(i)
elif(n==17):
  print("maximum value in s2 is : ",max(s2))
elif(n==18):
  print("minimum value in s2 is : ",min(s2))
elif(n==19):
  print("sum of elements in s2 : ",sum(s2))
elif(n==20):
  print("elements of s2 is sorted : ",sorted(s2))
elif(n==21):
  print("length of s1 is : ",len(s1))
else:
  print("Invalid number")
