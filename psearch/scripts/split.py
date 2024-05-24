the correct split.y
#==============================================================================

import sys
import argparse
import pandas as pd

def main(in_fname, out_act_fname, out_inact_fname):
    """
    Split a dataset into active and inactive sets by status column.
    :param in_fname: input .smi file
    :param out_act_fname: path where an active set will be saved
    :param out_inact_fname: path where an inactive set will be saved
    :return: None
    """
    try:
        # Attempt to read the file with utf-8 encoding
        df = pd.read_csv(in_fname, sep='\t', header=None, encoding='utf-8')
    except UnicodeDecodeError:
        # If utf-8 fails, fallback to ISO-8859-1 encoding
        df = pd.read_csv(in_fname, sep='\t', header=None, encoding='ISO-8859-1')

    df_act = df[df[2] == 'active']
    df_act.to_csv(out_act_fname, sep='\t', index=None, header=None)
    df_inact = df[df[2] == 'inactive']
    df_inact.to_csv(out_inact_fname, sep='\t', index=None, header=None)

    sys.stderr.write('actives: %i, inactives: %i.\n' % (df_act.shape[0], df_inact.shape[0]))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Select active and inactive compounds'
                                                 'based on given values (act_threshold and inact_threshold)')
    parser.add_argument('-i', '--in', metavar='input.smi', required=True,
                        help='Input SMILES file name. It should contain three columns separated by whitespaces: '
                             'SMILES, name, activity. No header.')
    parser.add_argument('-oa', '--out_act', metavar='active.smi', required=True,
                        help='Output SMILES file name for active compounds.')
    parser.add_argument('-oi', '--out_inact', metavar='inactive.smi', required=True,
                        help='Output SMILES file name for inactive compounds.')

    args = vars(parser.parse_args())
    for o, v in args.items():
        if o == "in": in_fname = v
        if o == "out_act": out_act_fname = v
        if o == "out_inact": out_inact_fname = v

    main(in_fname=in_fname,
         out_act_fname=out_act_fname,
         out_inact_fname=out_inact_fname)
