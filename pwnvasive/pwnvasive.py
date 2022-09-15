#! /usr/bin/env python

import sys
import asyncio
import argparse
import logging
import pdb

from .store import Store

logging.basicConfig()
logging.getLogger("asyncio").setLevel(logging.WARNING)




async def main(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("database")

    options = parser.parse_args(args)

    try:
        with Store(options.database) as options.store:
            options.operations = Operations(options.store)
            await PwnCLI(options).run(history=options.store.history)
    except Exception as e:
        print(f"ERROR: {e}")
        print("You can still recover data from options.store.nodes, etc.")
        sys.last_traceback = e.__traceback__
        pdb.pm()


if __name__ == "__main__":
    asyncio.run(main())
