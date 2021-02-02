import string
def checkparens(in_str):
    parens = 0
    brackets = 0
    curlies = 0
    most_recent = []
    for char in in_str:
        if char == '(':
            parens += 1
            most_recent.append('(')
        if char == ')':
            parens -= 1
            if parens < 0 or most_recent.pop() != '(':
                return False
        if char == '[':
            brackets += 1
            most_recent.append('[')
        if char == ']':
            brackets -= 1
            if brackets < 0 or most_recent.pop() != '[':
                return False
        if char == '{':
            curlies += 1
            most_recent.append('{')
        if char == '}':
            curlies -= 1
            if curlies < 0 or most_recent.pop() != '{':
                return False
    if parens == 0 and brackets == 0 and curlies == 0:
        return True
    return False

print(checkparens('(a(b))()()'))
print(checkparens('a(b())'))
print(checkparens(')a(b))'))
print(checkparens('(a(b){c}'))
print(checkparens('(a(b)c})'))
print(checkparens('[(a(b){c})]'))
print(checkparens('(a(b)]{c}'))
print(checkparens(')b('))
print(checkparens('(a[b)c]'))