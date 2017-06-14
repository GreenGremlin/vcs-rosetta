#!/usr/bin/env python

import os
import sys
import yaml

from usage_translator import UsageTranslator


def __load_translations__(file_location):
    with open(file_location, 'r') as stream:
        return yaml.load(stream)


def __not_found_message__(args, from_type, translations_file):
    return 'No translation found for `{from_type} {args}` in "{file}"'.format(
        from_type=from_type,
        args=args,
        file=translations_file,
    )


def main(from_type, to_type, args):
    if len(args) == 0:
        print('Please provide at least one argument to translate!')
        return
    script_dir = os.path.dirname(os.path.realpath(__file__))
    translations_file = os.path.join(os.getcwd(), script_dir, 'data/git_hg.yaml')
    translations = __load_translations__(translations_file)
    translator = UsageTranslator(from_type=from_type,
                                 to_type=to_type,
                                 translations=translations)

    usage = translator.lookup_usage(args)
    if usage is not None:
        print(usage)
    else:
        print(__not_found_message__(args, from_type, translations_file))


if __name__ == "__main__":
    args = sys.argv[1:]
    main(from_type=args[0], to_type=args[2], args=args[3])
