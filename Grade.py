#WAP to accept percentage from the user and display the grade accordingly.
percentage=float(input(" Enter your percentage: "))
if percentage>90:
    print(" Your grade is 'A'.")
elif percentage>80 and percentage<=90:
    print(" Your grade is 'B'.")
elif percentage>=60 and percentage<=80:
    print(" Your grade is 'C'.")
elif percentage<60 and percentage>=33:
    print(" Your grade is 'D'.")
else:
    print(" Your are Fail")
input()    
   
