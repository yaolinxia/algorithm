"""
思路1：定义两个指针，分别指向头尾。然后依次向中间遍历
思路2：从中间朝两头扫描，直到遍历至头以及尾
"""
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def isPalindrome(self, string):
        head = 0
        tail = len(string) - 1
        while head < tail:
            if string[head] != string[tail]:
                return False
            else:
                head += 1
                tail -= 1
        return True

    def isPalindrome2(self, string):
        #定义中间的指针，区分奇偶，如果是奇数，中间数的两边开始
        length = len(string)
        #偶数判断
        if length%2 == 0:
            head = length//2-1
            tail = length//2
        if length % 2 == 1:
            head = length//2-1
            tail = length//2+1

        while head >= 0 and tail <= length-1:

            if string[head] != string[tail]:
                return False
            else:
                head -= 1
                tail += 1
        return True
    """
    例子：
    1、判断一条单向链表是不是“回文” 
     分析：对于单链表结构，可以用两个指针从两端或者中间遍历并判断对应字符是否相等。但这里的关键就是如何朝两个方向遍历。
     由于单链表是单向的，所以要向两个方向遍历的话，可以采取经典的快慢指针的方法，即先位到链表的中间位置，
     再将链表的后半逆置，最后用两个指针同时从链表头部和中间开始同时遍历并比较即可。 
     
    2、判断一个栈是不是“回文” 
     分析：对于栈的话，只需要将字符串全部压入栈，然后依次将各字符出栈，这样得到的就是原字符串的逆置串，
     分别和原字符串各个字符比较，就可以判断了。 
    """
    #针对单链表的回文判断
    def case1(self, head):
        if not head and not head.next:
            return True

        new_list = []

        #快慢指针法找链表的中点
        slow = fast = head
        while fast and fast.next:
            new_list.insert(0, slow.val)
            slow = slow.next
            fast = fast.next.next

        if fast: #链表有奇数个节点
            slow = slow.next

        for val in new_list:
            if val != slow.val:
                return False
            slow = slow.next
        return True

    #对于列表是栈的判断， 需要定义出栈的操作，
    def case2(self, l):
        length = len(l)
        subl = []
        for i in range(length-1, -1, -1):
            subl.append(l[i])
        if subl == l:
            print("True")
            return True
        else:
            print("False")

    def is_p(self, s):
        head = 0
        tail = len(s)-1
        while head < tail:
            if s[head] == s[tail]:
                head += 1
                tail -= 1
            else:
                print('False')
                break
        if head >= tail:
            print("True")


if __name__ == "__main__":
    s = "abcdba"
    Solution().is_p(s)
    # print(Solution().isPalindrome(s))
    # print(Solution().isPalindrome2(s))
    #
    # l = ListNode(1)
    # l.next = ListNode(2)
    # l.next.next = ListNode(1)
    # l.next.next.next = ListNode(1)
    # print(Solution().case1(l))
    #
    # print("==========================================================")
    # li = [1, 2, 3, 3, 21, 1]
    # Solution().case2(li)

