import string
def check_parens(in_str):
    opens = '([{\'\"'
    closes = ')]}\'\"'
    stack = []
    for char in in_str:
        if char in opens:
            stack.append(opens.index(char))
        if char in closes:
            if stack:
                if stack[-1] == closes.index(char):
                    stack.pop() 
                else:
                    return False
            else: 
                return False   
    return stack == []

print(check_parens('(a(b))()()'))
print(check_parens('a(b())'))
print(check_parens(')a(b))'))
print(check_parens('(a(b){c}'))
print(check_parens('(a(b)c})'))
print(check_parens('[(a(b){c})]'))
print(check_parens('(a(b)]{c}'))
print(check_parens(')b('))
print(check_parens('(a[b)c]'))