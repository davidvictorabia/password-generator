#password generator
import random
import string

def generate_password():
    print("🔐 Advanced Password Generator")
    print("=" * 40)
    
    length = int(input("Password length (8-32): ") or 16)
    use_upper = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lower = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_symbols = input("Include symbols? (y/n): ").lower() == 'y'
    
    password = generate_password_logic(length, use_upper, use_lower, use_digits, use_symbols)
    print("\n✅ Your Password:", password)

def generate_password_logic(length, upper, lower, digits, symbols):
    chars = ""
    if lower:  chars += string.ascii_lowercase
    if upper:  chars += string.ascii_uppercase
    if digits: chars += string.digits
    if symbols:chars += "!@#$%^&*()_+-="
    
    if not chars:
        chars = string.ascii_letters + string.digits
    
    return ''.join(random.choice(chars) for _ in range(length))


# Run the generator
if __name__ == "__main__":
    generate_password()