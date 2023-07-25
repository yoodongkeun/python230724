# function3.py

def union(*ar):
    result =[]
    for item in ar:
        for x in item:
            if x not in result:
                result.append(x)
    return result

print(union("HAM", "SPAM"))
print(union("HAM", "SPAM", "EGG"))

