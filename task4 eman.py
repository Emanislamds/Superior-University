#Task 1: LUHN Algorithm
def luhn_algorithm(number):
    number = [int(digit) for digit in str(number)][::-1] 
    total = 0

    for i, digit in enumerate(number):
        if i % 2 == 1:  
            digit *= 2
            if digit > 9: 
                digit -= 9
        total += digit

    return total % 10 == 0

card_number = "4539578763621486"
if luhn_algorithm(card_number):
    print("The card number is valid.")
else:
    print("The card number is invalid.")

#Remove Punctuations from User Input String (Without remove Function)
def remove_punctuation(user_input):
    punctuation = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    result = ""
    for char in user_input:
        if char not in punctuation:
            result += char
    return result
user_input = "Hello, World! How's it going?"
cleaned_string = remove_punctuation(user_input)
print("String without punctuation:", cleaned_string)

#Task 3: Sort Text (Words) in Alphabetical Order (Without sort Function)
def sort_words(text):
    words = text.split()
    n = len(words)
    for i in range(n):
        for j in range(0, n - i - 1):
            if words[j] > words[j + 1]: 
                words[j], words[j + 1] = words[j + 1], words[j]
    return " ".join(words)

text = "banana apple orange mango"
sorted_text = sort_words(text)
print("Sorted words:", sorted_text)
