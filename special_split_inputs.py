#!/bin/env python2.7
import argparse
import json
import sys

def serialize(fn, obj):
    with open(fn, 'w') as ofs:
        ofs.write(json.dumps(obj, indent=2, separators=(',', ': ')))
        ofs.write('\n')

def run(special_split_fn, input_fn):
    fn_pattern = 'mapped_input_{}.txt'
    with open(input_fn, 'r') as infile:
        jobs = dict()
        for n, line in enumerate(infile.readlines()):
            fn = fn_pattern.format(n)
            with open(fn, 'w') as outfile:
                outfile.write(line)
            job = dict(
                input=[fn],
                # skip output and params for now
            )
            jobs[n] = job
    serialize(special_split_fn, jobs)

def parse_args(argv):
    description = """
Split input into multiple inputs, and write a file which records the new filenames, indexed by their original line-numbers.
"""
    parser = argparse.ArgumentParser(
            description=description,
    )
    parser.add_argument(
            '--special-split-fn', required=True,
            help='Output: Serialized split-file (in our special format), where "mapped_inputs" is a map of key to filename, relative to the directory of this file.')
    parser.add_argument(
            '--input-fn', required=True,
            help='Input: File of numbers, one per line.')
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    run(**vars(args))

if __name__ == "__main__":
    main()
