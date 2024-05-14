import random

def generate_random_requests(filename, num_requests=1000, max_cylinder=4999):
    with open(filename, 'w') as file:
        for _ in range(num_requests):
            request = random.randint(0, max_cylinder)
            file.write(f"{request}\n")

if __name__ == "__main__":
    generate_random_requests("requests.txt")
