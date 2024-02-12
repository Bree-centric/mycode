for i in range(99, 0, -1):
    if i == 1:
        print(f"{i} bottle of beer on the wall!")
        print(f"{i} bottle of beer on the wall! {i} bottle of beer! You take one down, pass it around!")
    else:
        print(f"{i} bottles of beer on the wall!")
        print(f"{i} bottles of beer on the wall! {i} bottles of beer! You take one down, pass it around!")

    if i - 1 == 1:
        print(f"{i-1} bottle of beer on the wall!")
    elif i - 1 == 0:
        print("No more bottles of beer on the wall!")
    else:
        print(f"{i-1} bottles of beer on the wall!")
    print()

