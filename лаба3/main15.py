direction = input("Enter direction (N/S/E/V): ").upper()
option = int(input("""
0 - continue
1 - turn left
2 - turn right
Your choice: """))

if direction not in ['N', 'S', 'E', 'V']:
    result = "error: invalid direction"
elif option not in [0, 1, 2]:
    result = "error: invalid instruction"

else:
    if option == 0:
        new_direction = direction
    elif option == 1:  
        if direction == 'N':
            new_direction = 'V'
        elif direction == 'S':
            new_direction = 'E'
        elif direction == 'E':
            new_direction = 'N'
        else: 
            new_direction = 'S'
    else:  
        if direction == 'N':
            new_direction = 'E'
        elif direction == 'S':
            new_direction = 'V'
        elif direction == 'E':
            new_direction = 'S'
        else: 
            new_direction = 'N'
    
    result = f"new direction: {new_direction}"

print(result)
        
            