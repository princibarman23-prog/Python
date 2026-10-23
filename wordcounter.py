def count_words(text):
    words_list = text.split() 
    return len(words_list)

def main():
    print("--- Simple Word Counter ---")
    
    user_input = input("Enter a sentence or paragraph: ")
    
    total_words = count_words(user_input)
    
    print(f"Your text contains {total_words} words.")

main()
