import inspect
def pfi(string):
    while True:
        try:
            return int(input(string))
        except:
            print("sorry an error occoured\n Please type an integer");

#####main

#x = pfi("Please type an integer: ");

#print(x);

x = pfi("first integer to mulitpy:")
y = pfi("Second number: ")
print("Your value is:" +  str(x*y))
