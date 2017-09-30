# -*- coding:utf-8 -*-
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        serial = ''
        if root is None:
            return '$'
        temp = []
        while temp or root:
            while root:
                serial += str(root.val)+','
                temp.append(root)
                root = root.left
            serial += '$,'
            root = temp.pop()
            root = root.right
        serial = serial[:-1]
        return serial
    def Deserialize(self,s):
        # write code here
        serial = s.split(',')
        tree, spp = self.desrialize_core(serial, 0)
        return tree

    def desrialize_core(self, s, sp):
        if sp >= len(s) or s[sp] == "$":
            return None, sp + 1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.desrialize_core(s, sp)
        node.right, sp = self.desrialize_core(s, sp)
        return node, sp