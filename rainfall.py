
movies = {
    "Avatar": 300,
    "Titanic": 250,
    "Avengers": 350
}

while True:

    print("\nAvailable Movies:")
    for movie, price in movies.items():
        print(movie, "- Rs.", price)

    choice = input("\nEnter movie name (or exit): ")

    if choice.lower() == "exit":
        print("Thank you for visiting!")
        break

    if choice not in movies:
        print("Movie not available!")
        continue

    quantity = int(input("Enter number of tickets: "))

    if quantity <= 0:
        print("Please enter a valid ticket quantity.")
        continue

    price = movies[choice]
    total = price * quantity

    if quantity >= 3:
        discount = total * 0.10
    else:
        discount = 0

    final_amount = total - discount

    print("\nBooking Summary")
    print("Movie:", choice)
    print("Tickets:", quantity)
    print("Total price: Rs.", total)
    print("Discount: Rs.", discount)
    print("Final amount: Rs.", final_amount)
