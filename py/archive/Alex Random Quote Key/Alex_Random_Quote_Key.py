import random
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
        for i in range(43):
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

def welcomeSequence():
    print("\n")
    welText = " "
    print("", end=f"\r{welText}")
    time.sleep(0.2)
    welText = "Welco"
    print("", end=f"\r{welText}")
    time.sleep(0.4)
    welText = "Welcome Use"
    print("", end=f"\r{welText}")
    time.sleep(0.2)
    welText = "Welcome User!"
    print("", end=f"\r{welText}\n\n")
    time.sleep(0.5)
    welText = "This mcah"
    print("", end=f"\r{welText}")
    time.sleep(0.8)
    welText = "This machine will gen"
    print("", end=f"\r{welText}")
    time.sleep(0.5)
    welText = "This machine will generate ra"
    print("", end=f"\r{welText}")
    time.sleep(0.2)
    welText = "This machine will generate random quotes aft"
    print("", end=f"\r{welText}")
    time.sleep(0.4)
    welText = "This machine will generate random quotes after you input a "
    print("", end=f"\r{welText}")
    time.sleep(0.3)
    welText = "This machine will generate random quotes after you input a key"
    print("", end=f"\r{welText}\n")
    time.sleep(0.4)
    validation = str(input("Please now input your pass key: "))
    time.sleep(0.6)
    if not validation:
        print("Error 256: in \"PassKey_Input\" ##see_Docs")
        shutDwon()
    else:
        welText = "Tanhks for yo"
        print("", end=f"\n\r{welText}")
        time.sleep(0.9)
        welText = "Thanks for your co-operat"
        print("", end=f"\r{welText}")
        time.sleep(0.2)
        welText = "Thanks for your co-operation. You may proc"
        print("", end=f"\r{welText}")
        time.sleep(0.1)
        welText = "Thanks for your co-operation. You may proceed "
        print("", end=f"\r{welText}\n\n")
        time.sleep(0.4)

QUOTES = ["Hi there! I am a quote", "I am also a quote", "Don't forget me!", "I am not a quote", "I am a sandwich, sir"]

def random_quote(quotes=None, cycles=1):
    if quotes is None:  # default to use QUOTES
        quotes = QUOTES.copy()  # don't mess with original
    else:
        quotes = quotes.copy()
    for cycle in range(cycles):  # if all quotes used, shuffle again
        random.shuffle(quotes)
        for quote in quotes:
            yield quote

def generateRandom():
    i = random.randint(0, 5)
    for counter, quote in enumerate(random_quote()):
        print(quote)
        if counter == i:
            break
        
def shutDwon():
    print("err")

def closeTimeOut():
    from msvcrt import kbhit, getwch
    def timed_input(prompt, timeout=3):
        print(prompt, end='', flush=True)
        start = time.time()
        response = "                                                                                                                                                "
        while time.time() - start < timeout:
            if kbhit():
                char = getwch()
                if char == '\r':
                    break
                print(char, end='', flush=True)
                response += char
            time.sleep(0.01)
        else:
            response = None
        print()
        return response
    time_limit = 4 # in seconds
    validation = timed_input('\nPlease now input your pass key: ', time_limit)
    if validation == "" or validation is None: #first part doesn't work ¯\_(ツ)_/¯ 
        shutDwon()
    else:
        print("\n")
        generateRandom()
        closeTimeOut()

def bootUp():       
    bootLineLoad()
    fadeLine()
    bootSymBbLoad()
    e = "                                                              "
    print("", end=f"\r{e}")
    stratStar()
    input()

def mainSequ():
    welcomeSequence()
    input()
    generateRandom()
    closeTimeOut()

bootUp()
mainSequ()

input()

