How to run project? There are four modes in project

1. Encryption

python3 main.py --input_file <path_1> --output_file <path_2> mode encode --cipher <caesar or vigenere> --key <the number if you use Caesar's code or the word if you use Vigenere's code>

— If you don't enter the cipher then the Caesar code will be selected
— The default value of the key is zero

2. Decryption

python3 main.py --input_file <path_1> --output_file <path_2> mode decode --cipher <caesar or vigenere> --key <the number if you use Caesar's code or the word if you use Vigenere's code>

— If you do not specify the path to the input/output file then the input/output will be through the console
— If you don't enter the cipher then the Caesar code will be selected
— The default value of the key is zero

3. Counting letter frequencies (in percents)

python3 main.py --input_file <path_1> --output_file <path_2>

— If you do not specify the path to the input/output file then the input/output will be through the console

4. Hacking (Caesar's cipher)

python3 main.py --input_file <path_1> --output_file <path_2> hack <path_3>

— If you do not specify the path to the input/output file then the input/output will be through the console
— <path_3> is a path to the binary file in which stores a middle letter frequencies (In the project it is called "symbols_frequency.pickle")

