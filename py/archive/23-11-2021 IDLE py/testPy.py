import time

if __name__ == '__main__':
    for i in range(23):
        b = i % 4
        if (b == 0):
            d = "- "
        else:
            if (b == 1):
                d = "\ "
            elif (b == 2):
                d = "| "
            elif (b == 3):
                d = "/ "
        print("", end=f"\r{d}")
        #print("d is",d,"i is",i,"b is",b)
        time.sleep(0.1)

q = input("")

if __name__ == '__main__':
    for i in range(11):
        b = " "*i
        print("", end=f"\r{b}.")
        time.sleep(0.1)

q = input("")

if __name__ == '__main__':
    for i in range(101):
        print("", end=f"\r  {i}%")
        time.sleep(0.1)

q = input("")
