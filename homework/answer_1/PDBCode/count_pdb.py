
from constant import ROOT_PATH
import os, sys
from optparse import OptionParser
import numpy as np


def add_dic(dic, num):
    if num in dic.keys():
        dic[num] += 1
    else:
        dic[num] = 1
    return dic


def read_pdb(pdb_name):
    pdbdir = os.path.join(ROOT_PATH, 'PDBData', pdb_name, 'output_%s'%pdb_name)
    A = {}
    D = {}
    for line in open(pdbdir).readlines():
        if line[0] == 'A':
            splt = line.split()
            A_id, D_id = int(splt[1]), int(splt[6])
            add_dic(A, A_id)
            add_dic(D, D_id)
        else:
            break
    sort_A = sorted(A.items(),key=lambda x:x[0])
    sort_D = sorted(D.items(),key=lambda x:x[0])
    print('A: \n', sort_A,'\nB:\n', sort_D)
    count_pdb_dir = os.path.join(ROOT_PATH, 'PDBData', pdb_name, 'count_%s'%pdb_name)
    if os.path.exists(count_pdb_dir):
        os.remove(count_pdb_dir)
    os.mknod(count_pdb_dir)
    for x in sort_A:
        open(count_pdb_dir, 'a').write('A   %s: %s\n' % (x[0], x[1]))
    open(count_pdb_dir, 'a').write('Total number of A: %s\n'%sum(dict(sort_A).values()))
    open(count_pdb_dir, 'a').write('\n\n')
    for x in sort_D:
        open(count_pdb_dir, 'a').write('D   %s: %s\n'%(x[0], x[1]))
    open(count_pdb_dir, 'a').write('Total number of D: %s\n'%sum(dict(sort_D).values()))
    
    
        


def main(argv = None):
    if argv is None:
        argv = sys.argv[1:]

    parser = OptionParser(usage = """Count.""")

    (options, args) = parser.parse_args(argv)
    if len(args) < 1:
        parser.print_help()
        return 1

    pdb_name = args[0]

    return read_pdb(pdb_name)

if __name__ == "__main__":
    sys.exit(main())
