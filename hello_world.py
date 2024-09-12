def print_hello():
    print("Hello, World!")

def print_pibonacci():
    a, b, c = 0, 1, 1
    for _ in range(100):
        print(c)
        a = b
        b = c
        c = a + b

if __name__ == '__main__':
    print_pibonacci()
    print_hello()
