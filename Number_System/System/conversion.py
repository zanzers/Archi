
# DONE!!!!!
class BinaryConverter:
    
    def decimal(binary):
                
        binary_num = int(binary)
        dnum = 0
        i = 1
        while binary_num !=0:
            rem = binary_num % 10
            dnum = dnum + (rem * i)
            i = i * 2
            binary_num = int(binary_num/10)
        
        
        print("B_d",dnum)
        return dnum
         
    def octal(binary):   
             
        binary_num = int(binary)
        odig = 0
        mul = chk = 1
        octal_number = ""
        while binary_num != 0:
            rem = binary_num % 10
            odig = odig +(rem * mul)
            if chk %3 == 0:
                octal_number += str(odig)
                mul = chk = 1
                odig = 0
            else:
                mul *= 2
                chk += 1
            binary_num = int(binary_num / 10)
        if chk!=1:
            octal_number += str(odig)
            
        octal_number = octal_number[::-1]
        
        
        print("B_o",octal_number)
        return octal_number

    def hex(binary):        
        
        binary_num = int(binary)
        hex_list = []
        while binary_num != 0:
            hex_digit = 0
            for i in range(4):
                bit = binary_num % 10
                hex_digit += bit * (2 ** i)
                binary_num //= 10
            if hex_digit < 10:
                hex_list.insert(0, str(hex_digit))
            else:
                hex_list.insert(0, chr(hex_digit + 55))
        hex_value = "".join(hex_list)
          
        print("B_h", hex_value)    
        return hex_value

    def twos_complement(binary):
        
        invert = ''.join('1' if bit == '0' else '0' for bit in binary)
        complement = format(int(invert, 2) + 1, 'b')
        
        while len(complement) % 4 != 0:
            complement = '0' + complement
            
        print(complement)
        
        octal_num = BinaryConverter.octal(complement)
        hex_num = BinaryConverter.hex(complement)
        deci_num = BinaryConverter.decimal(binary)
        
        hex_num_str = str(hex_num)
        deci_num_str= '-' + str(deci_num)
        
        print("t_o", octal_num)
        print("t_h", hex_num)
        print("t_d", deci_num_str)
        
        num_digit = max(len(octal_num), len(hex_num_str))
        if num_digit < 4:
            octal_num = '7' * (4 - len(octal_num)) + octal_num
            hex_num_str = 'F' * (4 - len(hex_num_str)) + hex_num_str[-4:]
            
        else:
            hex_num_str = hex_num_str[-4:]
        
        return octal_num, hex_num_str, deci_num_str

    def frac_decimal(fraction):
        
        decimal_frac = sum(int(digit) * (2 ** -(i+1)) for i, digit in enumerate(fraction))
        decimal_frac_str = str(decimal_frac)
        if decimal_frac_str.startswith("0."):
            decimal_frac_str = decimal_frac_str[2:]
        
        print("F_B_d",decimal_frac_str)
        return decimal_frac_str
    
    def frac_octal(fraction):
        
        octal_fraction_str = ''

        while len(fraction) % 3 != 0:
            fraction += '0'

        for i in range(0, len(fraction), 3):
            group = fraction[i:i+3]
            octal_digit = int(group, 2)
            octal_fraction_str += str(octal_digit)

        if octal_fraction_str.startswith("0."):
            octal_fraction_str = octal_fraction_str[2:]

        print("F_B_o", octal_fraction_str)
        return octal_fraction_str

    def frac_hex(fraction):
        
        hex_frac_str = ''
        
        while len(fraction) % 4 != 0:
            fraction += '0'
            
        for i in range(0, len(fraction), 4):
            hex_val = fraction[i:i+4]
            hex_digit = hex(int(hex_val, 2))[2:].upper()
            hex_frac_str += hex_digit
            
        if hex_frac_str.startswith("0."):
            hex_frac_str = hex_frac_str[2:]
        
        print("F_B_h",hex_frac_str)
        return hex_frac_str

