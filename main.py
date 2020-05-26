# -*- coding: utf-8 -*-
import string
import pickle
import math
import argparse
import sys

from normal_frequency import mid_freq_dict

my_alphabet = (string.ascii_letters,
               "абвгдежзийклмнопрстуфхцчшщъыьэюяАБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ",
               string.punctuation)


def get_sign_type(sign):
    if ('a' <= sign <= 'z') or ('A' <= sign <= 'Z'):
        return 0
    elif ('а' <= sign <= 'я') or ('А' <= sign <= 'Я'):
        return 1
    elif (string.punctuation.find(sign) != -1):
        return 2
    return -1


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


def encode_caesar(text, alphabet_arr, shift):
    encoded_text = ''
    text_size = len(text)
    for i in range(text_size):
        char_type = get_sign_type(text[i])
        if char_type == -1:
            encoded_text += text[i]
        else:
            alphabet_size = len(alphabet_arr[char_type])
            index = alphabet_arr[char_type].find(text[i])
            new_index = (index + shift) % alphabet_size
            if text[i] == text[i].lower():
                encoded_text += alphabet_arr[char_type][new_index].lower()
            else:
                encoded_text += alphabet_arr[char_type][new_index].upper()
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


def get_vigenere_square(alphabet_arr):
    square = ()
    alphabet_size = len(alphabet_arr)
    for j in range(alphabet_size):
        small_square = ()
        small_alphabet_size = len(alphabet_arr[j])
        for i in range(small_alphabet_size):
            tmp_str = shift_str(alphabet_arr[j], i)
            small_square += tuple(tmp_str)

        square += small_square,
    return square


def encode_vigenere(text, alphabet_arr, key_word):
    text_size = len(text)
    vigenere_square = get_vigenere_square(alphabet_arr)
    encoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for i in range(key_size):
        char_type = get_sign_type(key_word[i])
        key_abc_index_arr += char_type if (char_type == -1) else \
            tuple(str(alphabet_arr[char_type].find(key_word[i])))

    for i in range(text_size):
        char_type = get_sign_type(text[i])
        text_abc_index = char_type if (char_type == -1) else alphabet_arr[char_type].find(text[i])
        if text_abc_index == -1:
            encoded_text += text[i]
        else:
            alphabet_size = len(alphabet_arr[char_type])
            new_index = text_abc_index * alphabet_size + int(key_abc_index_arr[key_index])
            if text[i] == text[i].lower():
                encoded_text += vigenere_square[char_type][new_index].lower()
            else:
                encoded_text += vigenere_square[char_type][new_index].upper()
            key_index = (key_index + 1) % key_size
    return encoded_text


def decode_vigenere(text, alphabet_arr, key_word):
    text_size = len(text)
    vigenere_square = get_vigenere_square(alphabet_arr)
    decoded_text = ''
    key_index = 0
    key_size = len(key_word)
    key_abc_index_arr = ()

    for k in range(key_size):
        char_type = get_sign_type(key_word[k])
        key_abc_index_arr += tuple(str(char_type)) if (char_type == -1) else \
            tuple(str(alphabet_arr[char_type].find(key_word[k])))

    for i in range(text_size):
        char_type = get_sign_type(text[i])
        text_abc_index = char_type if (char_type == -1) else alphabet_arr[char_type].find(text[i])
        if text_abc_index == -1:
            decoded_text += text[i]
        else:
            alphabet_size = len(alphabet_arr[char_type])
            text_index_in_abc = 0
            for j in range(alphabet_size):
                if vigenere_square[char_type][alphabet_size * int(key_abc_index_arr[key_index]) + j] == text[i]:
                    text_index_in_abc = j
                    break

            if text[i] == text[i].lower():
                decoded_text += alphabet_arr[char_type][text_index_in_abc].lower()
            else:
                decoded_text += alphabet_arr[char_type][text_index_in_abc].upper()
            key_index = (key_index + 1) % key_size

    return decoded_text


def encode(args):
    data = read_file(args.input_file.name)
    abc_arr = my_alphabet
    new_data = ''
    if args.cipher == 'vigenere':
        new_data = encode_vigenere(data, abc_arr, args.key)
    elif args.cipher == 'caesar':
        new_data = encode_caesar(data, abc_arr, int(args.key))
    write_file(args.output_file.name, new_data)


def decode(args):
    data = read_file(args.input_file.name)
    abc_arr = my_alphabet
    new_data = ''
    if args.cipher == 'vigenere':
        new_data = decode_vigenere(data, abc_arr, args.key)
    elif args.cipher == 'caesar':
        new_data = decode_caesar(data, abc_arr, int(args.key))
    write_file(args.output_file.name, new_data)


def count_frequency(text, alphabet_arr):
    keys = [*my_alphabet]
    freq_dict = dict.fromkeys(str(keys), 0)
    new_text_len = 0
    text_size = len(text)
    for i in range(text_size):
        char_type = get_sign_type(text[i])
        if char_type != -1 and alphabet_arr[char_type].find(text[i].lower()) != -1:
            freq_dict[text[i].lower()] += 1
            new_text_len += 1

    if new_text_len != 0:
        for sign in freq_dict.keys():
            freq_dict[sign] *= (100 / new_text_len)
    return freq_dict


def read_frequency(filename):
    try:
        with open(filename, 'rb') as f:
            data = pickle.load(f)
            # print(data)
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


def hack_caesar(text, alphabet_arr, key_file):
    norm_freq_dict = read_frequency(key_file)
    text_freq_dict = count_frequency(text, alphabet_arr)
    total_alphabet_len = len(alphabet_arr[0]) * len(alphabet_arr[1]) * \
                        len(alphabet_arr[2])
    needed_shift = 0
    diff = estimate_freq(norm_freq_dict, text_freq_dict)
    for j in range(1, total_alphabet_len):
        tmp_dict = shift_dict(text_freq_dict, j)
        tmp_diff = estimate_freq(norm_freq_dict, tmp_dict)
        if diff > tmp_diff:
            diff = tmp_diff
            needed_shift = j

    return encode_caesar(text, alphabet_arr, needed_shift)


def count_freq(args):
    data = read_file(args.input_file.name)
    abc_str = my_alphabet
    freq = count_frequency(data, abc_str)
    print(freq)
    write_frequency(args.output_file.name, freq)


def hack(args):
    data = read_file(args.input_file.name)
    abc_str = my_alphabet
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


if __name__ == "__main__":
    my_parser = get_parser()
    args = my_parser.parse_args()
    args.func(args)
