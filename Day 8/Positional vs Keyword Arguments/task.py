# # Functions with input
#
# def greet_with_name(name):
#     print(f"Hello {name}")
#     print(f"How do you do {name}?")
#
#
# greet_with_name("Jack Bauer")



###FUNCTIONS WITH MULTIPLE INPUTS###
def greet_with(name, location):
    print(f"Hello {name}! Nice weather in {location} right?")

greet_with(input("Please enter your name\n"), input("Please enter your location\n"))



###KEYWORD ARGUMENTS###
def greet_with(name, location):
    print(f"Hello {name}! Nice weather in {location} right?")

greet_with(location="Veghel", name="Zakariya")

