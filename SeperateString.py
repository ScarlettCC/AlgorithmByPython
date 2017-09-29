import string
class solution:
    def seperate(self):
        sStr1 = 'ab,cde,fgh,ijk'
        sStr2 = ','
        sStr1 = sStr1[sStr1.find(sStr2) + 1:]
        print sStr1
    def scan(self):
        sStr1 = 'cekjgdklab'
        sStr2 = 'gka'
        nPos = -1
        for c in sStr1:
            if c in sStr2:
                nPos = sStr1.index(c)
                break
        print nPos
    def upperandlower(self,s):
        print s.upper()  #all change to upper
        print s.lower()  #all change to lower
    def joinstring(self):
        delimiter = ','
        mylist = ['Brazil', 'Russia', 'India', 'China']
        str = 'www'
        str2 = 'ww ee rr'
        print delimiter.join(mylist)
        print ' '.join(mylist)
        print ' '.join(str)
        print ' '.join(str2)

s = solution()
s.seperate()
s.scan()
s.upperandlower('SSSuuOpppRRR7773')
s.joinstring()
s.OnlyCharNum('a000aab')