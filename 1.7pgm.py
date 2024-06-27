# 1.7. Write a menu-driven program that performs the following operations on
# strings
# 1.7.1. Check if the String is a Substring of Another String
# 1.7.2. Count Occurrences of Character
# 1.7.3. Replace a substring with another substring
# 1.7.4. Convert to Capital Letters

# Updates to keyboard shortcuts … On Thursday, August 1, 2024, Drive keyboard shortcuts will be updated to give you first-letters navigation.Learn more
def is_substring(s1, s2):
    return s1 in s2

def count_occurrences(s, char):
    return s.count(char)

def replace_substring(s, old, new):
    return s.replace(old, new)

def to_capital_letters(s):
    return s.upper()

def main():
    while True:
        print("\nMenu:")
        print("1. Check if a String is a Substring of Another String")
        print("2. Count Occurrences of a Character")
        print("3. Replace a Substring with Another Substring")
        print("4. Convert to Capital Letters")
        print("5. Exit")
        
        choice = input("Enter your choice  ")
        
        if choice == '1':
            s1 = input("Enter the first string: ")
            s2 = input("Enter the second string: ")
            if is_substring(s2, s1):
                print(f'"{s2}" is a substring of "{s1}".')
            else:
                print(f'"{s2}" is not a substring of "{s1}".')
        
        elif choice == '2':
            s = input("Enter the string: ")
            char = input("Enter the character to count: ")
            count = count_occurrences(s, char)
            print(f'The character "{char}" occurs {count} times in the string.')
        
        elif choice == '3':
            s = input("Enter the original string: ")
            old = input("Enter the substring to be replaced: ")
            new = input("Enter the new substring: ")
            result = replace_substring(s, old, new)
            print(f'The new string is: "{result}"')
        
        elif choice == '4':
            s = input("Enter the string: ")
            result = to_capital_letters(s)
            print(f'The string in capital letters is: "{result}"')
        
        elif choice == '5':
            print("Exiting the program.")
            break
        
        else:
            print("Invalid choice. Please select a number between 1 and 5.")

main()

