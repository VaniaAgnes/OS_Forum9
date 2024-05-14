import sys
import random

def read_requests(file_path):
    with open(file_path, 'r') as file:
        requests = [int(line.strip()) for line in file.readlines()]
    return requests

def calculate_head_movements(requests, initial_position):
    current_position = initial_position
    total_movements = 0
    for request in requests:
        total_movements += abs(current_position - request)
        current_position = request
    return total_movements

def fcfs(requests, initial_position):
    return calculate_head_movements(requests, initial_position)

def scan(requests, initial_position, max_cylinder):
    requests.sort()
    current_position = initial_position
    total_movements = 0

    left = [request for request in requests if request < initial_position]
    right = [request for request in requests if request >= initial_position]

    for request in right:
        total_movements += abs(current_position - request)
        current_position = request

    if left:
        total_movements += abs(current_position - 0)
        current_position = 0

        for request in reversed(left):
            total_movements += abs(current_position - request)
            current_position = request

    return total_movements

def c_scan(requests, initial_position, max_cylinder):
    requests.sort()
    current_position = initial_position
    total_movements = 0

    right = [request for request in requests if request >= initial_position]
    left = [request for request in requests if request < initial_position]

    for request in right:
        total_movements += abs(current_position - request)
        current_position = request

    if left:
        total_movements += abs(current_position - max_cylinder)
        total_movements += abs(max_cylinder - 0)
        current_position = 0

        for request in left:
            total_movements += abs(current_position - request)
            current_position = request

    return total_movements

def main():
    if len(sys.argv) != 3:
        print("Usage: python disk_scheduling.py <initial_position> <file_path>")
        return

    initial_position = int(sys.argv[1])
    file_path = sys.argv[2]
    max_cylinder = 5000

    requests = read_requests(file_path)

    # Task 1: Service the requests as they appear in the file
    fcfs_movements = fcfs(requests, initial_position)
    scan_movements = scan(requests, initial_position, max_cylinder)
    c_scan_movements = c_scan(requests, initial_position, max_cylinder)
    
    print("Task 1: ")

    print("FCFS (original result):", fcfs_movements)
    print("SCAN (original result):", scan_movements)
    print("C-SCAN (original result):", c_scan_movements)

    
    requests.sort()
    fcfs_movements_optimized = fcfs(requests, initial_position)
    
    # Split requests into two halves for Task 2
    mid_index = len(requests) // 2
    first_half = requests[:mid_index]
    second_half = requests[mid_index:]
    
    scan_movements_optimized = scan(first_half, initial_position, max_cylinder)
    c_scan_movements_optimized = c_scan(second_half, initial_position, max_cylinder)

    print("Task 2: ")
    print("FCFS (optimized result):", fcfs_movements_optimized)
    print("SCAN (optimized result):", scan_movements_optimized)
    print("C-SCAN (optimized result):", c_scan_movements_optimized)

if __name__ == "__main__":
    main()
