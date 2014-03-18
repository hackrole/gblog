#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/env python
# encoding: utf-8

"""
tools to run the test for unit/view/modes/fts, and so on.
"""

import sys

import unittest


def main(sdk_path, test_path):
    """
    run unit tests for App Engine apps.
    """
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    suite = unittest.loader.TestLoader().discover(test_path)
    print test_path
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    #usage = "%prog SDK_PATH TEST_PATH"
    #parser = optparse.OptionParser(usage)
    #options, args = parser.parse_args()
    #if len(args) != 2:
        #parser.print_help()
        #sys.exit(1)

    #SDK_PATH = args[0]
    #TEST_PATH = args[1]

    SDK_PATH = "/home/hackrole/Desktop/program/google_appengine"
    TEST_PATH = "/home/hackrole/Desktop/program/google_appengine/gblog/tests"
    main(SDK_PATH, TEST_PATH)
