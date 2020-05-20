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

Console output: {'a': 8.866995073891625, 'b': 2.0408163265306123, 'c': 1.477832512315271, 'd': 2.7445460942997886, 'e': 10.978184377199154, 'f': 1.3370865587614356, 'g': 3.5186488388458828, 'h': 4.011259676284307, 'i': 6.826178747361013, 'j': 0.5629838142153413, 'k': 0.4926108374384236, 'l': 6.826178747361013, 'm': 5.348346235045742, 'n': 6.192821956368754, 'o': 10.626319493314567, 'p': 1.0555946516537649, 'q': 0.0, 'r': 3.659394792399718, 's': 4.926108374384236, 't': 8.444757213230119, 'u': 2.8149190710767065, 'v': 1.0555946516537649, 'w': 1.9000703729767767, 'x': 0.0, 'y': 4.2223786066150595, 'z': 0.07037297677691766}

Бонусов нет.

