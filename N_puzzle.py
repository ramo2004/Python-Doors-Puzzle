

def n_doors_puzzle(N):
    doors = [False] * N  

    for i in range(1, N + 1):
        for j in range(1, N + 1):
            if j % i == 0:
                doors[j - 1] = not doors[j - 1]  
                print(f"i: {i}; j: {j}; step size: {i}. Toggling door number {j}.")

    print("Algorithm has finished.\n")

    open_doors = [door_number + 1 for door_number, state in enumerate(doors) if state]
    print("\n".join(f"Door number {door} remains open." for door in open_doors))
    print("\n")


    closed_doors = [door_number + 1 for door_number, state in enumerate(doors) if not state]
    print("\n".join(f"Door number {door} remains closed." for door in closed_doors))


N1 = int(input("Run 1:\nEnter the number of Doors (N): "))
n_doors_puzzle(N1)

N2 = int(input("\nRun 2:\nEnter the number of Doors (N): "))
n_doors_puzzle(N2)
