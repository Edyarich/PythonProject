import string
import pickle
import math
from get_parser import parser


def find_mode(buf):
    mode = 3
    if buf.find('key_file') != -1:
        mode = 4
    elif buf.find('my_mode') != -1:
        if buf.find('encode') != -1:
            mode = 1
        elif buf.find('decode') != -1:
            mode = 2

    return mode


def read_file(filename):
    if filename != '<stdin>':
        try:
            with open(filename, 'rt') as buffer:
                data = buffer.read()
        except IOError:
            print("An IOError has occurred!")
            data = ""
        except NameError:
            print("input file doesn't exist")
            data = ""
    else:
        data = str(input())
    return data


def write_file(filename, obj):
    if filename != '<stdout>':
        try:
            with open(filename, 'wt') as output_file:
                output_file.write(obj)
        except IOError:
            print("An IOError has occured")
        except NameError:
            print("Output file doesn't exist")
    else:
        print(obj)


def encode_caesar(text, alphabet, shift):
    encoded_text = ''
    alphabet_size = len(alphabet)
    for i in range(len(text)):
        index = alphabet.find(text[i])
        if index == -1:
            encoded_text += text[i]
        else:
            encoded_text += alphabet[(index + shift) % alphabet_size]
    return encoded_text


def decode_caesar(text, alphabet, shift):
    return encode_caesar(text, alphabet, -shift)


def shift_str(string, steps):
    length = len(string)
    shifted_str = ""
    if steps == 0:
        return string
    else:
        for i in range(length):
            shifted_str += string[(i + steps) % length]
    return shifted_str


def shift_list(my_list, steps):
    copy_list = my_list
    if steps < 0:
        steps = abs(steps)
        for i in range(steps):
            copy_list.append(copy_list.pop(0))
    else:
        for i in range(steps):
            copy_list.insert(0, copy_list.pop())
    return copy_list


def shift_dict(my_dict, steps):
    i = 0
    new_dict = my_dict.copy()
    values = []
    for value in my_dict.values():
        values.append(value)

    shifted_values = shift_list(values, steps)

    for key in new_dict.keys():
        new_dict[key] = shifted_values[i]
        i += 1
    return new_dict


def get_vigenere_square(alphabet):
    square = ()
    for i in range(len(alphabet)):
        tmp_str = shift_str(alphabet, i)
        square += tuple(tmp_str)
    return square


def encode_vigenere(text, alphabet, key_word):
    alphabet_size = len(alphabet)
    vigenere_square = get_vigenere_square(alphabet)
    encoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for i in range(key_size):
        key_abc_index_arr += tuple(str(alphabet.find(key_word[i])))

    for i in range(len(text)):
        text_abc_index = alphabet.find(text[i])
        if text_abc_index == -1:
            encoded_text += text[i]
        else:
            encoded_text += vigenere_square[text_abc_index * alphabet_size + int(key_abc_index_arr[key_index])]
            key_index = (key_index + 1) % key_size
    return encoded_text


def decode_vigenere(text, alphabet, key_word):
    alphabet_size = len(alphabet)
    vigenere_square = get_vigenere_square(alphabet)
    decoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for k in range(key_size):
        key_abc_index_arr += tuple(str(alphabet.find(key_word[k])))

    for i in range(len(text)):
        text_abc_index = alphabet.find(text[i])
        if text_abc_index == -1:
            decoded_text += text[i]
        else:
            text_index_in_abc = 0
            for j in range(alphabet_size):
                if vigenere_square[alphabet_size * int(key_abc_index_arr[key_index]) + j] == text[i]:
                    text_index_in_abc = j
                    break

            decoded_text += alphabet[text_index_in_abc]
            key_index = (key_index + 1) % key_size

    return decoded_text


def count_frequency(text, alphabet):
    freq_dict = dict.fromkeys(alphabet.lower(), 0)
    text_length = 0
    for i in range(len(text)):
        if alphabet.find(text[i].lower()) != -1:
            freq_dict[text[i].lower()] += 1
            text_length += 1

    if text_length != 0:
        for sign in freq_dict.keys():
            freq_dict[sign] *= (100 / text_length)
    return freq_dict


def read_frequency(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
    except IOError:
        print("An IOError has occured")
    except NameError:
        print("Output file doesn't exist")
    except pickle.UnpicklingError:
        print("Problems with unpickling file")
    return data


def write_frequency(filename, obj):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)
    except IOError:
        print("An IOError has occured")
    except NameError:
        print("Frequency file doesn't exist")
    except pickle.PicklingError:
        print("Problems with pickling object")


def estimate_freq(dict1, dict2):
    diff = 0
    for key in dict1.keys():
        diff += pow((dict1.get(key) - dict2.get(key)), 2)
    return math.sqrt(diff)


def hack_caesar(text, alphabet, key_file):
    norm_freq_dict = read_frequency(key_file)
    text_freq_dict = count_frequency(text, alphabet)
    needed_shift = 0
    diff = estimate_freq(norm_freq_dict, text_freq_dict)
    for j in range(1, len(alphabet)):
        tmp_dict = shift_dict(text_freq_dict, j)
        tmp_diff = estimate_freq(norm_freq_dict, tmp_dict)
        if diff >= tmp_diff:
            diff = tmp_diff
            needed_shift = j

    return encode_caesar(text, alphabet, needed_shift)


args = parser.parse_args()
data = read_file(args.input_file.name)
abc_str = string.ascii_letters
alphabet_len = len(abc_str)
new_data = ''
mode = find_mode(str(args))

if mode == 1:
    if args.cipher == 'vigenere':
        new_data = encode_vigenere(data, abc_str, args.key)
    elif args.cipher == 'caesar':
        new_data = encode_caesar(data, abc_str, int(args.key))
    write_file(args.output_file.name, new_data)
elif mode == 2:
    if args.cipher == 'vigenere':
        new_data = decode_vigenere(data, abc_str, args.key)
    elif args.cipher == 'caesar':
        new_data = decode_caesar(data, abc_str, int(args.key))
    write_file(args.output_file.name, new_data)
elif mode == 3:
    freq = count_frequency(data, abc_str)
    write_frequency(args.output_file.name, freq)
elif mode == 4:
    new_data = hack_caesar(data, abc_str, args.key_file.name)
    write_file(args.output_file.name, new_data)
