#!/usr/bin/env python3
# Copyright 2018 miruka
# This file is part of whratio, licensed under LGPLv3.

"""Usage: whratio [options] WIDTH HEIGHT

Print aspect ratio for the given numbers, integer and decimal by default.

Arguments:
  WIDTH   Width to calculate ratio for.
  HEIGHT  Height to calculate ratio for.

Options:
  -W, --int-width        Print the integer ratio width.
  -H, --int-height       Print the integer ratio height.
  -d, --decimal          Print the decimal ratio.
  -n NUM, --ndigits NUM  Digits for rounded decimal ratio, default is 2.

  -h, --help     Show this help.
  -V, --version  Show the program version."""

import sys

import blessings
import docopt

from . import __about__, ratio


def main():
    """Process CLI arguments and call appropriate functions."""
    term = blessings.Terminal()

    try:
        args = docopt.docopt(__doc__, version=__about__.__version__)
    except docopt.DocoptExit:
        if len(sys.argv) > 1:
            print(term.red("Invalid command syntax, check help:\n"))
        print(__doc__)
        sys.exit(1)

    print_all = False
    if not (args["--int-width"] or args["--int-height"] or args["--decimal"]):
        print_all = True

    width    = float(args["WIDTH"])
    height   = float(args["HEIGHT"])

    as_int   = ratio.as_int(width, height)
    ndigits  = int(args.get("--ndigits", 2))
    as_float = ratio.as_float(width, height, ndigits=ndigits)

    to_print = []

    if args["--int-width"] or print_all:
        to_print.append(term.blue(str(as_int[0])))

    if args["--int-height"] or print_all:
        to_print.append(term.blue(str(as_int[1])))

    if args["--decimal"] or print_all:
        to_print.append(term.magenta(f"%0.{ndigits}f" % as_float))

    print(" ".join(to_print))


if __name__ == "__main__":
    main()
