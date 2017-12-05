#!/bin/env python2.7
import argparse
import json
import os
import sys

def deserialize(fn):
    with open(fn) as ifs:
        return json.loads(ifs.read())

def assert_exists(fn):
    if not os.path.isfile(fn):
        raise Exception('Does not exist: {!r}'.format(fn))

def mkdir(dirname):
    if not os.path.isdir(dirname):
        # Possible race-condition, so dirs must be created serially.
        os.makedirs(dirname)

def symlink(name, target):
    msg = '{} -> {}'.format(name, target)
    assert not os.path.lexists(name), msg
    #print msg
    os.symlink(target, name)

def run(mapped_fn, fn_pattern):
    """
    Symlink targets will be relative to cwd.
    For pattern, the word '{key}' will be substituted everywhere, e.g.
        fn_pattern == 'top/{key}/input_{key}.txt'
    """
    mapped = deserialize(mapped_fn)
    mapdir = os.path.normpath(os.path.dirname(os.path.normpath(mapped_fn)))
    for key, val in mapped.iteritems():
        assert_exists(val)
        symlink_name = fn_pattern.format(key=key)
        outdir = os.path.normpath(os.path.dirname(symlink_name))
        mkdir(outdir)
        relmapdir = os.path.relpath(mapdir, outdir)
        target_name = os.path.relpath(os.path.join(relmapdir, val))
        symlink(symlink_name, target_name)

def parse_args(argv):
    description = 'Create symlinks named after "fn_pattern", targeting values in "mapped_fn".'
    parser = argparse.ArgumentParser(
            description=description,
    )
    parser.add_argument(
            '--mapped-fn', required=True,
            help='Serialized map of key to filename, relative to the directory of this file.')
    parser.add_argument(
            '--fn-pattern', required=True,
            help='Pattern for symlinks, to be substituted with keys in mapped_fn.')
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    run(**vars(args))

if __name__ == "__main__":
    main()
