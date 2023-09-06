
def replace_comma_with_space(text):
    space_string = ' '.join(i for i in text.split(','))
    return space_string

s = "I,have,been,practising,python,since,the,course,stared"
output = replace_comma_with_space(s)
print(output)