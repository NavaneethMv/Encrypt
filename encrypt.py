import argparse
import pyAesCrypt
from os import stat, remove
import sys
import pyfiglet


class Main:
    buffersize = 64 * 1024
    parser = argparse.ArgumentParser(description = '''Encrypt files using python''')
    parser.add_argument("-ef", "--input_normal", help = "file path to encrypt")
    parser.add_argument("-df", "--input_decrypt", help = "file path to decrypt")
    parser.add_argument("-of","--output", help = "output file name")
    args = parser.parse_args()


if Main.args.input_normal:
    class Encrypt(Main):
        password = input('Enter the password : ')
        confirm_password = input('Confirm passsword : ')
        if password == confirm_password:
            with open(Main.args.input_normal, 'rb') as f:
                with open(Main.args.output, 'wb') as g:
                    pyAesCrypt.encryptStream(f, g, password, Main.buffersize)
            remove(Main.args.input_normal)


elif Main.args.input_decrypt:
    class Encrypt(Main):
        password = input('Enter the password : ')
        # get encrypted file size
        encFileSize = stat(Main.args.input_decrypt).st_size
        try:
            with open(Main.args.input_decrypt, 'rb') as f:
                with open(Main.args.output, 'wb') as g:
                    pyAesCrypt.decryptStream(f, g, password, Main.buffersize, encFileSize)
        except ValueError:
            print("Incorrect password ")
            remove(Main.args.output)


else:
    print(pyfiglet.figlet_format("Encrypt", font = 'small'))
    Main.parser.print_help()
