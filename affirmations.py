print('Amazing feedback: ')
name = input("Who are you? ")
known = input("How long have you known this? ")
rating = input("On a scale of 1 to 10, how good do you think you will get? ")

if name == 'David' or name == 'dave':
    print("Hi David!")
else:
    print(f"Nice to meet you, {name}!")

if known == 'along time':
    print("Wow, you've known this for a long time!")
else:
    print("That's great!")

if int(rating) == 10:
    print("You're going to be amazing!")
elif int(rating) >= 7:
    print("You're already pretty good, keep it up!")
else:
    print("Hey David - yeah you thought I wouldn't know who you were because you dint capitalize properly")