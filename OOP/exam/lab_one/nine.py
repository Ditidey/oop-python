

def replace_with(s):
    slipt_s = s.split(" ")
    if slipt_s == "chief":
        slipt_s.replace("chief", "thief")
    elif slipt_s == "superintendent":
        slipt_s.replace("superintendent", "sweeper") 
    elif slipt_s == 'married':
        slipt_s.replace('married', 'left')
    elif slipt_s == 'tried':
        slipt_s.replace('tried', 'died')
    return slipt_s

be_negative= ["chief", "thief", "superintendent", "sweeper", "married", "left", "tried", "died"]
s = "I am the chief of Baghdad. Before that I used to be a superintendent of Bank Asia. Things have changed a lot since Jorina married me. A lot of girls tried to marry me."
make_negative = replace_with(s)
print(make_negative)
