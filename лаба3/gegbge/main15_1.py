direction = input("Enter direction (N/S/E/W): ").upper()
option = int(input("""
0 - continue
1 - turn left
2 - turn right
Your choice: """))

left_turn = {'N': 'W', 'W': 'S', 'S': 'E', 'E': 'N'}
right_turn = {'N': 'E', 'E': 'S', 'S': 'W', 'W': 'N'}

if direction not in ['N', 'S', 'E', 'W']:
    result = "error: invalid direction"
elif option not in [0, 1, 2]:
    result = "error: invalid instruction"
    
else:
    if option == 0:
        new_direction = direction
    elif option == 1:
        new_direction = left_turn[direction]
    else:  # option == 2
        new_direction = right_turn[direction]
    
    result = f"new direction: {new_direction}"

print(result)            

        
            