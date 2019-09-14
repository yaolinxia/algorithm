#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class Solution:
    def min_prac(self, S):
        """
        :type S: str
        :rtype: int
        """
        res = []
        for i in range(len(S)):
            if S[i] == '[':
                res.append(S[i])
            elif S[i] == ']':
                if res:
                    if res[-1] == '[':
                        res.pop()
                    else:
                        res.append(S[i])
                else:
                    res.append(S[i])
        return len(res)

import sys
if __name__ == '__main__':
    # s = "[[][["
    s = sys.stdin.readline().strip('\n')
    print(Solution().min_prac(s))
