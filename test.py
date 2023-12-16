import re

def num_check(string):
    text = re.compile(r".*[0-9]$")
    if text.match(string[-1]):
        return True
    else:
        return False
    
print(num_check('Приветствую вас!Что вы желаете выполнить?0'))
print(num_check('Приветствую вас!\nЧто вы желаете выполнить? 0'))
print(num_check('Приветствую вас!\nЧто вы желаете выполнить?1'))