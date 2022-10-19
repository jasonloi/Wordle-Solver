#1 bug found: if you put in the same letter in black in green (which can happen eg. Try "dryer" but word is "elder")
#the code breaks. might have to add conditional statement to find_black (ignore if letter is in green?)
#generally have issue with duplicate letters.
#2nd bug found: the set of english words is british, not american (colour, not color)

from english_words import english_words_lower_set

#make a list of all 5 letter words in english dictionary
five_letter_words = []
for word in english_words_lower_set:
    if len(word) == 5:
        five_letter_words.append(word)

#get user input
print("This program will tell you all the feasible words given the constraints you provide.")
print('Enter GREEN LETTERS: Correct letters and correct place (ex. i2, e4, w1):')
green = input()

print('Enter YELLOW LETTERS: Correct letters and their incorrect place(s) (ex. w2, w3, i1, t1, s5):')
yellow = input()

print('Enter BLACK LETTERS: Incorrect letters (ex. d, x, a):')
black = input()

#turn inputted strings into lists

green = green.split(", ")
yellow = yellow.split(", ")
black = black.split(", ")

print('Green: ' + str(green))
print('Yellow: ' + str(yellow))
print("Black: " + str(black))
counter = 0

#create a list of all words that match the green letter(s)

def find_green(old_list, counter):
    if green[0] == '':
        return five_letter_words
    new_list = []
    if counter == len(green):
        return old_list
    else:
        for word in old_list:
            if green[counter][0] == word[int(green[counter][1])-1]:
                new_list.append(word)
        return find_green(new_list, counter+1)

#create a list of all the words that don't have the black letter(s), starting with the list of words from find_green

def find_black(old_list, counter):
    if black[0] == '':
        return old_list
    new_list = []
    if counter == len(black):
        return old_list
    else:
        for word in old_list:
            if black[counter] not in word:
                new_list.append(word)
        return find_black(new_list, counter+1)

#create a list of all the words that follow the rules for uellow, starting with the list from find_black

def find_yellow(old_list, counter):
    if yellow[0] == '':
        return old_list
    new_list = []
    if counter == len(yellow):
        return old_list
    else:
        for word in old_list:
            if (yellow[counter][0] != word[int(yellow[counter][1])-1]) and (yellow[counter][0] in word):
                new_list.append(word)
        return find_yellow(new_list, counter+1)

green_final = find_green(five_letter_words, 0)
black_final = find_black(green_final, 0)
yellow_final = find_yellow(black_final, 0)
print("Possible Words: " + str(yellow_final))





