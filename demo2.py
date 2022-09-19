def solution1():
    s = "-1 -2 -3 -4"
    t = sorted(list(map(int,s.split(" "))))
    return "{} {}".format(t[0],t[len(t)-1])

def solution2():
    s = "3people unFollowed me"
    t = s.split(" ")
    

    for te in t:
        print(ord(te[0]))
  

solution2()

   
