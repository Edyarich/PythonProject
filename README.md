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
`python3 main.py decode --input examples/decode/input_vigenere.txt --output examples/decode/output_vigenere.txt --cipher vigenere --key SecretKey`

`python3 main.py decode --input examples/decode/input_caesar.txt --output examples/decode/output_caesar.txt --cipher caesar --key 15`

**3. Hack**
`python3 main.py hack --key examples/hack/symbols_frequency.pickle --input examples/hack/input.txt --output examples/hack/output.txt`

**4. Frequence**
`python3 main.py frequence --input examples/frequence/input.txt`

Console output: {'[': 0.0, "'": 0.21658415841584158, 'a': 3.4344059405940595, 'b': 1.577970297029703, 'c': 0.3919141914191419, 'd': 2.0936468646864688, 'e': 7.353547854785479, 'f': 1.021039603960396, 'g': 0.9900990099009901, 'h': 2.6402640264026402, 'i': 4.135726072607261, 'j': 0.0, 'k': 0.556930693069307, 'l': 2.495874587458746, 'm': 2.6093234323432344, 'n': 2.825907590759076, 'o': 3.78506600660066, 'p': 0.8766501650165016, 'q': 0.0, 'r': 2.4133663366336635, 's': 1.5367161716171618, 't': 3.3828382838283826, 'u': 1.608910891089109, 'v': 1.247937293729373, 'w': 0.721947194719472, 'x': 0.0, 'y': 1.8358085808580857, 'z': 0.0, 'A': 0.0, 'B': 0.0, 'C': 0.0, 'D': 0.0, 'E': 0.0, 'F': 0.0, 'G': 0.0, 'H': 0.0, 'I': 0.0, 'J': 0.0, 'K': 0.0, 'L': 0.0, 'M': 0.0, 'N': 0.0, 'O': 0.0, 'P': 0.0, 'Q': 0.0, 'R': 0.0, 'S': 0.0, 'T': 0.0, 'U': 0.0, 'V': 0.0, 'W': 0.0, 'X': 0.0, 'Y': 0.0, 'Z': 0.0, ',': 3.981023102310231, ' ': 0.0, 'а': 3.424092409240924, 'б': 1.1757425742574257, 'в': 2.8568481848184817, 'г': 0.4744224422442244, 'д': 1.1344884488448845, 'е': 3.3931518151815183, 'ж': 0.5156765676567656, 'з': 0.7735148514851485, 'и': 2.557755775577558, 'й': 0.17533003300330033, 'к': 0.8663366336633663, 'л': 2.8052805280528053, 'м': 1.4335808580858085, 'н': 1.9492574257425743, 'о': 4.507013201320132, 'п': 1.3201320132013201, 'р': 2.0008250825082508, 'с': 2.2483498349834985, 'т': 2.825907590759076, 'у': 1.0622937293729373, 'ф': 0.0, 'х': 0.4434818481848185, 'ц': 0.0721947194719472, 'ч': 0.4537953795379538, 'ш': 0.2887788778877888, 'щ': 0.06188118811881188, 'ъ': 0.0, 'ы': 0.6600660066006601, 'ь': 1.7842409240924093, 'э': 0.05156765676567657, 'ю': 0.525990099009901, 'я': 1.4542079207920793, 'А': 0.0, 'Б': 0.0, 'В': 0.0, 'Г': 0.0, 'Д': 0.0, 'Е': 0.0, 'Ж': 0.0, 'З': 0.0, 'И': 0.0, 'Й': 0.0, 'К': 0.0, 'Л': 0.0, 'М': 0.0, 'Н': 0.0, 'О': 0.0, 'П': 0.0, 'Р': 0.0, 'С': 0.0, 'Т': 0.0, 'У': 0.0, 'Ф': 0.0, 'Х': 0.0, 'Ц': 0.0, 'Ч': 0.0, 'Ш': 0.0, 'Щ': 0.0, 'Ъ': 0.0, 'Ы': 0.0, 'Ь': 0.0, 'Э': 0.0, 'Ю': 0.0, 'Я': 0.0, '!': 0.8147689768976898, '"': 0.0, '#': 0.0, '$': 0.0, '%': 0.0, '&': 0.0, '\\': 0.0, '(': 0.041254125412541254, ')': 0.041254125412541254, '*': 0.0, '+': 0.0, '-': 0.2784653465346535, '.': 1.681105610561056, '/': 0.06188118811881188, ':': 0.041254125412541254, ';': 0.0, '<': 0.0, '=': 0.0, '>': 0.0, '?': 0.0, '@': 0.0, ']': 0.0, '^': 0.0, '_': 0.010313531353135313, '`': 0.0, '{': 0.0, '|': 0.0, '}': 0.0, '~': 0.0}


Бонус: кириллица + знаки препинания

