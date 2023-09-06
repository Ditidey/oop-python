

def do_something(work):
    print('Start the work')
    work()
    print('Done with the work')

def practice_coding():
    print('I am practing python')
def learning_python():
    print('learning python class')

do_something(practice_coding) 
do_something(learning_python) 

def make_something():
    print('Inside the function do_something')
    def innner_function():
        print('Inside the inner function')
    innner_function()

make_something()

def first_function():
    print('Inside the first function')
    def second_function():
        print('Inside the innner function')
    return second_function

first = first_function()
first()
first_function()()







