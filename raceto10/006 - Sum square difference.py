sum_of_squares = lambda n: sum([i**2 for i in range(1, n+1)])
square_of_sum = lambda n: sum(range(1, n+1))**2
print(square_of_sum(100) - sum_of_squares(100))