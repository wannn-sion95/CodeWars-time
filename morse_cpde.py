MORSE_CODE = {
    ".-": "A", "-...": "B", "-.-.": "C", "-..": "D", ".": "E", "..-.": "F", "--.": "G", "....": "H",
    "..": "I", ".---": "J", "-.-": "K", ".-..": "L", "--": "M", "-.": "N", "---": "O", ".--.": "P",
    "--.-": "Q", ".-.": "R", "...": "S", "-": "T", "..-": "U", "...-": "V", ".--": "W", "-..-": "X",
    "-.--": "Y", "--..": "Z",
    "-----": "0", ".----": "1", "..---": "2", "...--": "3", "....-": "4", ".....": "5", "-....": "6",
    "--...": "7", "---..": "8", "----.": "9",
    "...---...": "SOS", "-.-.--": "!", ".-.-.-": ".", "--..--": ","
}

def decode_morse(morse_code: str) -> str:
    words = morse_code.strip().split("   ")  # Pisahkan berdasarkan 3 spasi (antar kata)
    decoded_words = []
    
    for word in words:
        decoded_chars = [MORSE_CODE[char] for char in word.split(" ") if char in MORSE_CODE]
        print("------------------")
        print("Hasil Terjemahan: ")
        print("------------------")
        decoded_words.append("".join(decoded_chars))
    
    return " ".join(decoded_words)  # Gabungkan kata dengan satu spasi

# Contoh Penggunaan
print(decode_morse(input("Masukkan code morse: ")))
