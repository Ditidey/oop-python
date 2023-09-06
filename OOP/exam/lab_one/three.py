import pyjokes


def tell_some_jokes():
    my_jokes = pyjokes.get_jokes(language = "en", category = "neutral")
    print(my_jokes)
 
tell_some_jokes()
