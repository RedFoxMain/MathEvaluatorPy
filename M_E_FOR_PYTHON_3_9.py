import re
import time

brackets_pat = re.compile("\(.*?\)")
opers_pat = re.compile("[+*\/]")

# operator priority
priority = {
        "+": 1,
        "-": 1,
        "*": 2,
        "/": 2
}

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
    return result[::-1], ind1, ind2-1


# method for math stuf
def compute(num1, num2, oper):
    if oper == "+":
        return float(num1) + float(num2)
    elif oper == "-":
        return float(num1) - float(num2)
    elif oper == "*":
        return float(num1) * float(num2)
    elif oper == "/":
        try:
            return float(num1) / float(num2)
        except ZeroDivisionError:
            return "∞"
    return None

# main method 
def evaluate(expr):
    # if expr is empty return None and print message
    if not expr:
        return None
    
    # gather numbers like 5 or -5 or 78 etc.
    nums = []
    
    # gather operators like + * /
    opers = []
    
    have_brackets = False
    if not re.search(brackets_pat, expr):
        opers = re.findall(opers_pat, expr)
        nums = re.split(opers_pat, expr)
    else:
        have_brackets = True
        
    # if we have - before number we need to put + before -
    for ind, elem in enumerate(nums):
        if "(" and ")" not in elem and float(elem) < 0 and ind > 0:
            opers.insert(ind - 1, "+")
    
    while len(nums) > 1 and len(opers) > 0 or have_brackets:
        try:
            if have_brackets:
                raise IndexError
            
            # get priority
            priority_index = 0
            max_priority = 0
            
            for ind, el in enumerate(opers):
                if priority[el] > max_priority:
                    max_priority = priority[el]
                    priority_index = ind
            
            # insert result into nums
            result = compute(nums.pop(priority_index), nums.pop(priority_index), opers.pop(priority_index))
            
            nums.insert(priority_index, str(result))

        except IndexError:
            if "(" and ")" in expr:
                part = get_bracket(expr)
                
                left = part[2]
                mid = part[0]
                right = part[1]
                exp = expr[:left] + evaluate(mid) + expr[right:]
                nums.insert(left, evaluate(exp))
                
                have_brackets = False

    if nums:
        return nums.pop(0)

# example

expr = "((((1+1)+1)+1)+1)*0+5*(2+3)"

t1 = time.perf_counter()
res = evaluate(expr)
t2 = time.perf_counter()
print(f"EXPR: {expr}\nFINAL_RESULT: {res}\nEnd in {t2-t1:.4f}")
