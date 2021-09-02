print("FizzBuzz".center(75, "="))

# fizzbuzz = int(input("Input Angka : "))

fizzbuzz = int(input("Input Angka : "))
#hasil = 1
for number in range(1, fizzbuzz):
    hasil = number
    if number % 3 == 0 and number % 5 == 0:
        hasil = "fizzbuzz"
    elif number % 3 == 0:
        hasil = "fizz"
    elif number % 5 == 0:
        hasil = "buzz"
    print(hasil)
