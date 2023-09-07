            max_priority = 0
            
            for ind, el in enumerate(opers):
                if get_priority(el) > max_priority:
                    max_priority = get_priority(el)
                    priority_index = ind
            
            
            num1 = nums.pop(priority_index)
            num2 = nums.pop(priority_index)
            oper = opers.pop(priority_index)
            
            # if number in ()
            num1 = parse(num1.strip("()")) if "(" in num1 else num1
            num2 = parse(num2.strip("()")) if "(" in num2 else num2
            
            if DEBUG_MODE:
                print("N1: ", num1)
                print("N2: ", num2)
                print("OP: ", oper)
            
            # insert result into nums
            result = compute(num1, num2, oper)
            nums.insert(priority_index, str(result))

        except IndexError:
            num1 = nums.pop(0)
            num2 = 0
            oper = "+"
            num1 = parse(num1.strip("()")) if "(" in num1 else num1
            nums.insert(0, num1)

    if DEBUG_MODE:
        print("END_NUMS: ", nums)
        print("END_OPERS: ", opers)
    
    # if nums length equal 1 and nums[0] have "(" and ")" then
    if "(" in nums[0] and ")" in nums[0]:
        expr = nums[0].strip("()")
        return parse(expr)
    
    return nums[0]


expr = "(-5+5)*2+(6-7)"
print(f"EXPR: {expr}\nFINAL_RESULT: {parse(expr)}")
