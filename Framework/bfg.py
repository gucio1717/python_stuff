import argparse
import mfw
from mfw.controller import dtgenerator


ROOT_DIR = '/home/eszcmic/mydt'


def get_input_parameters():
    parser = argparse.ArgumentParser("Generates loadable DT from templates")

    parser.add_argument('-hw-file',
                        required=True,
                        help="Path to the xml file that contains HW descrip..")
    parser.add_argument('-bsc-config',
                        required=True,
                        help="Bsc configuration name e.g bsc011_default")
    parser.add_argument('-laeip-file',
                        required=True,
                        help="Printout from LAEIP cmd")
    parser.add_argument('-features',
                        nargs='+',
                        help="List of features")
    parser.add_argument('-log-lvl',
                        help="Specify logging level",
                        default='INFO')

    return parser.parse_args()

if __name__ == '__main__':
    args = get_input_parameters()
    mfw.configure(ROOT_DIR, args.log_lvl)

    dt_generator = dtgenerator.DtGenerator(args.hw_file,
                                           args.bsc_config,
                                           args.laeip_file,
                                           args.features)
    result = dt_generator.generate()
    print(result)
