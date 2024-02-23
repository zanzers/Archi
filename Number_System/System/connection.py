import tkinter as tk
from System.conversion import BinaryConverter, DecimalConverter, OctalConverter,HexaConverter

# DONE!
class Bcon:
       
    def b_to_d(input_var, output_test):
        binary_input = input_var.get()
        binary_result = BinaryConverter.decimal(binary_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(binary_result))
        output_test.config(state=tk.DISABLED)
        output_test.focus()

    def b_to_o(input_var, output_test):
        binary_input = input_var.get()
        binary_result = BinaryConverter.octal(binary_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(binary_result))
        output_test.config(state=tk.DISABLED)

    def b_to_h(input_var, output_test):
        binary_input = input_var.get()
        binary_result = BinaryConverter.hex(binary_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(binary_result))
        output_test.config(state=tk.DISABLED)
    
    def frac_d(binary_input, point_label):
        frac_input = binary_input.get()
        frac_result = BinaryConverter.frac_decimal(frac_input)
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(frac_result))
        point_label.config(state=tk.DISABLED)
         
    def frac_o(binary_input, point_label):
        frac_input = binary_input.get()
        frac_result = BinaryConverter.frac_octal(frac_input)
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(frac_result))
        point_label.config(state=tk.DISABLED)

    def frac_h(binary_input, point_label):
        frac_input = binary_input.get()
        frac_result = BinaryConverter.frac_hex(frac_input)
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(frac_result))
        point_label.config(state=tk.DISABLED)

    def t_deci(binary_input, piont_label):
        binary_input = binary_input.get()
        _,_,deci_num_str = BinaryConverter.twos_complement(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(deci_num_str))
        piont_label.config(state=tk.DISABLED)

    def t_octal(binary_input, piont_label):
        binary_input = binary_input.get()
        octal_num,_,_ = BinaryConverter.twos_complement(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(octal_num))
        piont_label.config(state=tk.DISABLED)

    def t_hex(binary_input, piont_label):
        binary_input = binary_input.get()
        _,hex_num_str,_ = BinaryConverter.twos_complement(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(hex_num_str))
        piont_label.config(state=tk.DISABLED)

class Dcon:
    
    def d_to_b(input_var, output_test):
        decimal_input = input_var.get()
        decimal_result = DecimalConverter.binary(decimal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(decimal_result))
        output_test.config(state=tk.DISABLED)
        output_test.focus()
    
    def d_to_o(input_var, output_test):
        decimal_input = input_var.get()
        decimal_result = DecimalConverter.octal(decimal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(decimal_result))
        output_test.config(state=tk.DISABLED)   
    
    def d_to_h(input_var, output_test):
        decimal_input = input_var.get()
        decimal_result = DecimalConverter.hex(decimal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(decimal_result))
        output_test.config(state=tk.DISABLED)
    
    def frac_b(decimal_input, point_label):
        decimal_input = decimal_input.get()
        decimal_result = DecimalConverter.frac_binary(int(decimal_input))
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(decimal_result))
        point_label.config(state=tk.DISABLED)
    
    def frac_o(decimal_input, point_label):
        decimal_input = decimal_input.get()
        decimal_result = DecimalConverter.frac_octal(int(decimal_input))
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(decimal_result))
        point_label.config(state=tk.DISABLED)
        
    def frac_h(decimal_input, point_label):
        decimal_input = decimal_input.get()
        decimal_result = DecimalConverter.frac_hex(int(decimal_input))
        point_label.config(state=tk.NORMAL)
        point_label.delete(1.0, tk.END)
        point_label.insert(tk.END, str(decimal_result))
        point_label.config(state=tk.DISABLED)
        
    def t_binary(binary_input, piont_label):
        binary_input = binary_input.get()
        binary_num_spaced,_,_ = DecimalConverter.twos_decimal(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(binary_num_spaced))
        piont_label.config(state=tk.DISABLED)

    def t_octal(binary_input, piont_label):
        binary_input = binary_input.get()
        _,octal_num_spaced,_ = DecimalConverter.twos_decimal(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(octal_num_spaced))
        piont_label.config(state=tk.DISABLED)

    def t_hex(binary_input, piont_label):
        binary_input = binary_input.get()
        _,_,hex_num_spaced = DecimalConverter.twos_decimal(binary_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(hex_num_spaced))
        piont_label.config(state=tk.DISABLED)
            
