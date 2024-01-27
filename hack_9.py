"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    new_result = []

    for i in result:
        new_result.append(i)
        new_result.append('@')

    return new_result  

r = fn_hack_9()
print(r)