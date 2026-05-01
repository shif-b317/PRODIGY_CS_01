def caesar_cipher(text, shift,mode):
    result=""
    shift=shift%26
    for char in text:
        if char.isalpha():
            base=ord('A') if char.isupper() else ord('a')
            offset=shift if mode=='encrypt' else -shift
            result+=chr((ord(char)-base+offset)%26+base)
        else:
            result+=char
    return result
while True:
    message=input("Enter message: ")
    if message.lower()=='exit':
        print("Exiting...")
        break
    try:
        shift_value=int(input("Enter shift number: "))
    except ValueError:
        print("Invalid input")
        continue
    mode=input("Enter mode: 'encrypt' or 'decrypt': ").lower().strip()
    if mode not in ['encrypt','decrypt']:
        print("Invalid input. please choose 'encrypt' or 'decrypt' \n ")
        continue
    output=caesar_cipher(message,shift_value,mode)
    print("Result: ",output)
    print("Type 'exit' to quit \n")