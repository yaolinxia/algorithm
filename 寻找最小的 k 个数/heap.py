
class Solution(object):
    def heap(self, l):
        print(l)


    #上浮操作
    def Shift_up(self, i, l):
        while i // 2 >= 1:
            if l[i] < l[i // 2]:
                l[i], l[i // 2] = l[i // 2], l[i]
                