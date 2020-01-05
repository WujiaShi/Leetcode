class Solution(object):
    def countDigitOne(self, n):

        if n<=0: 
            return 0
        if n<10: 
            return 1
        last = int(str(n)[1:])
        power =  10**(len(str(n))-1)      
        high = int(str(n)[0])
        if high == 1:
            return self.countDigitOne(last) + self.countDigitOne(power-1) + last+1
        else:
            return power+high*self.countDigitOne(power-1) + self.countDigitOne(last)
