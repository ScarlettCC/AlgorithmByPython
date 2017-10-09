# -*-coding:utf-8 -*-
class listnode:
    def __init__(self,x=None):
        self.value = x
        self.next = None
    def __del__(self):
        self.value = None
        self.next = None

class Solution:
    def deletenode(self,phead,tobedeleted):
        if phead==None or tobedeleted==None:
            return None
        if phead==tobedeleted && tobedeleted.next ==None:
            tobedeleted.__del__()
            phead.__del__()
        elif tobedeleted.next==None:
            plist=phead
            while plist.next != tobedeleted:
                plist=plist.next
            plist.next=None
            tobedeleted.__del__()
        else:
            plist=tobedeleted.next
            tobedeleted.value = plist.value
            tobedeleted.next=plist.next
            plist.__del__()

