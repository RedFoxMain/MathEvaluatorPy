import re

# debug mode True/False
DEBUG_MODE = False

# operator priority
def get_priority(oper):
    priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2}

    return priority[oper]

# get expression from bracket
def get_bracket(text):
    ind = text.index(")")-1
    ind1 = text.index(")")+1
    ind2 = 0
    result = ""
    while text[ind] != "(":
        result += text[ind]
        ind2 = ind
        ind -= 1
    return result, ind1, ind2-1


# method for math stuf
def compute(num1, num2, oper):
    num1 = float(num1)
    num2 = float(num2)
    if oper == "+":
        return num1 + num2
    if oper == "-":
        return num1 - num2
    if oper == "*":
        return num1 * num2
    if oper == "/":
        try:
            return num1 / num2
        except ZeroDivisionError:
            print(f"Нельзя делить {num1} на {num2}")
    return None

# main method 
def parse(expr):
    # if expr is empty return None and print message
    if not expr:
        print("Пустое выражение!")
        return None
    
    # gather numbers like 5 or -5 or 78 etc.
    nums = []
    
    # gather operators like + * /
    opers = []
    
    have_brackets = False
    if not re.search(r"\(.*?\)", expr):
        nums = re.findall(r"-?\d+\.[0-9]+|-?\d+", expr)
        opers = re.findall(r"[+*\/]",expr)
    else:
        have_brackets = True
    
    # if we have - before number we need to put + before -
    for ind, elem in enumerate(nums):
        if "(" not in elem and ")" not in elem:
            if float(elem) < 0:
                if ind != 0:
                    opers.insert(ind - 1, "+")

    if DEBUG_MODE:
        print("BEGIN_NUMS: ", nums)
        print("BEGIN_OPERS: ", opers)
    
    
    while (len(nums) > 1 and len(opers) > 0) or have_brackets:
        try:
            if have_brackets:
                raise IndexError
                
            # get priority
            priority_index = 0
            max_priority = 0
            
            for ind, el in enumerate(opers):
                if get_priority(el) > max_priority:
                    max_priority = get_priority(el)
                    priority_index = ind
            
            
            num1 = nums.pop(priority_index)
            num2 = nums.pop(priority_index)
            oper = opers.pop(priority_index)
            
            if DEBUG_MODE:
                print("N1: ", num1)
                print("N2: ", num2)
                print("OP: ", oper)
            
            # insert result into nums
            result = compute(num1, num2, oper)
            
            nums.insert(priority_index, str(result))

        except IndexError:
            if "(" and ")" in expr:
                part = get_bracket(expr)
                
                exp = expr[:part[2]] + parse(part[0]) + expr[part[1]:]
                nums.append(parse(exp))
                have_brackets = False

    if DEBUG_MODE:
        print("END_NUMS: ", nums)
        print("END_OPERS: ", opers)
    
    if nums:
        return nums[0]


expr = "((((1+1)+1)+1)+1)*0"
print(f"EXPR: {expr}\nFINAL_RESULT: {parse(expr)}")
