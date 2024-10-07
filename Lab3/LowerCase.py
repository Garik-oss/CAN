def analyze_sentence(sentence):
    lowercase = ""
    uppercase = ""
    digits = ""
    non_alphabetics = ""

    for char in sentence:
        if char.islower():
            lowercase += char
        elif char.isupper():
            uppercase += char
        elif char.isdigit():
            digits += char
        elif not char.isalnum():
            non_alphabetics += char

    return lowercase, uppercase, digits, non_alphabetics

user_input = input("Please enter a sentence: ")

lowercase, uppercase, digits, non_alphabetic = analyze_sentence(user_input)

print(f"New sentence: {lowercase + uppercase + digits + non_alphabetic}")
print(f"Count of alphabetics: {len(lowercase) + len(uppercase)}")
print(f"Count of digits: {len(digits)}")
print(f"Count of non-alphabetic symbols: {len(non_alphabetic)}")
