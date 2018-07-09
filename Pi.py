# Find PI to the Nth Digit
# Ask for user input for 'n' number of places
# Print out PI to the 'n'th digit


def calcPi(limit):  # Generator function
    """
    Prints out the number of decimal
    places of pi until the limit is reached
    """

    w, a, s, d, k, t = 1, 0, 1, 1, 3, 3

    decimal = limit
    counter = 0

    while counter != decimal + 1:
            if 4 * w + a - s < k * s:
                    # yield digit
                    yield k
                    # insert decimal point after first digit
                    if counter == 0:
                            yield '.'
                    # end
                    if decimal == counter:
                            print('')
                            break
                    counter += 1
                    ka = 10 * (a - k * s)
                    k = ((10 * (3 * w + a)) // s) - 10 * k
                    w *= 10
                    a = ka
            else:
                    ka = (2 * w + a) * t
                    kk = (w * (7 * d) + 2 + (a * t)) // (s * t)
                    w *= d
                    s *= t
                    t += 2
                    d += 1
                    k = kk
                    a = ka


def main():  # Wrapper function

    # Calls CalcPi with the given limit
    pi_digits = calcPi(int(input(
        "Enter the number of decimals to calculate to: ")))

    i = 0

    # Prints the output of calcPi generator function
    # Inserts a newline after every 40th number
    for d in pi_digits:
            print(d, end='')
            i += 1
            if i == 40:
                print("")
                i = 0

if __name__ == '__main__':
    main()