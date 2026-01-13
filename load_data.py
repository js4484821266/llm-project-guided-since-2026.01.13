import os

pwd = "./data/"
t = os.listdir(pwd)
DATA = dict()
for i in t:
    f = open(os.path.join(pwd, i), "rt", encoding="utf-8")
    r = f.readlines()
    f.close()
    r = [x.strip() for x in r]
    r = [x for x in r if x]
    DATA[i] = r
if __name__ == "__main__":
    print(DATA)
