#! \Local\Programs\Python\Python36\python.exe
# -*- coding: utf-8 -*-
__author__ = '98221254@qq.com'

'''
实现链表
'''


class Node:
    def __init__(self, key, prev=None, next=None):
        self.key = key
        self.prev = prev
        self.next = next


class LinkList:
    def __init__(self):
        self.head = None

    def initLink(self, data):
        self.head = Node(data[0])
        node = self.head
        for i in data[1:]:
            node.next = Node(i, prev=node)
            node = node.next

    def isEmpty(self):
        return self.head == None

    # 求出链表长度
    def size(self):
        node = self.head
        index = 1
        while node.next:
            index += 1
            node = node.next
        return index

    # 查找key为k时，元素在链表中的位置
    def search(self, k):
        if self.isEmpty():
            raise IndexError('链表为空')
        node = self.head
        index = 1
        # 当不是最后一项且key不为k时，向后遍历
        while node.next and node.key != k:
            index += 1
            node = node.next
        if node.key != k:
            return 'not find'
        return index

    # 将node插到链表第index个位置
    # node可以为Node对象，也可以为key值
    def insert(self, node, index=1):
        index = index // 1  # 确保为整数index
        if not isinstance(node, Node):
            node = Node(node)
        # index为1时，node以链表头插入
        if index == 1:
            node.next = self.head
            node.prev = self.head.prev
            self.head = node
        elif index > 1:
            if index > self.size():
                index = self.size()
            start_node = self.head
            for i in range(1, index):
                start_node = start_node.next
            node.next = start_node
            node.prev = start_node.prev
            start_node.prev.next = node
            start_node.prev = node

    # 删除node对象，或者删除key值为node的元素
    def delete(self, node):
        if self.isEmpty():
            raise IndexError('链表为空')
        if isinstance(node, Node):
            node = node.key
        n = self.head.next
        while n and n.key != node:
            n = n.next
        if not n:
            raise IndexError('not find the Node')
        if n == self.head:
            n.next.prev = None
            self.head = n.next
        else:
            n.next.prev = n.prev
            n.prev.next = n.next

        return n.key

    # 遍历链表
    def show(self):
        node = self.head
        while node:
            print(node.key, end=' ')
            node = node.next


l = LinkList()
l.initLink([1, 2, 3, 4])
# l.insert(Node(10))
# print(l.head.key)
ele = l.head.next
l.insert(10, 2)
# rst = l.size()
print(l.show())
