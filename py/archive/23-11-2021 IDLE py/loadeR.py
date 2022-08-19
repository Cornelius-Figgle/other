import time

def bootLineLoad():
    if __name__ == '__main__':
        for i in range(13):
            b = i % 4
            if (b == 0):
                d = "Booting   "
            elif (b == 1):
                d = "Booting."
            elif (b == 2):
                d = "Booting.."
            elif (b == 3):
                d = "Booting..."
            print("", end=f"\r{d}")
            time.sleep(0.4)
    e = "                "
    print("", end=f"\r{e}")
    
def fadeLine():
    timeFadeLine = 0.01
    if __name__ == '__main__':
        for i in range(24):
            b = "█"*i
            print("", end=f"\r{b}▓▒░")
            time.sleep(timeFadeLine)
            g = i
    b = "█"*g
    print("", end=f"\r▓{b}▓▒░")
    time.sleep(timeFadeLine)
    print("", end=f"\r▒▓{b}▓▒░")
    time.sleep(timeFadeLine)
    print("", end=f"\r░▒▓{b}▓▒░")
    time.sleep(timeFadeLine)
    print("", end=f"\r ░▒▓{b}▓▒░")
    time.sleep(timeFadeLine)
    if __name__ == '__main__':
        for i in range(78):
            c = " "*i
            print("", end=f"\r{c}  ░▒▓{b}▓▒░")
            time.sleep(timeFadeLine)
    e = "                                                                                                                                                "
    print("", end=f"\r{e}")

def bootSymBbLoad():
    if __name__ == '__main__':
        for i in range(53):
            b = i % 4
            if (b == 0):
                d = "⌂$%6*^«⌂ßµΦ‹š╢╝­,⌂Jƒ‹è⌂▄⌠‰áj$Ó»·§⌂vv$▒"
            elif (b == 1):
                d = "╝­*^▄⌠‰áj$Ó»·§⌂▒«,⌂Jƒ‹è⌂$%6⌂ßµΦ‹vv$š╢⌂"
            elif (b == 2):
                d = "‹è⌂▄⌠‰Ó»╝­,⌂Jƒ·§⌂$%vv$▒áj⌂6*^«⌂ßµΦ‹š╢$"
            elif (b == 3):
                d = "$Ó»·§⌂vΦ⌂$%6*^«‰áj‹š╢╝­,⌂Jv$▒⌂ßµƒ‹è⌂▄⌠"
            print("", end=f"\r{d}")
            time.sleep(0.007)
    e = "                                        "
    print("", end=f"\r{e}")
    e = ""
    print("", end=f"\r{e}")
    
def stratStar():
    start = " "
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\\"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\S"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\Sta"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\Star"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\Start"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\Start>"
    print("", end=f"\r{start}")
    time.sleep(0.2)
    start = "<\Start> :"
    print("", end=f"\r{start}")
    time.sleep(0.2)

bootLineLoad()
fadeLine()
bootSymBbLoad()
e = "                                                              "
print("", end=f"\r{e}")
stratStar()
q = input()
print("", end=f"\r{e}\n")
#rest of code

q = input()
