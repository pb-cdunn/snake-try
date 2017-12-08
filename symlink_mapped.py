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

def run(special_split_fn, fn_pattern):
    """
    Symlink targets will be relative to cwd.
    For pattern, the word '{key}' will be substituted everywhere, e.g.
        fn_pattern == 'top/{key}/input_{key}.txt'
    """
    jobs = deserialize(special_split_fn)
    mapdir = os.path.normpath(os.path.dirname(os.path.normpath(special_split_fn)))
    for key, job in jobs.iteritems():
        assert 1 == len(job['input'])
        val = job['input'][0]
        # val should be relative to the location of the special_split_fn.
        assert not os.path.isabs(val), 'mapped input filename {!r} must be relative (to serialzed file location {!r}'.format(
                val, special_split_fn)
        mapped_input_fn = os.path.join(mapdir, val)
        assert_exists(mapped_input_fn)
        symlink_name = fn_pattern.format(key=key)
        outdir = os.path.normpath(os.path.dirname(symlink_name))
        mkdir(outdir)
        target_name = os.path.relpath(mapped_input_fn, outdir)
        symlink(symlink_name, target_name)

def parse_args(argv):
    description = 'Create symlinks named after "fn_pattern", targeting values in "mapped_fn".'
    parser = argparse.ArgumentParser(
            description=description,
    )
    parser.add_argument(
            '--special-split-fn', required=True,
            help='Serialized split-file (in our special format), where "mapped_inputs" has a map with key to filename, relative to the directory of this file.')
    parser.add_argument(
            '--fn-pattern', required=True,
            help='Pattern for symlinks, to be substituted with keys in special_split_fn.')
    return parser.parse_args(argv[1:])

def main(argv=sys.argv):
    args = parse_args(argv)
    run(**vars(args))

if __name__ == "__main__":
    main()
