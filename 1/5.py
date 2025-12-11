def print_multiplication_table(N):
    print(" " * 4, end="")
    for j in range(1, N + 1):
        if j % 2 == 0:  
            print(f"{j:4}", end="")
    print()
    print(" " * 4 + "-" * (4 * (N//2 + 1)))
    
    for i in range(1, N + 1):
        if i % 2 == 0:  
            print(f"{i:2} |", end="")
            for j in range(1, N + 1):
                if j % 2 == 0:  
                    product = i * j
                    print(f"{product:4}", end="")
            print()


print_multiplication_table(10)
