class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        sum = 0
        for value in nums:
            sum += value
        self.result += num+sum
        return self

    def subt(self, num, *nums):
        sum = 0
        for value in nums:
            sum+=value
        self.result -= num+sum
        return self
        # create an instance:

md = MathDojo()

# to test:
x = md.add(2).add(2,5,1,10,5,2).subt(3,2).subt(3,2).add(2,5,1,10,5,2).subt(3,2).result
# .add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!
