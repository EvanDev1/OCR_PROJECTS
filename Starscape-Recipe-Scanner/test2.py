def create_whitelist(item_name):
    seen_chars = set()  # Set to keep track of seen characters
    whitelist = ''
    for char in item_name:
        char_lower = char.lower()
        if char_lower not in seen_chars:  # Check if lowercase version of char is not in seen_chars
            seen_chars.add(char_lower)  # Add lowercase char to seen_chars
            seen_chars.add(char_lower.upper())  # Also add uppercase version to seen_chars
            whitelist += char  # Add char to whitelist
    return whitelist

item_name = "Cannon-M III"
whitelist = create_whitelist(item_name)
print(whitelist.lower() + whitelist.upper())