class DecimalConverter:
        
    def binary(decimal):
        
        dnum = int(decimal)
        i = 0
        b = []
        
        while dnum != 0:
            b.insert(i, dnum % 2)
            i += 1
            dnum = int(dnum / 2)
            
        i -= 1
        binary_str = ""
    
        while i >= 0:
            binary_str += str(b[i])
            i -= 1
        
        # if len(binary_str) < 8:
        #     binary_str  = '0'  * (8 - len(binary_str)) + binary_str
        
        print("D_B",binary_str)
        return binary_str
    
    def octal(decimal):
    
        dnum = abs(int(decimal))
        
        i = 0
        onum = []
        
        while dnum != 0:
            onum.insert(i, dnum % 8)
            i += 1
            dnum = int(dnum / 8)
        
        octal_str = ""        
        i -= 1
        while i >= 0:
            octal_str += str(onum[i])
            i -= 1

      
        return octal_str
    
    def hex(decimal):
        
        dnum = abs(int(decimal))  

        i = 0
        hex_list = []

        while dnum != 0:
            rem = dnum % 16
            if rem < 10:
                rem += 48
            else:
                rem += 55
                
            hex_list.insert(i, chr(rem))
            i += 1
            dnum = int(dnum / 16)
            
        hex_str = ""
        i -= 1
        while i >= 0:
            hex_str += hex_list[i]
            i -= 1
        
        print(hex_str)
        return hex_str

    def frac_binary(fraction):
        precision = 7
        b_fraction = ""

        fraction_str = str(fraction)
        if '.' not in fraction_str:
            fraction_str = '.' + fraction_str
        print(fraction_str)
        
        for i in range(precision):
            fraction_str = float(fraction_str) * 2
            if fraction_str >= 1:
                b_fraction += "1"
                fraction_str -= 1
            else:
                b_fraction += "0"
        
        return b_fraction

    def frac_octal(fraction):
        
        precision = 3
        octal_frac = ""
        
        fraction_str = str(fraction)
        if '.' not in fraction_str:
            fraction_str = '.' + fraction_str
        
        for i in range(precision):
            fraction_str = float(fraction_str) * 8
            fraction_input = int(fraction_str)
            octal_frac += str(fraction_input)
            fraction_str -= fraction_input
            
        return octal_frac
    
    def frac_hex(fraction):
        precision = 5
        hex_frac = ""
        
        
        fraction_str = str(fraction)
        if '.' not in fraction_str:
            fraction_str = '.' + fraction_str
        
        
        for i in range(precision):
            fraction_str = float(fraction_str) * 16
            fraction_part = int(fraction_str)
            if fraction_part < 10:
                hex_frac += str(fraction_part)
            else:
                hex_frac += chr(ord('A') + fraction_part - 10)
            fraction_str -= fraction_part
            
        return hex_frac

    def twos_decimal(decimal):
        
        binary_decimal = -1 * int(decimal)
        binary_decimal = DecimalConverter.binary(binary_decimal & 0b1111111111111111)[2:].zfill(8)
        octal_num = DecimalConverter.octal(int(binary_decimal, 2))[2:]
        hex_num_str = DecimalConverter.hex(int(binary_decimal, 2))[1:]
        
        
        print("1st",binary_decimal)
        print(octal_num)
        print(hex_num_str)
       
        octal_num = '7' * (12 - len(octal_num)) + octal_num
        hex_num_str = 'F' * (16 - len(hex_num_str)) + hex_num_str
        binary_decimal = '1' * (16 - len(binary_decimal)) + binary_decimal
            
        binary_num_spaced = ' '.join([binary_decimal[i:i+4] for i in range(0, len(binary_decimal), 4)])
        octal_num_spaced = ' '.join([octal_num[i:i+3] for i in range(0, len(octal_num), 3)])
        hex_num_spaced = ' '.join([hex_num_str[i:i+4] for i in range(0, len(hex_num_str),4)])        
        
        return binary_num_spaced, octal_num_spaced,hex_num_spaced
     
class OctalConverter:    
    
    def is_valid_octal(octal):
        
