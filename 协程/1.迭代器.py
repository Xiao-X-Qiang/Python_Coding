

class Classmate(object):
    def __init__(self):
        self.name = list()

    def add(self, name):
        self.name.append(name)

    def __iter__(self):
        return Classmate2(self)

class Classmate2(object):
    def __init__(self, obj):
        self.num = 0
        self.obj = obj

    def __iter__(self):
        pass

    def __next__(self):
        if self.num < len(self.obj.name):
            temp = self.obj.name[self.num]
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