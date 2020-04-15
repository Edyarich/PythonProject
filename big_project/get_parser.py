import argparse
import sys

parser = argparse.ArgumentParser(description='code and encode texts')
parser.add_argument('--input_file', type=argparse.FileType('rt'), default=sys.stdin,
                    help='The file with the text which we need to decode or encode')
parser.add_argument('--output_file', type=argparse.FileType('wt'),
                    default=sys.stdout,
                    help='The file where we put decoded or encoded text щк count the frequency of letters')
subparsers = parser.add_subparsers()

hack_parser = subparsers.add_parser('hack', help='')
hack_parser.add_argument('key_file', type=argparse.FileType('rt'),
                         help='Character frequency file for hacking Caesar’s cipher')

text_parser = subparsers.add_parser('mode', help='')
text_parser.add_argument('my_mode', choices=['decode', 'encode'], type=str,
                         help='Choose one of the two modes: encode or decode')
text_parser.add_argument('--cipher', type=str, choices=['caesar', 'vigenere'],
                         help='Choose one of the cipher: caesar or vigenere')
text_parser.add_argument('--key', type=str, default='0',
                         help='Write the number if you use Caesar\'s code, or the word otherwise')
