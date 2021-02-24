#!/usr/bin/env python
import re
try:
	import configparser as ConfigParser
except ImportError:
	import ConfigParser
patterns = {}

path = "./Data/patterns.ini"


def load_patterns(path):
    config = ConfigParser.ConfigParser()
    with open(path) as f:
        config.readfp(f)
    for ind_type in config.sections():
        try:
            ind_pattern = config.get(ind_type, 'pattern')
        except:
            continue
        if ind_pattern:
            ind_regex = re.compile(ind_pattern, re.IGNORECASE | re.M)
            patterns[ind_type] = ind_regex
    return patterns
