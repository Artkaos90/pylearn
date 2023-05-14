if __name__ == '__main__':

    vendor = input()
    fridge_height = int(input())
    fridge_width = int(input())

    is_pass_through_door = fridge_height <=210 and fridge_width <= 90
    is_pass_through_window= fridge_height <=170 and fridge_width <= 320

    if vendor in ("Brr", "SMF") and (is_pass_through_door or is_pass_through_window):
        print("OK")
    else:
        print("NO")