

class Solution(object):
    #1.使用枚举中心位置的方法
    #时间复杂度：O(n~2)
    def LongSubPali1(self, string):

        length = len(string)
        maxlength = 0
        #定义一个数记录临时长度temp
        for mid in range(1, length-2):
            left = mid - 1
            right = mid + 1
            temp = 1

            while left >= 0 and right < length:
                if string[left] == string[right]:

                    if temp > maxlength:
                        maxlength = temp
                        subStr = string[left:right+1]

                    left -= 1
                    right += 1
                    temp += 2
                else:
                    break
        print(subStr)
    #2.O(N)解法，参考https://www.felix021.com/blog/read.php?2040
    #https://segmentfault.com/a/1190000003914228

    def LongSubPali1(self, string):
        #没有看懂
        print("mancher")
if __name__ == "__main__":
    s = "aayaa1"
    Solution().LongSubPali1(s)
