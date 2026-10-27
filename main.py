# Mandelbrot
# how to calculate it:
# z1 = z0 * z0 + c
# c is a special number. z1 is the result of the current step. z0 is the result of the last step
# z0 is always zero (0)



def calculate():
    c = float(input("Enter the number you want to calculate with: "))
    z0 = 0
    rounds = int(input("Enter the number of rounds (recommended: 20): "))
    critical_number = float(input("Enter the number where you want to stop (recommended: 2): "))

    for number in range(int(rounds)):
        z1 = z0 * z0 + c
        print(z1)
        if z1 > critical_number:
            print("Your number is greater than the critical number!")
            break
        else:
            z0 = z1

calculate()
