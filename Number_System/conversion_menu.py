import tkinter as tk
from  System.connection import *
from System.utils import *


# DONE!  
class Menu3Page(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        
        back_button = tk.Button(self, text="Back to Main", command=lambda: controller.show_frame("MainPage"))  # Use a string identifier instead of MainPage
        back_button.grid(row=0, column=0, pady=10, padx=10, sticky="nw")
        
        label = tk.Label(self, text="Menu 3")
        label.grid(row=1, column=0, pady=10, padx=10, sticky="n")

        # Rest of your Menu3Page code...


        # Frame to contain dropdown menu, input field, and Convert button
        self.input_frame = tk.Frame(self)
        self.input_frame.grid(row=2, column=0, columnspan=3, pady=5, padx=10, sticky="ew")

        # Dropdown menu
        self.selected_option = tk.StringVar(self.input_frame)
        self.selected_option.set("Select Option")  # Set default option
        options = ["Option 1", "Option 2", "Option 3", "Option 4"]  # List of options
        dropdown = tk.OptionMenu(self.input_frame, self.selected_option, *options)
        dropdown.config(indicatoron=False)
        dropdown.grid(row=0, column=0, pady=5, padx=(0, 5), sticky="e")

        # Input field
        self.input_var = tk.StringVar(self.input_frame)
        self.input_entry = tk.Entry(self.input_frame, textvariable=self.input_var, highlightthickness=0, highlightbackground="black", width=1)
        self.input_entry.grid(row=0, column=1, pady=15, padx=(10, 10), sticky="ew")
        
        validate_cmd = (self.input_frame.register(lambda new_val: Utils.valid_input(new_val, self.selected_option.get())), '%P')
        self.input_entry.config(validate='key', validatecommand=validate_cmd)
        
        self.frac_point = tk.Label(self.input_frame, text=".", fg="black")
        self.frac_point.grid(row=0, column=2, pady=0, padx=(2,2), sticky="ew")
        
        self.decimal_var = tk.StringVar(self.input_frame)
        self.decimal_input = tk.Entry(self.input_frame, textvariable=self.decimal_var, highlightthickness=0, highlightbackground="black", width=10)
        self.decimal_input.grid(row=0, column=3, pady=5, padx=(10, 10), sticky="ew")
        
        valid_decimal = (self.input_frame.register(lambda new_val: Utils.valid_input(new_val, self.selected_option.get())), '%P')
        self.decimal_input.config(validate = 'key', validatecommand = valid_decimal)
        
        # Convert button
        convert_button = tk.Button(self.input_frame, text="Convert", command=self.convert_btn)
        convert_button.grid(row=0, column=4, pady=5, padx=(5, 0), sticky="w")
        
        # Clear button
        clear_btn = tk.Button(self.input_frame, text="clear", command=self.clear_btn)
        clear_btn.grid(row=1, column=4, pady=5, padx=(5, 0), sticky="w")

        # Labels for "Test 1", "Test 2", "Test 3", "Test 4" below each other
        self.label_test1 = tk.Label(self.input_frame, text="Test 1", fg="blue")
        self.label_test1.grid(row=2, column=0, pady=(20, 0), padx=10, sticky="ew")
        

        self.label_test2 = tk.Label(self.input_frame, text="Test 2", fg="red")
        self.label_test2.grid(row=3, column=0, pady=5, padx=10, sticky="ew")

        self.label_test3 = tk.Label(self.input_frame, text="Test 3", fg="green")
        self.label_test3.grid(row=4, column=0, pady=5, padx=10, sticky="ew")

        self.label_test4 = tk.Label(self.input_frame, text="Test 4", fg="purple")
        self.label_test4.grid(row=5, column=0, pady=5, padx=10, sticky="ew")
        
        self.label_test5 = tk.Label (self.input_frame, text="Test1_2's", fg="red")
        self.label_test5.grid(row=7, column=0, pady=10, padx=10, sticky="ew")
        
        self.label_test6 = tk.Label (self.input_frame, text="Test3_2's", fg="red")
        self.label_test6.grid(row=8, column=0, pady=10, padx=10, sticky="ew")
        
        self.label_test7 = tk.Label (self.input_frame, text="Test4_2's", fg="red")
        self.label_test7.grid(row=9, column=0, pady=10, padx=10, sticky="ew")

        # Output boxes for test results
        self.output_test1 = tk.Text(self.input_frame, wrap=tk.WORD, width=30, height=1 , highlightthickness=0, bd=0)
        self.output_test1.grid(row=2, column=1, pady=5, padx=5, sticky="ew")
        self.output_test1.config(state=tk.DISABLED)
        
        self.point_label1 = tk.Label(self.input_frame, text=".", fg="blue")
        self.point_label1.grid(row=2, column=2, pady=(20, 0), padx=10, sticky="ew")

        self.point_output1 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.point_output1.grid(row=2, column=3, pady=5, padx=5, sticky="ew")
        self.point_output1.config(state=tk.DISABLED)




        self.output_test2 = tk.Text(self.input_frame, wrap=tk.WORD, width=30, height=1, highlightthickness=0, bd=0)
        self.output_test2.grid(row=3, column=1, pady=5, padx=5, sticky="ew")
        self.output_test2.config(state=tk.DISABLED)
        
        self.point_label2 = tk.Label(self.input_frame, text=".", fg="blue")
        self.point_label2.grid(row=3, column=2, pady=(20, 0), padx=10, sticky="ew")
        
        self.point_output2 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.point_output2.grid(row=3, column=3, pady=5, padx=5, sticky="ew")
        self.point_output2.config(state=tk.DISABLED)
        
        

        self.output_test3 = tk.Text(self.input_frame, wrap=tk.WORD, width=30, height=1 , highlightthickness=0, bd=0)
        self.output_test3.grid(row=4, column=1, pady=5, padx=5, sticky="ew")
        self.output_test3.config(state=tk.DISABLED)
        
        self.point_label3 = tk.Label(self.input_frame, text=".", fg="blue")
        self.point_label3.grid(row=4, column=2, pady=(20, 0), padx=10, sticky="ew")

        self.point_output3 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.point_output3.grid(row=4, column=3, pady=5, padx=5, sticky="ew")
        self.point_output3.config(state=tk.DISABLED)

        
        self.output_test4 = tk.Text(self.input_frame, wrap=tk.WORD, width=30, height=1 , highlightthickness=0, bd=0)
        self.output_test4.grid(row=5, column=1, pady=5, padx=5, sticky="ew")
        self.output_test4.config(state=tk.DISABLED)
        
        self.point_label4 = tk.Label(self.input_frame, text=".", fg="blue")
        self.point_label4.grid(row=5, column=2, pady=(20, 0), padx=10, sticky="ew")

        self.point_output4 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.point_output4.grid(row=5, column=3, pady=5, padx=5, sticky="ew")
        self.point_output4.config(state=tk.DISABLED)    
        
        self.output_test5 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.output_test5.grid(row=7, column=1, pady=5, padx=10,sticky="ew")
        self.output_test5.config(state=tk.DISABLED)    
        
        
        self.output_test6 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.output_test6.grid(row=8, column=1, pady=5, padx=10,sticky="ew")
        self.output_test6.config(state=tk.DISABLED)  
        
        self.output_test7 = tk.Text(self.input_frame, wrap=tk.WORD, width=15, height=1 , highlightthickness=0, bd=0)
        self.output_test7.grid(row=9, column=1, pady=5, padx=10,sticky="ew")
        self.output_test7.config(state=tk.DISABLED)  
            
        
        self.input_entry.bind("<Return>", lambda event: self.convert_btn())
        self.decimal_input.bind("<Return>", lambda event: self.convert_btn())

        self.selected_option.trace("w", self.labels_update)


# DEDUG DONE! YEAH.....
    def labels_update(self, *args):
        option_display = {
            "Option 1": [self.label_test1, self.output_test1, self.point_label1, self.point_output1],
            "Option 2": [self.label_test2, self.output_test2, self.point_label2, self.point_output2],
            "Option 3": [self.label_test3, self.output_test3, self.point_label3, self.point_output3],
            "Option 4": [self.label_test4, self.output_test4, self.point_label4, self.point_output4]
        }
        

        selected_option = self.selected_option.get()
        
        for display in sum(option_display.values(), []):
            if display in option_display[selected_option]:
                display.grid_remove()
            else:
                display.grid()

# DEDUG DONE
    def convert_btn(self, **args):
        
        option = self.selected_option.get()
        decimal = self.decimal_input.get()
        
        
        conversion = {
            "Option 1": [Bcon.b_to_d,Bcon.b_to_o,Bcon.b_to_h,Bcon.t_deci,Bcon.t_octal,Bcon.t_hex],
            "Option 2": [Dcon.d_to_b,Dcon.d_to_o,Dcon.d_to_h,Dcon.t_binary,Dcon.t_octal,Dcon.t_hex],
            "Option 3": [Ocon.o_to_b,Ocon.o_to_d,Ocon.o_to_h,Ocon.t_binary,Ocon.t_decimal,Ocon.t_hex],
            "Option 4": [Hcon.h_to_b,Hcon.h_to_d,Hcon.h_to_o,Hcon.t_binary,Hcon.t_deci,Hcon.t_octal]
        }
        
        output_display = {
            "Option 1": [self.output_test2,self.output_test3,self.output_test4,self.output_test5,self.output_test6,self.output_test7],
            "Option 2": [self.output_test1,self.output_test3,self.output_test4,self.output_test5,self.output_test6,self.output_test7],
            "Option 3": [self.output_test1,self.output_test2,self.output_test4,self.output_test5,self.output_test6,self.output_test7],
            "Option 4": [self.output_test1,self.output_test2,self.output_test3,self.output_test5,self.output_test6,self.output_test7]
        }
        
        for func, output in zip (conversion.get(option, []), output_display.get(option, [])):
            func(self.input_var, output)
        
        
        if  decimal !="" and option == "Option 1":
            
            frac_function = [Bcon.frac_d,Bcon.frac_o,Bcon.frac_h]
            frac_display = [self.point_output2,self.point_output3,self.point_output4]
            
            for func, frac_output in zip(frac_function, frac_display):
                func(self.decimal_input, frac_output)
        
        if  decimal !="" and option == "Option 2":
            
            frac_function = [Dcon.frac_b,Dcon.frac_o,Dcon.frac_h]
            frac_display = [self.point_output1,self.point_output3,self.point_output4]
            
            for func, frac_output in zip(frac_function, frac_display):
                func(self.decimal_input, frac_output)
                
        if decimal !="" and option == "Option 3":
            
            frac_function = [Ocon.frac_b,Ocon.frac_d,Ocon.frac_h]
            frac_display = [self.point_output1,self.point_output2,self.point_output4]
            
            for func, frac_output in zip(frac_function, frac_display):
                func(self.decimal_input, frac_output)
        
        if decimal !="" and option == "Option 4":
            
            frac_function = [Hcon.frac_b,Hcon.frac_d,Hcon.frac_o]
            frac_display = [self.point_output1,self.point_output2,self.point_output3]
            
            for func, frac_output in zip(frac_function, frac_display):
                func(self.decimal_input, frac_output)
           
# DEDUG DONE...  
    def clear_btn(self):
      
        self.input_var.set("")
        self.decimal_var.set("")

        output_tests = [
            self.output_test1,
            self.output_test2,
            self.output_test3,
            self.output_test4,
            self.point_output1,
            self.point_output2,
            self.point_output3,
            self.point_output4,
            self.output_test5,
            self.output_test6,
            self.output_test7
        ]
        for output_test in output_tests:
            output_test.config(state=tk.NORMAL)
            output_test.delete(1.0, tk.END)
            output_test.config(state=tk.DISABLED)

        validate_cmd = (self.input_frame.register(lambda new_val:
                        Utils.valid_input(new_val, self.selected_option.get())),
                        '%P')
        self.input_entry.config(validate='key', validatecommand=validate_cmd)
    