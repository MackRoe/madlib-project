
noun = input("Enter a noun: ")
adjective = input("Enter an adjective: ")
verb = input("Enter a verb: ")
adverb = input("Enter an adverb (word that modifies an adjective, usually ending in -ly):")
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

print(explicative + " they " + verb + "ed me " + first_number + " times!")
print(explicative + " they " + verb + "ed me " + second_number + " times!")
print(explicative + " they " + verb + "ed me " + third_number + " times!")
