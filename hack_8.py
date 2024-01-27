"""
list: [1,3,5,7,9] output => [3,5,7]
"""

def fn_hack_8():
    result = [1,3,5,7,9]
    result_sliced = result[1:4]
    return result_sliced

print(fn_hack_8())