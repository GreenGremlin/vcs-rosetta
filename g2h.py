#!/usr/bin/env python

import sys
from print_translation import print_usage

if __name__ == "__main__":
    print_usage(from_type = 'git', to_type = 'hg', args = sys.argv[1:])
