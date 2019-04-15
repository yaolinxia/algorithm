#!/usr/bin/env python
# _*_ coding:utf-8 _*_

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # 返回构造的TreeNode根节点
    def reConstructBinaryTree(self, pre, tin):
        # write code here
        if len(tin) == 0:
            return None
        else:
            root = TreeNode(pre[0])
            slt = tin.index(pre[0])
            root.left = self.reConstructBinaryTree(pre[1:1+slt], tin[:slt])
            root.right = self.reConstructBinaryTree(pre[1+slt:], tin[slt+1:])
        # print(root.val)
        return root


if __name__ == '__main__':

    # pre = TreeNode(1)
    # pre.left = TreeNode(2)
    # pre.left.left = TreeNode(4)
    # pre.left.left.right = TreeNode(7)
    # pre.right = TreeNode(3)
    # pre.right.left = TreeNode(5)
    # pre.right.right = TreeNode(6)
    # pre.right.right.left = TreeNode(8)
    pre = [1, 2, 4, 7, 3,5,6,8]
    tin = [4,7,2,1,5,3,8,6]
    Solution().reConstructBinaryTree(pre, tin)