class Ocon:
    
    def o_to_b(input_var, output_test):
    
        octal_input = input_var.get()
        octal_result = OctalConverter.octal_binary(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(octal_result))
        output_test.config(state=tk.DISABLED)
        output_test.focus()
        
    def o_to_d(input_var, output_test):
        octal_input = input_var.get()
        octal_result = OctalConverter.octal_decimal(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(octal_result))
        output_test.config(state=tk.DISABLED)
        
    def o_to_h(input_var, output_test):
        octal_input = input_var.get()
        octal_result = OctalConverter.octal_hex(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(octal_result))
        output_test.config(state=tk.DISABLED)
    
    def frac_b(input_var, output_test):
        octal_input = input_var.get()
        binary_fraction,_,_ = OctalConverter.octal_fraction(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(binary_fraction))
        output_test.config(state=tk.DISABLED)
    
    def frac_d(input_var, output_test):
        octal_input = input_var.get()
        _,decimal_fraction_str,_ = OctalConverter.octal_fraction(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(decimal_fraction_str))
        output_test.config(state=tk.DISABLED)
    
    def frac_h(input_var, output_test):
        octal_input = input_var.get()
        _,_,hex_fraction = OctalConverter.octal_fraction(octal_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(hex_fraction))
        output_test.config(state=tk.DISABLED)
          
    def t_binary(octal_input, piont_label):
        octal_input = octal_input.get()
        binary_num_spaced,_,_ = OctalConverter.twos_octal(octal_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(binary_num_spaced))
        piont_label.config(state=tk.DISABLED)

    def t_decimal(octal_input, piont_label):
        octal_input = octal_input.get()
        _,decimal_num_str,_ = OctalConverter.twos_octal(octal_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(decimal_num_str))
        piont_label.config(state=tk.DISABLED)

    def t_hex(octal_input, piont_label):
        octal_input = octal_input.get()
        _,_,hex_num_spaced = OctalConverter.twos_octal(octal_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(hex_num_spaced))
        piont_label.config(state=tk.DISABLED)

class Hcon:
    def h_to_b(input_var, output_test):
        
        hex_input = input_var.get()
        hex_result = HexaConverter.hex_binary(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(hex_result))
        output_test.config(state=tk.DISABLED)
        output_test.focus()
        
    def h_to_d(input_var, output_test):
        hex_input = input_var.get()
        hex_result = HexaConverter.hex_decimal(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(hex_result))
        output_test.config(state=tk.DISABLED)
        
    def h_to_o(input_var, output_test):
        hex_input = input_var.get()
        hex_result = HexaConverter.hex_octal(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(hex_result))
        output_test.config(state=tk.DISABLED)
    
    def frac_b(input_var, output_test):
        hex_input = input_var.get()
        binary_fraction,_,_ = HexaConverter.hex_fraction(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(binary_fraction))
        output_test.config(state=tk.DISABLED)
    
    def frac_d(input_var, output_test):
        hex_input = input_var.get()
        _,decimal_fraction_str,_ = HexaConverter.hex_fraction(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(decimal_fraction_str))
        output_test.config(state=tk.DISABLED)
    
    def frac_o(input_var, output_test):
        hex_input = input_var.get()
        _,_,octal_fraction = HexaConverter.hex_fraction(hex_input)
        output_test.config(state=tk.NORMAL)
        output_test.delete(1.0, tk.END)
        output_test.insert(tk.END, str(octal_fraction))
        output_test.config(state=tk.DISABLED)
    
    def t_binary(input_var, piont_label):
        hex_input = input_var.get()
        binary_num_spacced,_,_ = HexaConverter.twos_hex(hex_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(binary_num_spacced))
        piont_label.config(state=tk.DISABLED)    

    def t_deci(input_var, piont_label):
        hex_input = input_var.get()
        _,decimal_num,_ = HexaConverter.twos_hex(hex_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(decimal_num))
        piont_label.config(state=tk.DISABLED)    
        
    def t_octal(input_var, piont_label):
        hex_input = input_var.get()
        _,_,octal_num_spacced = HexaConverter.twos_hex(hex_input)
        piont_label.config(state=tk.NORMAL)
        piont_label.delete(1.0, tk.END)
        piont_label.insert(tk.END, str(octal_num_spacced))
        piont_label.config(state=tk.DISABLED)  