
# Objective: Write a program that takes a list of numbers and prints out the sum, average, and largest number in the list.




# Problem 1:
def calculate_sum(numbers):

    total = sum(numbers)
    return total 

# Example:
Problem1_list = [5, 10, 15, 20, 25] 
Problem1Result = calculate_sum(Problem1_list)
print("The sum of the list is:", Problem1Result) 




#Problem 2:
def calculate_average(numbers):

    total_sum = sum(numbers)
    average = total_sum / len(numbers)
    return average 

# Example:
Problem2_list = [2, 4, 6, 8, 10]
Problem2Result = calculate_average(Problem2_list)
print("The average of the list is:", Problem2Result) 




#Problem 3:
def find_largest(numbers):

  largest_num = numbers[0]
  for num in numbers:
    if num > largest_num:
      largest_num = num  
  return largest_num 

# Example:
Problem3_list = [2, 72, 91, 14, 0, 5]
print("The largest number is:", find_largest(Problem3_list)) 
