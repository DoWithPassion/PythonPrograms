#Python program
def pretty_print(num):
    def print_line(n):
        low = abs(n)
        print(' '.join(str(max(low + 1, abs(i) + 1)) for i in range(-num + 1, num)))

    for i in range(-num + 1, num):
        print_line(i)
