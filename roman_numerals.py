def cleanup(str):
    return list(filter(lambda x : x != " ", str.upper()))

def get_roman_val(n):
    match n:
        case "M":
            return 1000
        case "D":
            return 500
        case "C":
            return 100
        case "L":
            return 50
        case "X":
            return 10
        case "V":
            return 5
        case "I":
            return 1
        case _ :
            raise ValueError("Invalid character entered")

def str_to_num(roman_list):
    if len(roman_list) == 1:
        [get_roman_val(roman_list[0])]
    else:
        [get_roman_val(roman_list[0])] + str_to_num(roman_list[1:])     
  
def confirm_order(roman_list):
    if len(roman_list) == 1:
        return True
    else:
        digit = roman_list[0]
        next_digit = roman_list[1]
        cond_i = digit == 1 and next_digit <= 10
        cond_x = digit == 10 and next_digit <= 100
        cond_c = digit == 100 and next_digit <= 1000
        cond_1 = cond_i or cond_x or cond_c
        cond_2 = len(list(filter(lambda num : next_digit < num, roman_list[2:]))) == 0
        if digit >= next_digit or (cond_1 and cond_2):
            return confirm_order(roman_list[1:])
        else: 
            return False 

def confirm_characters(roman_list):
    found_characters = {"M": 0, "D": 0, "C": 0, "L": 0, "X": 0, "V": 0,"I": 0}
    characters_4 = ["M", "C", "X","I"]
    characters_1 = ["D", "L", "V"]
    for i in range(0, len(roman_list)):
        match roman_list[i]:
            case 1000:
                found_characters["M"] = found_characters["M"] + 1
            case 500:
                found_characters["D"] = found_characters["D"] + 1
            case 100:
                found_characters["C"] = found_characters["C"] + 1
            case 50:
                found_characters["L"] = found_characters["L"] + 1
            case 10:
                found_characters["X"] = found_characters["X"] + 1
            case 5:
                found_characters["V"] = found_characters["V"] + 1
            case 1:
                found_characters["I"] = found_characters["I"] + 1
            case _ :
                raise ValueError("Invalid character entered")
    for c in characters_4:
        if found_characters[c] > 4:
            return False
    for c in characters_1:
        if found_characters[c] > 1:
            return False
    return True

def roman_to_arabic(roman_list):
    digit = roman_list[0]
    if len(roman_list) == 1:
        return digit
    else:
        next_digit = roman_list[1]
        if digit < next_digit:
            return roman_to_arabic(roman_list[1:]) - digit
        else:
            return roman_to_arabic(roman_list[1:]) + digit

def test_max(num):
    return num >= 4000

def to_arabic(str):
    roman_list = cleanup(str)
    for i in range(0, len(roman_list)):
        roman_list[i] = get_roman_val(roman_list[i])
    if confirm_order(roman_list) and confirm_characters(roman_list):
        conversion = roman_to_arabic(roman_list)
        if test_max(conversion):
            raise ValueError("Maximum Roman numeral is MMMCMXCIX")
        else: 
            return conversion
    else:
        raise ValueError("Invalid input")

def to_roman(num):
    if test_max(num):
        raise ValueError("Maximum number that can be represented is 3999")
    else:
        result = ""

        for i in range(0, int(num / 1000)):
            result = result + "M"
        num = num % 1000

        hundreds = int(num / 100)
        if hundreds == 9:
            result = result + "CM"
        elif hundreds >= 5:
            result = result + "D"
            for i in range(0, hundreds - 5):
                result = result + "C"
        elif hundreds == 4:
            result = result + "CD"
        else:
            for i in range(0, hundreds):
                result = result + "C"
        num = num % 100

        tens = int(num / 10)
        if tens == 9:
            result = result + "XC"
        elif tens >= 5:
            result = result + "L"
            for i in range(0, tens - 5):
                result = result + "X"
        elif tens == 4:
            result = result + "XL"
        else:
            for i in range(0, tens):
                result = result + "X"
        num = num % 10

        if num == 9:
            result = result + "IX"
        elif num >= 5:
            result = result + "V"
            for i in range(0, num - 5):
                result = result + "I"
        elif num == 4:
            result = result + "IV"
        else:
            for i in range(0, num):
                result = result + "I"

        return result