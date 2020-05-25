# How to run project?

**1. Encryption**

`python3 main.py encode --input_file <path_1> --output_file <path_2> --cipher <caesar or vigenere> --key <the number if you use Caesar's code or the word if you use Vigenere's code>`

— If you don't enter the cipher then the Caesar code will be selected <br>
— The default value of the key is zero

**2. Decryption**

`python3 main.py decode --input_file <path_1> --output_file <path_2> --cipher <caesar or vigenere> --key <the number if you use Caesar's code or the word if you use Vigenere's code>`

— If you do not specify the path to the input/output file then the input/output will be through the console <br>
— If you don't enter the cipher then the Caesar code will be selected <br>
— The default value of the key is zero

**3. Counting letter frequencies (in percents)**

`python3 main.py frequence --input_file <path_1> --output_file <path_2>`

— If you do not specify the path to the input/output file then the input/output will be through the console

**4. Hacking (Caesar's cipher)**

`python3 main.py hack --key_file <path_1> --input_file <path_2> --output_file <path_3>`

— If you do not specify the path to the input/output file then the input/output will be through the console <br>
— <path_1> is a path to the binary file in which stores a middle letter frequencies (In the project it is called "symbols_frequency.pickle")

___


## Examples

**1. Encode**
`python3 main.py encode --input examples/encode/input.txt --output examples/encode/output_caesar.txt --cipher caesar --key 15`

`python3 main.py encode --input examples/encode/input.txt --output examples/encode/output_vigenere.txt --cipher vigenere --key SecretKey`

**2. Decode**
`python3 main.py decode --input examples/decode/input_vigenere.txt --output examples/decode/output_vigenere.txt --cipher vigenere --key kid`

`python3 main.py decode --input examples/decode/input_caesar.txt --output examples/decode/output_caesar.txt --cipher caesar --key 75`

**3. Hack**
`python3 main.py hack --key examples/hack/symbols_frequency.pickle --input examples/hack/input.txt --output examples/hack/output.txt`

**4. Frequence**
`python3 main.py frequence --input examples/frequence/input.txt`

Console output: {'[': 0.0, "'": 0.9395973154362416, 'a': 8.456375838926174, 'b': 1.9463087248322148, 'c': 1.4093959731543624, 'd': 2.61744966442953, 'e': 10.46979865771812, 'f': 1.2751677852348993, 'g': 3.3557046979865772, 'h': 3.825503355704698, 'i': 6.510067114093959, 'j': 0.5369127516778524, 'k': 0.4697986577181208, 'l': 6.510067114093959, 'm': 5.100671140939597, 'n': 5.906040268456376, 'o': 10.134228187919463, 'p': 1.0067114093959733, 'q': 0.0, 'r': 3.48993288590604, 's': 4.697986577181208, 't': 8.053691275167786, 'u': 2.684563758389262, 'v': 1.0067114093959733, 'w': 1.8120805369127517, 'x': 0.0, 'y': 4.026845637583893, 'z': 0.06711409395973154, 'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'F': 0.0, 'G': 0.0, 'H': 0.0, 'I': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'M': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 'Q': 0.0, 'R': 0.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0, ',': 1.8120805369127517, ' ': 0.0, 'а': 0.0, 'б': 0.0, 'в': 0.0, 'г': 0.0, 'д': 0.0, 'е': 0.0, 'ж': 0.0, 'з': 0.0, 'и': 0.0, 'й': 0.0, 'к': 0.0, 'л': 0.0, 'м': 0.0, 'н': 0.0, 'о': 0.0, 'п': 0.0, 'р': 0.0, 'с': 0.0, 'т': 0.0, 'у': 0.0, 'ф': 0.0, 'х': 0.0, 'ц': 0.0, 'ч': 0.0, 'ш': 0.0, 'щ': 0.0, 'ъ': 0.0, 'ы': 0.0, 'ь': 0.0, 'э': 0.0, 'ю': 0.0, 'я': 0.0, 'А': 0.0, 'Б': 0.0, 'В': 0.0, 'Г': 0.0, 'Д': 0.0, 'Е': 0.0, 'Ж': 0.0, 'З': 0.0, 'И': 0.0, 'Й': 0.0, 'К': 0.0, 'Л': 0.0, 'М': 0.0, 'Н': 0.0, 'О': 0.0, 'П': 0.0, 'Р': 0.0, 'С': 0.0, 'Т': 0.0, 'У': 0.0, 'Ф': 0.0, 'Х': 0.0, 'Ц': 0.0, 'Ч': 0.0, 'Ш': 0.0, 'Щ': 0.0, 'Ъ': 0.0, 'Ы': 0.0, 'Ь': 0.0, 'Э': 0.0, 'Ю': 0.0, 'Я': 0.0, '!': 0.20134228187919462, '"': 0.0, '#': 0.0, '$': 0.0, '%': 0.0, '&': 0.0, '\\': 0.0, '(': 0.1342281879194631, ')': 0.1342281879194631, '*': 0.0, '+': 0.0, '-': 1.0738255033557047, '.': 0.20134228187919462, '/': 0.0, ':': 0.0, ';': 0.0, '<': 0.0, '=': 0.0, '>': 0.0, '?': 0.1342281879194631, '@': 0.0, ']': 0.0, '^': 0.0, '_': 0.0, '`': 0.0, '{': 0.0, '|': 0.0, '}': 0.0, '~': 0.0}



Бонус: кириллица + знаки препинания

