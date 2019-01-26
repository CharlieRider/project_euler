"""
Problem: 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
The sum of these multiples is 23.
Find the sum of all the multiples of 3 or 5 below 1000.

"""

class MultiplesUnder:
    """
    Takes a max number and a list of "multiples" and
    returns the sum of all numbers under the max that are a multiple of the list
    """
    def __init__(self, max = 0, multiples = [1]):
        self.max = max
        self.multiples = multiples
        self.rolling_sum = 0

    def __iter__(self):
        self.n = 1
        self.rolling_sum = 0
        return self

    def __next__(self):
        if self.n < self.max:
            if any(self.n % x== 0 for x in self.multiples):
                self.rolling_sum += self.n
            self.n += 1
            return self.rolling_sum
        else:
            raise StopIteration


mults_under = MultiplesUnder(max=1000, multiples =[3,5])
imu = iter(mults_under)

for item in imu:
    pass
print(imu.rolling_sum)
