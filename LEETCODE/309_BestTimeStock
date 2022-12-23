class Solution(object):
    def maxProfit(self, prices):
        def action(buy,sell,cool,i,curr,path,res):
            if i == len(prices)-1:
                return res.append(path)
            if buy : action(False,True,True,i+1,prices[i],path,res)  #buy
            if sell : action(False,False,True,i+1,0,path+(prices[i]-curr),res) #sell
            if cool: action(buy,sell,cool,i+1,curr,path,res)   #cool
#            if cool and :  action(True,False,True,i+1,curr,path,res) #cool after sell

        res = []
        path = 0
        action(True,False,True,0,0,path,res)
        return max(res)