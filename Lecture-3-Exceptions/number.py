# Exception Handling
def main():
     x = get_int()
     print(f"x is {x}")

# while True makes the prgram to run in loop untill user enters a integer.
# when user enters integer the loop breaks and print function is executed.
def get_int():
    while True:
            try:
                return int(input("what's x? "))
            except ValueError:
               pass

main()