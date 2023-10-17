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


