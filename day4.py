def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


# ye function 1 se leke high tak ke prime numbers return karega as a list 
def generate_primes(low, high):
    primes = []
    for num in range(low, high + 1):
        if is_prime(num):
            primes.append(num)
    return primes



# saving primes to a file
def save_primes_to_file(prime_list, filename):
    # with automactically closes the file after the block is executed
    # opening file in write mode
    with open(filename, "w") as f:
        for p in prime_list:
            f.write(str(p) + "\n")


# Use karte hain
primes_1_to_100 = generate_primes(1, 100)
print("Primes between 1 and 100:", primes_1_to_100)


# Save in file
save_primes_to_file(primes_1_to_100, "primes_1_to_100.txt")
print("Prime numbers saved in file primes_1_to_100.txt")
