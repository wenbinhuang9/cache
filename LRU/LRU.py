#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan  3 19:19:11 2020

@author: ben
"""

## this is what I am going to implement today 
## data structure
## 1. without capacity limitation, map, O(1)
## 2. with capacity, add a attribute, visitedtime , sortedMap? 
## 3. linkedlist hashmap? 
class DLinkNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.prev = None
        self.next = None
        
        
class LRUCache(object):       
        
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.query = {}
        self.capacity = capacity
        self.start = DLinkNode(0, 0)
        self.tail = DLinkNode(0, 0)
        self.start.next = self.tail
        self.tail.prev = self.start
        
    def addToHead(self, node):
        mid = self.start.next
        mid.prev = node
        node.next = mid
        node.prev = self.start
        self.start.next = node  
        
    def delNode(self, delNode):
        preNode = delNode.prev
        nextNode = delNode.next
        preNode.next = nextNode
        nextNode.prev = preNode
        
    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.query:
            return -1
        
        node = self.query[key]
        self.delNode(node)
        self.addToHead(node)
        
        return node.val
        

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.query:
            self.query[key].val = value
            self.delNode(self.query[key])
            self.addToHead(self.query[key])           
            return 
        
        curCapacity = len(self.query.keys())
        if curCapacity >= self.capacity:
            delNode = self.tail.prev
            delkey = delNode.key
            self.delNode(delNode)
            del self.query[delkey]
            
        cur = DLinkNode(key, value)
        self.addToHead(cur)
        self.query[key] = cur
            