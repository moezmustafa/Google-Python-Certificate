def initials(phrase):
    words = phrase.split()
    result = [word[0] for word in words]
    for word in words:
        result += "".join(word[0])
    return result

print(initials("Universal Serial Bus")) # Should be: USB
print(initials("local area network")) # Should be: LAN
print(initials("Operating system")) # Should be: OS
print(initials("Stand up and dance!")) # Should be: SAD!
print(initials("Change is inevitable")) # Should be: CI