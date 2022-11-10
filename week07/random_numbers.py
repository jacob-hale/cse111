import random 

def append_random_numbers(numbers_list, quantity=1):
    while quantity >= 1:
        numbers_list.append(round(random.uniform(1, 100), 1))
        quantity = quantity - 1

def append_random_words(words_list, quantity=1):
    while quantity >=1:
        possible_words = ["beans", "fortnite", "BeReal", "Brother Birch", "segway"]
        words_list.append(random.choice(possible_words))
        quantity = quantity - 1
    
def main():
    numbers_list = [95.4, 78.4, 42.3]
    words_list = []
    print(numbers_list)
    append_random_numbers(numbers_list)
    print(numbers_list)
    append_random_numbers(numbers_list, 3)
    print(numbers_list)
    print(words_list)
    append_random_words(words_list)
    print(words_list)
    append_random_words(words_list, 3)
    print(words_list)

main()