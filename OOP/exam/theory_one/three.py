#import re 
s = 'Programming Hero is the best'
words = s.split(" ")
rev_word = [word[::-1] for word in words]
rev_s = " ".join(rev_word)
print(rev_s)
#rev = re.sub('(\w+)', lambda x : x.group()[::-1], s)
#print(rev)


