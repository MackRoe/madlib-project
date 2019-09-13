
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adverb = input(""" Enter an adverb (word that modifies an adjective,
usually ending in -ly):""")
proper_noun_place = input("Enter the name of a Place:")
first_number = input("Enter a number: ")
second_number = input("Enter another number: ")
third_number = input("Please enter one more number: ")
explicative = input("What do you say when something surprises you suddenly?: ")




#define madlibs to be filled
#madlibs = []
#madlibs.append("Test {}, {}, {}")
#test so far
#print(madlibs(0)).format(first_number, second_number, third_number)
#none of that worked right

madlibs_done = 0


print(explicative + " they " + verb + "ed me " + first_number + " times!")
print(explicative + " they " + verb + "ed me " + second_number + " times!")
print(explicative + " they " + verb + "ed me " + third_number + " times!")
print(" ")
do_another = input("Would you like to do another?")

if do_another == "yes":
    animal = input("Name an animal: ")
    color = input("Name a color: ")
    clothing = input("Something you wear: ")
    car = input("A type of vehicle: ")
    seat = input("Somewhere you sit: ")
    print(" ")
    print("I got the " + animal + "s in the back")
    print(animal + " tack is attached")
    print(noun + " is matte " + color)
    print("Got the " + clothing + " that's " + color + " to match")
    print("Ridin' on a " + animal + ", ha")
    print("You can whip your " + car)
    print("I been in the valley")
    print("You ain't been up off that " + seat + ", now")
    print(" ")
    print("THANK YOU FOR PLAYING")
else:
    print("Good bye")
