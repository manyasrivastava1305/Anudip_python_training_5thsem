def check_palindrome_and_reverse():
    try:
        user_input = input("Enter a number: ")
        
        num = int(user_input)
        
        reverse_str = user_input[::-1]
        
        print(f"Reverse: {reverse_str}")
        
        if user_input == reverse_str:
            print("Palindrome Number")
        else:
            print("Not a Palindrome Number")
            
    except ValueError:
        print("Invalid input! Please enter a valid integer.")

if __name__ == "__main__":
    check_palindrome_and_reverse()
