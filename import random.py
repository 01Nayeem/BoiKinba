import random

# Define the fitness function
def fitness_function(x):
    return x**2

# Generate a random initial solution
def generate_initial_solution(min_value, max_value):
    return random.uniform(min_value, max_value)

# Generate a neighbor solution by making a small change to the current solution
def generate_neighbor(current_solution, step_size, min_value, max_value):
    neighbor = current_solution + random.uniform(-step_size, step_size)
    return max(min(neighbor, max_value), min_value)

# Hill Climbing Algorithm
def hill_climbing(iterations, step_size, min_value, max_value):
    # Initialize the current solution
    current_solution = generate_initial_solution(min_value, max_value)
    current_fitness = fitness_function(current_solution)
    
    for iteration in range(iterations):
        # Generate a neighbor solution
        neighbor_solution = generate_neighbor(current_solution, step_size, min_value, max_value)
        neighbor_fitness = fitness_function(neighbor_solution)
        
        # If the neighbor solution is better, move to the neighbor
        if neighbor_fitness < current_fitness:
            current_solution = neighbor_solution
            current_fitness = neighbor_fitness
    
    return current_solution

# Parameters
iterations = 1000
step_size = 0.1
min_value = -10
max_value = 10

# Run the Hill Climbing Algorithm
best_solution = hill_climbing(iterations, step_size, min_value, max_value)
print("Best solution:", best_solution)
print("Fitness of best solution:", fitness_function(best_solution))
