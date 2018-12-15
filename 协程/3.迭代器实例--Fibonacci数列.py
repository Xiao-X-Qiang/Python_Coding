

class Fobanacci(object):
    def __init__(self, nums):
        self.nums = nums
        self.current_count = 0
        self.a = 0
        self.b = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_count < self.nums:
            result = self.a
            self.a, self.b = self.b, self.a + self.b
            self.current_count += 1
            return result
        else:
            raise StopIteration


def main():

  fobanacci = Fobanacci(6)
  for temp in fobanacci:
      print(temp)


if __name__ == "__main__":
    main()