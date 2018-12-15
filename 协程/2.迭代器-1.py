

class Classmate(object):
    def __init__(self):
        self.name = list()
        self.num = 0

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        return self

    def __next__(self):
        if self.num < len(self.name):
            temp = self.name[self.num]
            self.num += 1
            return temp
        else:
            raise StopIteration


def main():
    classmate = Classmate()
    classmate.add("张三")
    classmate.add("李四")
    for temp in classmate:
        print(temp)


if __name__ == "__main__":
    main()