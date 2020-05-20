import string
import pickle
import math
import argparse
import sys


def read_file(filename):
    data = ""
    if filename != '<stdin>':
        try:
            with open(filename, 'rt') as buffer:
                data = buffer.read()
        except IOError:
            print("An IOError has occurred!")
            raise IOError
        except NameError:
            print("input file doesn't exist")
            raise NameError
    else:
        for line in sys.stdin.read().split('\n'):
            data += str(line)
            data += '\n'

    return data


def write_file(filename, obj):
    if filename != '<stdout>':
        try:
            with open(filename, 'wt') as output_file:
                output_file.write(obj)
        except IOError:
            print("An IOError has occured")
            raise IOError
        except NameError:
            print("Output file doesn't exist")
            raise NameError
    else:
        print(obj.strip('\n'))


def encode_caesar(text, alphabet, shift):
    encoded_text = ''
    alphabet_size = len(alphabet)
    text_size = len(text)
    for i in range(text_size):
        index = alphabet.find(text[i])
        if index == -1:
            encoded_text += text[i]
        else:
            new_index = (index + shift) % alphabet_size
            if text[i] == text[i].lower():
                encoded_text += alphabet[new_index].lower()
            else:
                encoded_text += alphabet[new_index].upper()
    return encoded_text


def decode_caesar(text, alphabet, shift):
    return encode_caesar(text, alphabet, -shift)


def shift_list(my_list, steps):
    new_steps = steps % len(my_list)
    return my_list[-new_steps:] + my_list[:-new_steps]


def shift_str(my_str, steps):
    new_steps = steps % len(my_str)
    return my_str[new_steps:] + my_str[:new_steps]


def shift_dict(my_dict, steps):
    keys = list(my_dict.keys())
    values = list(my_dict.values())
    shifted_values = shift_list(values, steps)
    new_dict = {}
    new_dict.update(zip(keys, shifted_values))
    return new_dict


def get_vigenere_square(alphabet):
    square = ()
    alphabet_size = len(alphabet)
    for i in range(alphabet_size):
        tmp_str = shift_str(alphabet, i)
        square += tuple(tmp_str)
    return square


def encode_vigenere(text, alphabet, key_word):
    alphabet_size = len(alphabet)
    text_size = len(text)
    vigenere_square = get_vigenere_square(alphabet)
    encoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for i in range(key_size):
        key_abc_index_arr += tuple(str(alphabet.find(key_word[i])))

    for i in range(text_size):
        text_abc_index = alphabet.find(text[i])
        if text_abc_index == -1:
            encoded_text += text[i]
        else:
            new_index = text_abc_index * alphabet_size + int(key_abc_index_arr[key_index])
            if text[i] == text[i].lower():
                encoded_text += vigenere_square[new_index].lower()
            else:
                encoded_text += vigenere_square[new_index].upper()
            key_index = (key_index + 1) % key_size
    return encoded_text


def decode_vigenere(text, alphabet, key_word):
    alphabet_size = len(alphabet)
    text_size = len(text)
    vigenere_square = get_vigenere_square(alphabet)
    decoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for k in range(key_size):
        key_abc_index_arr += tuple(str(alphabet.find(key_word[k])))

    for i in range(text_size):
        text_abc_index = alphabet.find(text[i])
        if text_abc_index == -1:
            decoded_text += text[i]
        else:
            text_index_in_abc = 0
            for j in range(alphabet_size):
                if vigenere_square[alphabet_size * int(key_abc_index_arr[key_index]) + j] == text[i]:
                    text_index_in_abc = j
                    break

            if text[i] == text[i].lower():
                decoded_text += alphabet[text_index_in_abc].lower()
            else:
                decoded_text += alphabet[text_index_in_abc].upper()
            key_index = (key_index + 1) % key_size

    return decoded_text


def encode(args):
    data = read_file(args.input_file.name)
    abc_str = string.ascii_letters
    new_data = ''
    if args.cipher == 'vigenere':
        new_data = encode_vigenere(data, abc_str, args.key)
    elif args.cipher == 'caesar':
        new_data = encode_caesar(data, abc_str, int(args.key))
    write_file(args.output_file.name, new_data)


def decode(args):
    data = read_file(args.input_file.name)
    abc_str = string.ascii_letters
    new_data = ''
    if args.cipher == 'vigenere':
        new_data = decode_vigenere(data, abc_str, args.key)
    elif args.cipher == 'caesar':
        new_data = decode_caesar(data, abc_str, int(args.key))
    write_file(args.output_file.name, new_data)


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
        raise IOError
    except NameError:
        print("Output file doesn't exist")
        raise NameError
    except pickle.UnpicklingError:
        print("Problems with unpickling file")
        raise pickle.UnpicklingError
    return data


