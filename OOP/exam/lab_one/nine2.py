def replace_with(s):
    x = s.replace('chief', 'thief').replace('superintendent', 'sweeper').replace('married', 'left').replace('tried', 'died')
    return x 
    
be_negative= ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
make_negative = replace_with(s)
print(make_negative)