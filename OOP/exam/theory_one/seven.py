class SubSet:
    def sub(self, num):
        self.subsetRe([], sorted(num))

    def subsetRe(self, pnum, num):
        if num:
            return self.subsetRe(pnum, num[1:]) + self.subsetRe(pnum + [num[0]], num[1:])
        return [pnum]

print(SubSet().sub([4, 5, 6]))