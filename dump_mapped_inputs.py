#!/bin/env python2.7
import argparse
import json
import sys

def serialize(fn, obj):
    with open(fn, 'w') as ofs:
        ofs.write(json.dumps(obj))
        ofs.write('\n')

def run(mapped_fn, input_fn):
    fn_pattern = 'mapped_input_{}.txt'
    with open(input_fn, 'r') as infile:
        mapped = dict()
        for n, line in enumerate(infile.readlines()):
            fn = fn_pattern.format(n)
            with open(fn, 'w') as outfile:
                outfile.write(line)
            mapped[n] = fn
    serialize(mapped_fn, mapped)

def parse_args(argv):
    description = """
Dump "chunks" and write a file which records the new filenames, indexed by their original line-numbers.
"""
    parser = argparse.ArgumentParser(
            description=description,
    )
    parser.add_argument(
            '--mapped-fn', required=True,
            help='Output: Serialized map of key to filename, relative to the directory of this file.')
    parser.add_argument(
            '--input-fn', required=True,
            help='Input: File of numbers, one per line.')
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    run(**vars(args))

if __name__ == "__main__":
    main()
