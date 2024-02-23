import tkinter as tk

class Utils:
# DEBUG DONE    

    def valid_input(new_val, selected_option):
       
        if selected_option == "Option 1":
            
            max_length = 8
            return all(char in '01' for char in new_val) and len(new_val) <= max_length 
        
        elif selected_option == "Option 2":
            
            max_length = 10
            return all(char in '0987654321' for char in new_val) and len(new_val) <= max_length     
        
        
        elif selected_option == "Option 3":
            
            max_length = 10
            return all(char in '07654321' for char in new_val) and len(new_val) <= max_length     
        
        
        
        elif selected_option == "Option 4":
            
            max_length = 16
            allow_char = '0987654321ABCDEF'
            return all(char.lower() in allow_char.lower() for char in new_val) and  len(new_val) <= max_length
       
        else:
           return False
       
       
