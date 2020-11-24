import os
import time


def screenshot(filename):
    os.system(f"adb exec-out screencap -p > {filename}")


def click(x, y):
    os.system(f"adb shell input tap {x} {y}")


def enter_dragon():
    click(900, 300)
    click(1800, 500)
    click(1800, 500)


def enter_battle():
    click(1800, 1000)
    click(1300, 300)

def enter_nogada():
   click(1550, 1000)
   click(1550, 1000)

def solve_block():
    screenshot('test.png')


def click_decks():
    for x in [450, 600, 700]:
        for y in [100, 300, 400, 600]:
            click(x, y)


def close():
    click(1000, 800)


def gold():
    enter_nogada()
    click_decks()
    time.sleep(10)


def item():
    enter_dragon()
    click_decks()
    time.sleep(10)
    close()


if __name__ == '__main__':
    while True:
        # gold()
        item()
