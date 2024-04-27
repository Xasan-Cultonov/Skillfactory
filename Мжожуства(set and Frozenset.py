# data = set('Hello')
data = {6, 5, 6, 7,}

data.add(33)
data.update([32,True,4, "44"] )
data.remove(True)
data.pop()
# data.clear()

nums = [4, 5, 6, 7,]
nums = set(nums)

new_data = frozenset([4, 5, 6, '33', True])



print(new_data)