def key_generation(text, auto_key):
    text = text.upper()
    if len(text) == len(auto_key):
        return auto_key
    else:
        i = 0
        length = len(text)
        while (len(auto_key) < length):
            if "A" <= text[i] <= "Z":
                auto_key += text[i]
                i += 1

            else:
                length -= 1
                i += 1
        return auto_key.upper()


def auto_key_encrypt(text, auto_key):
    key = key_generation(text, auto_key)

    cipher = ""
    text = text.upper()
    j = 0
    for i in range(len(text)):

        if "A" <= text[i] <= "Z":
            ckey = ((ord(key[j]) + ord(text[i])) % 26) + 65

            cipher += chr(ckey)
            j += 1
        else:
            cipher += text[i]
    return cipher


def auto_key_decrypt(cipher_text, auto_key):
    key = auto_key.upper()
    plain_text = ""
    cipher_text = cipher_text.upper()
    j = 0
    for i in range(len(cipher_text)):
        if "A" <= cipher_text[i] <= "Z":
            ckey = ((ord(cipher_text[i]) - ord(key[j]) + 26) % 26) + 65
            plain_text += chr(ckey)
            key += chr(ckey)
            j += 1
        else:

            plain_text += cipher_text[i]

    return plain_text


if __name__ == "__main__":
    print(auto_key_encrypt("Think out of the box!@", "ru"))
    print(auto_key_decrypt("KBBUS BEH IY HMX ISY!@", "ru"))
