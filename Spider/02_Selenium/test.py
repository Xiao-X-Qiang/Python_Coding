
import time,json

def test():

    with open("11.txt",'w',encoding="utf8") as f:
        while True:
            f.write(json.dumps("1111"))
            f.write("\n")
            time.sleep(1)


test()
