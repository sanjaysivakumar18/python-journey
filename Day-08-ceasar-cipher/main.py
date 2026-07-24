alphabet="abcdefghijklmnopqrstuvwxyz"
direction=input("Encode or decode?").lower()
text=input("message: ").lower()
shift=int(input("Shift number: "))
def ceasar(start_text,shift_amount,cipher_direction):
    result=""
    if cipher_direction=="decode":
        shift_amount*=-1
    for letter in start_text:
        if letter in alphabet:
            position=alphabet.index(letter)
            new_position=(position+shift_amount)%26
            result+=alphabet[new_position]
        else:
            result+=letter
        
    print(f"Result:{result}")
ceasar(text,shift,direction)

