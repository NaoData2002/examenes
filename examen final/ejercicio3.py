import time

def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"La función {func.__name__} tardó {end_time - start_time:.6f} segundos en ejecutarse.")
        return result
    return wrapper

@timer_decorator
def multiply(*args, **kwargs):
    product = 1
    for arg in args:
        product *= arg
    for key, value in kwargs.items():
        product *= value
    return product

def main():
    print("Resultado: ", multiply(1, 2, 3, 4))
    print("Resultado: ", multiply(2, 3, a=5, b=7))
    print("Resultado: ", multiply(1, 2, 3, a=4, b=5, c=6))

if __name__ == "__main__":
    main()
