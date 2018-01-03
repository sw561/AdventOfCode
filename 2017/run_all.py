#!/usr/bin/env python3

import subprocess
import time

for i in range(1, 26):
	start = time.time()
	subprocess.check_call("cd {} && bash run.sh && cd -".format(i), shell=True)
	end = time.time()
	print("Day: {}. Time: {:.1f}".format(i, end-start))
