# 901. Online Stock Span

class StockSpanner:

    def __init__(self):
        self.stack=[]

    def next(self, price: int) -> int:
        cnt=1
        while self.stack and self.stack[-1][0] <= price:
            v=self.stack.pop()[1]
            cnt=cnt+v
        self.stack.append((price,cnt))
        return cnt

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)