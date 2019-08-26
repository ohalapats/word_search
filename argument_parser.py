import argparse


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--gridsize', '-gs', help='Input grid size',
                        type=int, default=15)
    args = parser.parse_args()
    return args
