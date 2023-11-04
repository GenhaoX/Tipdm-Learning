class myProd():
    def prods(self, x):
        for i in range(1,x+1):
            a = ''
            for j in range(1,i+1):
                a = a+' '+f'{i}*{j}={i*j}'
            print(a)