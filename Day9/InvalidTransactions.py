class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        n=len(transactions)
        for i in range(n):
            transactions[i]=transactions[i].split(',')
            transactions[i][1]=int(transactions[i][1])
        transactions.sort(key=lambda x:x[1])
        
        res=set()
        for i in range(n):
            j=i+1
            while j<n and (int(transactions[j][1])-int(transactions[i][1]))<=60:
                if transactions[j][0]==transactions[i][0] and transactions[j][3]!=transactions[i][3]:
                    res.add(j)
                    res.add(i)
                j+=1
                
        for i in range(n):
            if int(transactions[i][2])>1000:
                res.add(i)
                
        ans=[]
        for i in res:
            transactions[i][1]=str(transactions[i][1])
            ans.append(",".join(transactions[i]))
            
        return ans