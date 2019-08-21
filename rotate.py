def rotate_word(string, key):
    encodeString = ''
    for i in range(len(string)):
        encodeString += encodeChar(string[i], key)
    return encodeString

def encodeChar(character, key):
    character_ascii = ord(character)
    if character.isupper():
        startAt = ord('A')
    elif character.islower():
        startAt = ord('a')
    else: return character
    return chr((character_ascii - startAt + key) % 26 + startAt)
    
print(rotate_word('cheer', 7))
print(rotate_word('melon', -10))
