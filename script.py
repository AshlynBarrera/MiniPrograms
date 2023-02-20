
# 2/20/23 Ashlyn Barrera, 4.3 ExerciseB 
import random
import math
#MINI PROGRAM ONE
#Str input
print("Welcome to Divisible!")
name = input('\nPlease enter your name:  ');

#Int input one
intOne = int(input("\nHello " + name + " enter a number."));

#Int input two 
intTwo = int(input("\nHello " + name + " enter another number."));

even = "\n Your inputs sum are even "
odd = "\n Your inputs sum are odd "

if (intOne % intTwo == 0): 
   print("\n" + even);
else:
    print("\n" + odd)


#MINI PROGRAM Two

print("\nWelcome to Geometry")

DecOne = float(input("\n " + name + " enter a small decimal number: "));

DecTwo = float(input("\n " + name + " enter a big decimal number: "));

radius = float(random.uniform(DecOne, DecTwo));
print(radius)

volume = (4/3)*math.pi*radius**3
print(volume)

print ("The volume of a sphere with a radius" + str(radius) + " is : " + str(volume))


print("\n Quiz, enter true or false")


q1 = input("\n Is the sky blue?: ")

if( q1 == "true"):
    print("\nCorrect");
elif(q1 == "false"):
    print('\nSorry try again');
else:
    print("\nInvalid Input " + name );

