class make_pair:
    def do_sum(self, num, targ_nums):
        sign = {}
        for i, nums in enumerate(num):
            if targ_nums - nums in sign:
                return (sign[targ_nums - nums], i+1)
            sign[nums] = i+1

print("%d %d" % make_pair().do_sum((10, 20, 10, 40, 50, 60, 70), 50))

