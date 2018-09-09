#!/usr/bin/env python3

# Copyright (c) Facebook, Inc. and its affiliates.
# All rights reserved.
#
# This source code is licensed under the BSD-style license found in the
# LICENSE file in the root directory of this source tree.
#

import sys
from nubia import Nubia
from nubia_plugin import lldbPlugin

if __name__ == "__main__":
    plugin = lldbPlugin()
    shell = Nubia(name="lldb", plugin=plugin)
    sys.exit(shell.run())