# Check if the input's string is a valid octal number
        oct_str = str(octal)
        if not oct_str:
            return False  # Empty string is not a valid octal number
        if oct_str[0] == '-':
            oct_str = oct_str[1:]  # Remove the negative sign if present
        for digit in oct_str:
            if not '0' <= digit <= '7':
                return False  # Non-octal digit found
        return True

    def octal_binary(octal):
        if not OctalConverter.is_valid_octal(octal):
            return "N/A"
        
        oct_num = int(str(octal), 8)
        b_num = DecimalConverter.binary(oct_num)[2:]  # Assuming DecimalConverter.binary is defined elsewhere
        
        if len(b_num) < 8:
            b_num = '0' * (8 - len(b_num)) + b_num
            
        print(b_num)
        return b_num
  
    def octal_decimal(octal):
        
        oct_num = abs(int(octal))
        
        chk = 0
        i = 0
        dec_num = 0
        
        while oct_num != 0:
            rem = oct_num % 10
            
            if rem > 7:
                chk = 1
                break
            dec_num += (rem * (8 ** i))
            i += 1
            oct_num = int(oct_num / 10)
        
        print(dec_num)
        return str(dec_num) if chk == 0 else "N/A"
    
    def octal_hex(octal):
        oct_num = abs(int(octal))
        
        chk = 0
        i = dnum = 0
        
        while oct_num != 0:
            rem = oct_num % 10
            if rem > 7:
                chk = 1
                break
            dnum += (rem * (8 ** i))
            i += 1
            oct_num = int(oct_num / 10)
        
        hex_num = ""
        while dnum != 0:
            rem = dnum % 16
            if rem < 10:
                rem += 48
            else:
                rem += 55
            rem = chr(rem)
            hex_num += rem
            dnum = int(dnum / 16)
            
        
        hex_result = hex_num[::-1]
        
        print("ss", hex_result)
        return hex_result if chk == 0 else "N/A"
  
    def twos_octal(octal):
        
        
        binary_int = int(octal)
        
        binary = OctalConverter.octal_binary(binary_int & 0b1111111111111111)[2:].zfill(8)
        invert = ''.join('1' if bit == '0' else '0' for bit in binary)
        complement = format(int(invert, 2) + 1, 'b')
        
        print("C",complement)
        
        decimal_num_str = OctalConverter.octal_decimal(octal)
        hex_num_str = OctalConverter.octal_hex(int(complement, 2))[1:].upper()
        
        
        hex_num_str = 'F' * (16 - len(hex_num_str)) + hex_num_str
        binary_str = '1' * (16 - len(complement)) + complement
        decimal_num_str = '-' + decimal_num_str
        
        binary_num_spaced = ' '.join([binary_str[i:i+4] for i in range(0, len(binary_str), 4)])
        hex_num_spaced = ' '.join([hex_num_str[i:i+4] for i in range(0, len(hex_num_str),4)])  
        
        print(binary_num_spaced,hex_num_spaced, decimal_num_str)
        
        return binary_num_spaced, decimal_num_str, hex_num_spaced
    
    def octal_fraction(octal):
        
        binary_fraction = ''
        decimal_fraction = 0.0
        hex_fraction = ''
        
        #This part are for binary using bin fraction 
        for digit in octal:
            binary_digit = bin(int(digit))[2:].zfill(3)
            binary_fraction += binary_digit
        
        # This part are for decimal fraction
        for i in range(len(octal)):
            decimal_fraction += int(octal[i]) * (8 ** -(i+1))

        decimal_num = decimal_fraction
        
        # this for hex fraction
        for i in range(4):
            decimal_num *= 16
            hex_digit = hex(int(decimal_num))[2:].upper()
            hex_fraction += hex_digit
            decimal_num -= int(decimal_num)
            
            
        decimal_fraction_str = str(decimal_fraction)
        if decimal_fraction_str.startswith('0.'):
            decimal_fraction_str = decimal_fraction_str[2:]
        
        print("TWOS OCTAL:",decimal_fraction_str)
        return binary_fraction, decimal_fraction_str, hex_fraction        
        
