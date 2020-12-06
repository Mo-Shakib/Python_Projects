import inflect
p = inflect.engine()
print(p.number_to_words(int(input())))


# import inflect 
# print(inflect.engine().number_to_words(int(input())))

# import num2word
# x = num2word.to_card(16)

# print(x)

# def Numbers_To_Words (number):
#     dictionary = {'1': "one", '2': "two", '3': "three", '4': "four", '5': "five", '6': "six",
#             '7': "seven", '8': "eight", '9': "nine", '0': "zero"}
#     return "-".join(map(lambda x: dictionary[x], str(number)))


# print(Numbers_To_Words(99))
