def encrypt(text, shift=3):
    """
    Encrypts a string using Caesar Cipher with the specified shift.
    
    Args:
        text (str): The text to encrypt
        shift (int): The number of positions to shift each letter (default: 3)
        
    Returns:
        str: The encrypted text
    """
    result = ""
    
    for char in text:
        if char.isalpha():
            # Determine the ASCII offset based on case (65 for uppercase, 97 for lowercase)
            ascii_offset = 65 if char.isupper() else 97
            
            # Convert to 0-25 range, apply shift, and wrap around with modulo 26
            shifted = (ord(char) - ascii_offset + shift) % 26
            
            # Convert back to ASCII and then to character
            result += chr(shifted + ascii_offset)
        else:
            # Preserve non-alphabetical characters
            result += char
    
    return result

def decrypt(text, shift=3):
    """
    Decrypts a string that was encrypted using Caesar Cipher with the specified shift.
    
    Args:
        text (str): The text to decrypt
        shift (int): The number of positions that were shifted (default: 3)
        
    Returns:
        str: The decrypted text
    """
    # Decryption is just encryption with the negative shift
    return encrypt(text, -shift)

def main():
    # Get input from user
    user_input = input("Enter a message to encrypt: ")
    
    # Encrypt the input
    encrypted = encrypt(user_input)
    print(f"\nEncrypted message: {encrypted}")
    
    # Decrypt the encrypted message
    decrypted = decrypt(encrypted)
    print(f"Decrypted message: {decrypted}")

if __name__ == "__main__":
    main()