class HexaConverter:
    
    def hex_binary(hexa):
        
        input_str = str(hexa)
        
        hex_num = str(hexa)
        bin_num = ""
        i = 0
        
        while i < len(hex_num):
            if hex_num[i] == '0':
                bin_num = bin_num + '0000'
            elif hex_num[i] == '1':
                bin_num = bin_num + '0001'
            elif hex_num[i] == '2':
                bin_num = bin_num + '0010'
            elif hex_num[i] == '3':
                bin_num = bin_num + '0011'
            elif hex_num[i] == '4':
                bin_num = bin_num + '0100'
            elif hex_num[i] == '5':
                bin_num = bin_num + '0101'
            elif hex_num[i] == '6':
                bin_num = bin_num + '0110'
            elif hex_num[i] == '7':
                bin_num = bin_num + '0111'
            elif hex_num[i] == '8':
                bin_num = bin_num + '1000'
            elif hex_num[i] == '9':
                bin_num = bin_num + '1001'
            elif hex_num[i] == 'a' or hex_num[i] == 'A':
                bin_num = bin_num + '1010'
            elif hex_num[i] == 'b' or hex_num[i] == 'B':
                bin_num = bin_num + '1011'
            elif hex_num[i] == 'c' or hex_num[i] == 'C':
                bin_num = bin_num + '1100'
            elif hex_num[i] == 'd' or hex_num[i] == 'D':
                bin_num = bin_num + '1110'
            elif hex_num[i] == 'e' or hex_num[i] == 'E':
                bin_num = bin_num + '1110'
            elif hex_num[i] == 'f' or hex_num[i] == 'F':
                bin_num = bin_num + '1111'
            i += 1
            
            
  
        return bin_num                                                          

    def hex_decimal(hexa):
        
        input_str = str(hexa)
        
        chk = dnum = i = 0
        hex_num = str(hexa)
        hex_list = len(hex_num) - 1
        
        while hex_list >= 0:
            if hex_num[hex_list] >= '0' and hex_num[hex_list] <= '9':
                rem = int(hex_num[hex_list])
            elif hex_num[hex_list] >= 'A' and hex_num[hex_list] <= 'F':
                rem = ord(hex_num[hex_list]) - 55
            elif hex_num[hex_list] >= 'a' and hex_num[hex_list] <= 'f':
                rem = ord(hex_num[hex_list]) - 87
            else:
                chk = 1
                break
            
            dnum += rem * (16 ** i)
            hex_list -= 1
            i += 1

     
        print(dnum)
        return dnum 

    def hex_octal(hexa):
        
        input_str = str(hexa)
        original_input = hexa
        
      
        hex_num = str(input_str)
        chk = i = 0
        deci_num = 0
        hex_len = len(hex_num) - 1
        
        oct_num = ''
        
        while hex_len >= 0:
            if '0' <= hex_num[hex_len] <= '9':
                rem = int(hex_num[hex_len])
            elif 'A' <= hex_num[hex_len] <= 'F':
                rem = ord(hex_num[hex_len]) - 55
            elif 'a' <= hex_num[hex_len] <= 'f':
                rem = ord(hex_num[hex_len]) - 87       
            else:
                chk = 1
                break
            
            deci_num += rem * (16 ** i)
            hex_len -= 1
            i += 1
            
        if chk == 0:
            while deci_num != 0:
                oct_num = str(deci_num % 8) + oct_num
                deci_num = deci_num // 8
        else:
            oct_num = "N/A"
        

        
        print(oct_num)
        return oct_num

    def hex_fraction(hexa):
        
        binary_fraction = ''
        decimal_fraction = 0.0
        octal_fraction = ''
        
        # Hex fraction to binary yup!!
        for digit in hexa:
            binary_digit = bin(int(digit, 16))[2:].zfill(4)
            binary_fraction += binary_digit

        for i in range (len(hexa)):
            decimal_fraction += int(hexa[i], 16) * (16 ** -(i+1))

        decimal_part = decimal_fraction
        for i in range(4):
            decimal_part *= 8
            octal_digit = oct(int(decimal_part))[2:]
            octal_fraction += octal_digit
            decimal_part -= int(decimal_part)
            
        decimal_fraction_str = str(decimal_fraction)
        if decimal_fraction_str.startswith('0.'):
            decimal_fraction_str = decimal_fraction_str[2:]
        
        print(decimal_fraction_str)
        return binary_fraction, decimal_fraction_str, octal_fraction
    
    def twos_hex(hexa):
        
        binary_num = HexaConverter.hex_binary(hexa)
        invert = ''.join('1' if bit == '0' else '0' for bit in binary_num)
        complement = format(int(invert, 2) + 1, 'b')[2:]
        
        octal_num = BinaryConverter.octal(complement)
        decimal_num = HexaConverter.hex_decimal(hexa)
        
        octal_num = int(octal_num)
        if octal_num >= 1000:
            octal_num %= 1000
        else:
            octal_num = octal_num
        
        decimal_num = str(decimal_num)
        decimal_num  = '-' + decimal_num
        octal_num = str(octal_num)
        
        octal_num = '7' * (12 - len(octal_num)) + octal_num
        binary_num = '1' * (16 - len(complement))+ complement
        
        binary_num_spacced = ' '.join([binary_num[i:i+4] for i in range(0, len(binary_num), 4)])
        octal_num_spacced = ' '.join([octal_num[i:i+3] for i in range(0, len(octal_num), 3)])      
        
        return binary_num_spacced, decimal_num, octal_num_spacced


# decimal_number = "10A"
# octal_twos_complement = HexaConverter.twos_hex(decimal_number)
# oc = HexaConverter.hex_binary(decimal_number)
# print("Octal two's complement of", decimal_number, "is:", octal_twos_complement)
# print(oc)
# # input = '8'
# result = OctalConverter.octal_binary(input)
# print("bi", result)
# # hex_converter = HexaConverter()
# # binary_result = hex_converter.hex_binary(-19)
# print("Binary result:", result)


# input_hex = "-10b"
# binary_result = HexaConverter.hex_octal(input_hex)
# print("Octal result:", binary_result)


# hex_converter = HexaConverter()
# binary_result = hex_converter.hex_decimal("-19")
# print("Decimal result:", binary_result)

