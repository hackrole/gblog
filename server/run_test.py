#!/usr/bin/env python
# encoding: utf-8

#!/usr/bin/env python
# encoding: utf-8

"""
tools to run the test for unit/view/modes/fts, and so on.
"""

import sys
import optparse
import unittest


def main(sdk_path, test_path, name=None):
    """
    run unit tests for App Engine apps.
    """
    sys.path.insert(0, sdk_path)
    import dev_appserver
    dev_appserver.fix_sys_path()
    loader = unittest.loader.TestLoader()
    if name is None:
        suite = loader.discover(test_path)
    else:
        suite = loader.loadTestsFromName(name)
    unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    usage = "%prog SDK_PATH TEST_PATH"
    parser = optparse.OptionParser(usage)
    options, args = parser.parse_args()
    name = None
    if len(args) == 1:
        name = args[0]

    SDK_PATH = "/home/hackrole/Desktop/program/google_appengine"
    TEST_PATH = "/home/hackrole/Desktop/program/google_appengine/gblog/tests"
    main(SDK_PATH, TEST_PATH, name)
