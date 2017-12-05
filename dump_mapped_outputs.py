#!/bin/env python2.7
import argparse
import json
import sys

def serialize(fn, obj):
    with open(fn, 'w') as ofs:
        ofs.write(json.dumps(obj))
        ofs.write('\n')

def deserialize(fn):
    with open(fn) as ifs:
        return json.loads(ifs.read())

def run(mapped_fn, unmapped_fn, fn_pattern):
    unmapped = deserialize(unmapped_fn)
    mapped = dict()
    for i, fn in enumerate(unmapped):
        key = i
        mapped[i] = fn
    serialize(mapped_fn, mapped)

def parse_args(argv):
    description = """
Write a file which records the unmapped filenames, indexed by their keys (inferred from a pattern).
"""
    parser = argparse.ArgumentParser(
            description=description,
    )
    parser.add_argument(
            '--mapped-fn', required=True,
            help='Output: Serialized map of key to filename, relative to the directory of this file.')
    parser.add_argument(
            '--unmapped-fn', required=True,
            help='Input: List of results of a merge task.')
    parser.add_argument(
            '--fn-pattern', default='foo.txt',
            help='A pattern to match against the unmapped filenames.')
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    run(**vars(args))

if __name__ == "__main__":
    main()
