'''
    시간초과의 늪.....오
    1퍼에서만 머물다가 8퍼까지 감
'''

class Goldbach:
    def __init__(self) -> None:
        self.MAX = 1000001
        self.arr = [False if i % 2 == 0 or i < 2 else True for i in range(self.MAX)]
        self.answer = {}


    def makePrimeArr(self) -> None:
        for i in range(3, self.MAX, 2):
            if self.arr[i] == True:
                for j in range(i+i, self.MAX, i):
                    self.arr[j] = False
        return
    
    def run(self, N) -> str:
        ans = 'Goldbach\'s conjecture is wrong.'
        for n in range(3, N//2 + 1, 2):
            if self.arr[n] and self.arr[N - n]:
                ans = '{} = {} + {}'.format(N, n, N - n)
                break

        return ans
    
    def makeAnswer(self) -> None:
        for i in range(6, self.MAX, 2):
            self.answer[i] = self.run(i)
        
        return



gb = Goldbach()
gb.makePrimeArr()
gb.makeAnswer()

while True:
    N = int(input())
    
    if not N:
        break
    
    print(gb.answer[N])