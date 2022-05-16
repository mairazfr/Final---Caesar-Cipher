alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]
import art


def caesar(start_text, shift_amount, crypt_direction):
    output_text = ""
    if crypt_direction == "decode":
        shift_amount *= -1

    for i in start_text:
        if i in alphabet:
            index = alphabet.index(i)
            new_index = index + shift_amount
            output_text += alphabet[new_index]
        else:
            output_text += i
    print(f"The {crypt_direction}d text is {output_text}")


print(art.logo)

end = False
while not end:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, crypt_direction=direction)

    repeat = input(
        "Type 'yes' if you would like to go again, otherwise type 'no'. \n"
    ).lower()
    if repeat == "no":
        end = True
        print("Goodbye")
