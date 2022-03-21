import math

plain_text = input("Enter Plain Text: ")
plain_text = plain_text.replace(" ", "")  # remove white space
key = input("Enter key: ")
key = key.replace(" ", "")
sorted_key = sorted(key)
matrix = [[(x + y - ord("a")) % 26 for y in range(26)] for x in range(ord("a"), ord("z") + 1)]


print("Polyalphabetic Cipher Table")
for x in sorted_key:
    row = matrix[ord(x) - ord("a")]
    for col in row:
        print(chr(col + ord("a")), end=" ")
    print("\n")

same_length_key = (key * len(plain_text))[:len(plain_text)]

print("key: ", end=" ")
print([i for i in same_length_key], end=" ")
print("\n")
print("Text: ", end=" ")
print([i for i in plain_text], end=" ")
print("\n")

encrypted = ""
for i in range(len(same_length_key)):
    x = ord(same_length_key[i]) - ord("a")
    y = ord(plain_text[i]) - ord("a")
    encrypted += chr(matrix[x][y] + ord("a"))

print(f"Plain Message: {plain_text}")
print(f"Encrypted Message: {encrypted}")

decrypted = ""
for i in range(len(same_length_key)):
    x = ord(same_length_key[i]) - ord("a")
    y = ord(encrypted[i]) - ord("a")
    decrypted += chr(matrix[x].index(y) + ord("a"))

print(f"Decrypted Message: {decrypted}")
