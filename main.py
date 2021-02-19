import cv2
import random

print("Welcome to the dice rolling simulator")


def main():
    global result
    global play_again

    result = random.randint(1, 6)
    play_again = ""


def play_loop():
    global play_again

    play_again = input("Would you like to roll another dice? (Press y for yes, or n for no)").lower()

    while play_again != "y" and play_again != "n":
        play_again = input("Would you like to roll another dice? (Press y for yes, or n for no)").lower()

    if play_again == "y":
        main()
        roll()
    elif play_again == "n":
        print("Thank you for rolling!")
        quit()


def roll():
    global result
    pic_list = ['dice_one.png', 'dice_two.png', 'dice_three.png', 'dice_four.png', 'dice_five.png', 'dice_six.png']
    input("Press enter to roll the dice: ")
    if result == 6:
        result -= 1
    img = cv2.imread(pic_list[result])
    img_resize = cv2.resize(img, (200, 200))
    win_name = "Result"
    cv2.namedWindow(win_name)
    cv2.moveWindow(win_name, 700, 200)
    cv2.imshow(win_name, img_resize)
    cv2.waitKey(5000)
    cv2.destroyWindow(win_name)
    play_loop()


main()
roll()
