def my_favorite(*items):
    """My favorite menu is."""
    print("\nI'll order my food:")
    for item in items:
        print(" Starter is " + item + " Main is " + item + ' and desert' + item) 
    print("Bone apatite!")

my_favorite('butter and artizan bread ', 'fish', 'cake')