import os
import random
import string
import platform
import logging
import getpass


def main(deskpath):
    # i = 0
    # while True:
    for i in range(5):
        filepath = os.path.join(deskpath, f'test{i}.txt')
        with open(filepath, "w") as f:
            f.write(''.join(random.choice(string.ascii_lowercase)
                    for _ in range(10)))
            f.close()
        # i += 1


def check_os():
    os_type = platform.system()
    user = getpass.getuser()
    print(os_type, user)

    if os_type.lower().startswith('darwin') or os_type.lower().startswith('macos'):
        deskpath = f'/Users/{user}/Desktop'

    elif os_type.lower().startswith('win'):
        deskpath = f'C:\\Users\\{user}\\Desktop'

    elif os_type.lower().startswith('linux'):
        deskpath = f'~/Desktop'

    else:
        logging.warning(" This OS is not supported. Shutting down.")
        quit()

    main(deskpath)


if __name__ == '__main__':
    check_os()
