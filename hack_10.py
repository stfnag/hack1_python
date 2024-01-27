"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    ls2=[]
    lista=[]
    result = "fooziman"
    lista.append(result.replace("fooziman","F00Z1M@N"))
    ls2 = list(lista[0])
    return ls2

r = fn_hack_10()
print(r)