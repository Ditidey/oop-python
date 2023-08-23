
greeting_words = ['hi', 'hello', 'good morning']
bye_word  = ['bye', 'good night', 'take care']
bad_word  = ['dog', 'stupid', 'rascal']

def listen():
    return input('Say something: ')

def decide(command):
    each_word = command.split(' ')
    
    for word in each_word:
        if(word in greeting_words):
             callBack('Hello, nice to meet you')
             break
        
        elif(word in bye_word):
            callBack('Bye, take care')
            break

        elif(word in bad_word):
            callBack('You are not talking well, bye')
            break

def callBack(response):
    print(response)


command = listen()
decide(command)
 