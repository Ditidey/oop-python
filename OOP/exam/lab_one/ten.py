def creat_new_string(s):
    x = s.split(("oh")[-1]).split(("Emelia")[-1]).split(("to")[-1])
    return x

a = ['oh', 'Emelia', 'to']

s = "Oh, I got two tickets for Dhaka. I and Emelia love to visit different places very much. This time we are going to Bangladesh."
output = creat_new_string(s)
print(" ".join(output))