def make_double(num):
    try:
        num = num * 2
        print(num)
    except:
        print('something wrong')
    finally:
        print('done')
make_double(5)