def write_frequency(filename, obj):
    try:
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)
    except IOError:
        print("An IOError has occured")
        raise IOError
    except NameError:
        print("Frequency file doesn't exist")
        raise NameError
    except pickle.PicklingError:
        print("Problems with pickling object")
        raise pickle.PicklingError


def estimate_freq(dict1, dict2):
    diff = 0
    for key in dict1.keys():
        diff += ((dict1.get(key) - dict2.get(key)) ** 2)
    return math.sqrt(diff)


def hack_caesar(text, alphabet, key_file):
    norm_freq_dict = read_frequency(key_file)
    text_freq_dict = count_frequency(text, alphabet)
    needed_shift = 0
    diff = estimate_freq(norm_freq_dict, text_freq_dict)
    for j in range(1, len(alphabet)):
        tmp_dict = shift_dict(text_freq_dict, j)
        tmp_diff = estimate_freq(norm_freq_dict, tmp_dict)
        if diff > tmp_diff:
            diff = tmp_diff
            needed_shift = j

    return encode_caesar(text, alphabet, needed_shift)


def count_freq(args):
    data = read_file(args.input_file.name)
    abc_str = string.ascii_letters
    freq = count_frequency(data, abc_str)
    print(freq)
    write_frequency(args.output_file.name, freq)


def hack(args):
    data = read_file(args.input_file.name)
    abc_str = string.ascii_letters
    new_data = hack_caesar(data, abc_str, args.key_file.name)
    write_file(args.output_file.name, new_data)


def encode_parse(subparsers):
    encode_parser = subparsers.add_parser('encode')
    encode_parser.add_argument('--input_file',
                               type=argparse.FileType('rt'),
                               default=sys.stdin,
                               help='The file with the text which we need to encode')
    encode_parser.add_argument('--output_file',
                               type=argparse.FileType('wt'),
                               default=sys.stdout,
                               help='The file where we put encoded text')
    encode_parser.add_argument('--cipher',
                               type=str,
                               choices=['caesar', 'vigenere'],
                               help='Choose one of the cipher: caesar or vigenere')
    encode_parser.add_argument('--key',
                               type=str,
                               default='0',
                               help='Write the number if you use Caesar\'s code, or the word otherwise')
    encode_parser.set_defaults(func=encode)
    return encode_parser


def decode_parse(subparsers):
    decode_parser = subparsers.add_parser('decode', help='')
    decode_parser.add_argument('--input_file',
                               type=argparse.FileType('rt'),
                               default=sys.stdin,
                               help='The file with the text which we need to decode')
    decode_parser.add_argument('--output_file',
                               type=argparse.FileType('wt'),
                               default=sys.stdout,
                               help='The file where we put decoded text')
    decode_parser.add_argument('--cipher',
                               type=str,
                               choices=['caesar', 'vigenere'],
                               help='Choose one of the cipher: caesar or vigenere')
    decode_parser.add_argument('--key', type=str, default='0',
                               help='Write the number if you use Caesar\'s code, or the word otherwise')
    decode_parser.set_defaults(func=decode)


def freq_parse(subparsers):
    freq_parser = subparsers.add_parser('frequence', help='')
    freq_parser.add_argument('--input_file',
                             type=argparse.FileType('rt'),
                             default=sys.stdin,
                             help='The file with text in which we must calculate the frequency of letters')
    freq_parser.add_argument('--output_file',
                             type=argparse.FileType('wt'),
                             default=sys.stdout,
                             help='The file where we put binary file with the frequency of letters')
    freq_parser.set_defaults(func=count_freq)


def hack_parse(subparsers):
    hack_parser = subparsers.add_parser('hack', help='')
    hack_parser.add_argument('--key_file',
                             type=argparse.FileType('rt'),
                             help='Character frequency file for hacking Caesar’s cipher')
    hack_parser.add_argument('--input_file',
                             type=argparse.FileType('rt'),
                             default=sys.stdin,
                             help='The file with text in which we need to hack')
    hack_parser.add_argument('--output_file',
                             type=argparse.FileType('wt'),
                             default=sys.stdout,
                             help='The file where we put decoded text')
    hack_parser.set_defaults(func=hack)


def get_parser():
    parser = argparse.ArgumentParser(description='code and encode texts')
    subparsers = parser.add_subparsers()

    encode_parse(subparsers)
    decode_parse(subparsers)
    freq_parse(subparsers)
    hack_parse(subparsers)

    return parser


my_parser = get_parser()

if __name__ == "__main__":
    args = my_parser.parse_args()
    args.func(args)
