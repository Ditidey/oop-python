import re

non_alpha = re.compile(':;.,_-/')
def clean_string(text):
    output = non_alpha.sub(text)
    print(output)

s = "p:::::,,,,h;;;;;i,,,,t--r;,;o..N"
clean_string(s)
