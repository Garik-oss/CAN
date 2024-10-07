vowels = "aeiouAEIOU"

def separate_vowels_and_consonants(sentence):
    consonants = ""
    vowel_list = ""

    for char in sentence:
        if char.isalpha():
            if char in vowels:
                vowel_list += char
            else:
                consonants += char

    return vowel_list, consonants

user_input = input("Please enter a sentence: ")

vowels, consonants = separate_vowels_and_consonants(user_input)

print(f"Vowels: {vowels}, count: {len(vowels)}")
print(f"Consonants: {consonants}, count: {len(consonants)}")
