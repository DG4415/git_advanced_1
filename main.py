'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
from typing import List

def even_list(int_list: List[int]) -> List[int]:    
   
    even_int_list = []
    for num in int_list:
        if num % 2 == 0:
            even_int_list.append(num)
    return even_int_list
        

    #TODO: Implement even_list    
 
 # Skeleton code for sum_of_squares_of_even
def sum_of_squares_of_even(even_int_list: List[int]) -> int:    
    
    # TODO: Implement sum_of_squares_of_even    
    
    sum_of_squares_of_even = 0 
    for num in even_int_list:
        sum_of_squares_of_even += num*num
        
    return sum_of_squares_of_even
    

# Main function
def main():    
    # Example list    
    int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]    
    even_int_list = even_list(int_list)    
    output = sum_of_squares_of_even(even_int_list)    
    print(output)

# Boilerplate code
if __name__ == "__main__":    
    main()