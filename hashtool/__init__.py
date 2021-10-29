import os
import hashlib
import argparse


available_methods = ['md5', 'sha1', 'sha224', 'sha256',
                     'sha384', 'sha3_224', 'sha3_256',
                     'sha3_384', 'sha3_512', 'sha512']


def show_message(message):
    print(message)
    raise SystemExit


def get_hash_value(byte_message, hash_method):
    hashobj = getattr(hashlib, hash_method)()
    hashobj.update(byte_message)
    return hashobj.hexdigest()


def main():

    available_methods_format = ', '.join(available_methods)
    parser = argparse.ArgumentParser(
        description='hash file or text with different method')
    parser.add_argument('file', help='target file')
    parser.add_argument('-t', '--text', action='store_true',
                        help='hash a text instead a file')
    parser.add_argument('method',
                        help=f'the following methods are availalbe: {available_methods_format}')

    args = parser.parse_args()

    path = args.file
    if args.method not in available_methods:
        show_message(f'错误：不支持这种哈希方式：{args.method}')
    if args.text:
        data = path.encode()
    else:
        if not os.path.exists(path):
            show_message(f'错误:目标文件不存在:{path}')
        with open(path, 'rb')as fl:
            data = fl.read()
    print(get_hash_value(data, args.method))
