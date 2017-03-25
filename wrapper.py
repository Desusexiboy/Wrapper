'''
PyAuthomation training task: Rsync wrapper.Stage 1: Argparse.
Takes known parameters from CLI input. Returns output_dict.
All keys stored in output_dict['keys'].
All recognised files,dirrectories to copy and remote dirrectory is
stored in output_dict['host_files']
Password to remote host located in output_dict['password']
'''

import argparse


def inputparse():
    output_dict = {}
    single_param = tuple('PavSzqi')
    parser = argparse.ArgumentParser()
    filesgarbage = []
    unknownkeys = []
    keys = []
    parser.add_argument('-process', action="store_true", default=False)
    parser.add_argument('-pass', action="store", dest="userpass", type=str)
    parser.add_argument('-e', action="store", dest='connection', type=str)
    parser.add_argument('files', type=str, help='list of files and dirrs to copy', nargs='*')
    known, unknown = parser.parse_known_args()
    # Fill arguments in group
    for i in unknown:
        if i[1:] in single_param:
                keys.append(i)
        else:
            unknownkeys.append(i)
    for i in known.files:
        filesgarbage.append(i)
    if known.connection == 'ssh':
        keys.append('-e ssh')
    elif known.connection == 'rsh':
        keys.append('-e rsh')
    if known.process:
        keys.append('-process')
    output_dict.update({'host_files': filesgarbage, 'keys': keys, 'password': known.userpass})
    unknownkeys = set(unknownkeys)
    return output_dict, list(unknownkeys)

print inputparse()