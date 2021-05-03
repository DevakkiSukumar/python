print("\nStudent Marks")
name=(input("\tEnter the student name :"))
print("\nEnter the Marks")
t=int(input("\tEnter the Tamil :"))
e=int(input("\tEnter the English :"))
m=int(input("\tEnter the Maths :"))
s=int(input("\tEnter the Science :"))
ss=int(input("\tEnter the Social Science :"))
sum=t+e+m+s+ss
a=sum/5
print("\n\tStudent Name :",name)
print("\tTotal of Marks :",sum)
print("\tAverage of Marks :",a)