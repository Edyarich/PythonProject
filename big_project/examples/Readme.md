**1. Encode**
`python3 main.py encode --input input.txt --output output_caesar.txt --cipher caesar --key 15`

`python3 main.py encode --input input.txt --output output_vigenere.txt --cipher vigenere --key SecretKey`

**2. Decode**
`python3 main.py decode --input input_vigenere.txt --output output_vigenere.txt --cipher vigenere --key kid`

`python3 main.py decode --input input_caesar.txt --output output_caesar.txt --cipher caesar --key 75`

**3. Hack**
`python3 main.py hack --key symbols_frequency.pickle --input input.txt --output output.txt`

**4. Frequence**
`python3 main.py frequence --input input.txt`
Console output: {'a': 8.866995073891625, 'b': 2.0408163265306123, 'c': 1.477832512315271, 'd': 2.7445460942997886, 'e': 10.978184377199154, 'f': 1.3370865587614356, 'g': 3.5186488388458828, 'h': 4.011259676284307, 'i': 6.826178747361013, 'j': 0.5629838142153413, 'k': 0.4926108374384236, 'l': 6.826178747361013, 'm': 5.348346235045742, 'n': 6.192821956368754, 'o': 10.626319493314567, 'p': 1.0555946516537649, 'q': 0.0, 'r': 3.659394792399718, 's': 4.926108374384236, 't': 8.444757213230119, 'u': 2.8149190710767065, 'v': 1.0555946516537649, 'w': 1.9000703729767767, 'x': 0.0, 'y': 4.2223786066150595, 'z': 0.07037297677691766}
