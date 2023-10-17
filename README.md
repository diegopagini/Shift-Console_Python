# Shift-Console_Python


## numbers
```python
def perfumery_numbers():
    for n in range(1, 1000):
        yield f"Pe - {n}"


def pharmacy_numbers():
    for n in range(1, 1000):
        yield f"Ph - {n}"


def cosmetic_numbers():
    for n in range(1, 1000):
        yield f"C - {n}"


perfumery = perfumery_numbers()
pharmacy = pharmacy_numbers()
cosmetic = cosmetic_numbers()


def decorator(category):
    print("\n" + "*" * 23)
    print("Your number is: ")
    if category == "PE":
        print(next(perfumery))
    elif category == "PH":
        print(next(pharmacy))
    else:
        print(next(cosmetic))

    print("Please wait and you will be attended")
    print("*" * 23 + "\n")



```

## shift-console
```python
import numbers


def ask_category():
    print("Wellcome to the Pharmacy Python")
    while True:
        print("[PE] - Perfumery\n[PH] - Pharmacy\n[C] - Cosmetic")
        try:
            my_category = input("Choose your category").upper()
            ["PE", "PH", "C"].index(my_category)
        except ValueError:
            print("That is not a valid option")
        else:
            break

    numbers.decorator(my_category)


def init():
    while True:
        ask_category()
        try:
            another_turn = input("Do you want another turn? [S] [N]: ").upper()
            ["S", "N"].index(another_turn)
        except ValueError:
            print("That is not a valid option")
        else:
            if another_turn == "N":
                print("Thank you for your visit")
                break


init()
```
