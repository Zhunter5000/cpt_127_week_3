# The code now properly stops after 10 numbers


# Code

finished_program = False

# Count to 10 Program

i = 0

while finished_program == False:

    print(f'Testing i = {i}')

    if (i == 10):
        finished_program = True
        break

    i += 1