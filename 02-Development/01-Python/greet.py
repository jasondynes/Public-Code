# Review:
# Create a function called greet().
# Write 3 print statements inside the function.
# Call the greet() function and run your code.

def greet(name, location):
    print("Hello " + name)
    print("How are you doing " + name)
    # using f string alternative syntax
    print(f"Glad you are ok {name}")
    print(f"I understand you live in {location}")

# parameters passed as positional arguments
greet("Jason", "London")

# same parameters passed as Keyword Arguments and out of order
greet(location="Hitchin", name="Ethan")
