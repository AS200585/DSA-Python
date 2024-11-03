from collections import deque

wdc_stock_price = []
wdc_stock_price.insert(0, 213)
wdc_stock_price.insert(1, 215.7)
wdc_stock_price.insert(2, 221.3)
wdc_stock_price.insert(3, 208.9)
wdc_stock_price.insert(4, 209.8)
print(wdc_stock_price)
wdc_stock_price.pop()
print(wdc_stock_price)


q = deque()
q.appendleft(3)
q.appendleft(6)
q.appendleft(2)
q.appendleft(5)
print(q)
q.pop()
print(q)