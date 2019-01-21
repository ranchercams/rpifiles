#!/usr/bin/env python

import os, sys
import os.path
from os import mkdir
import custnumber

cust_num = custnumber.custnum

custfolder = os.path.join(cust_num)

os.makedirs(custfolder)