#!/usr/bin/env python3

import re


def filter_datum(fields, redaction, message, separator):
    """
    filtered datum
    Args:
        fields(dict): fileds to be inputed
        redaction(str): the hashing character
        message(str): the logged texts
        separator(str): separates filed name and value
    Return:
        returns string
    """
    pattern = f"({'|'.join(fields)})=([^ {separator}]*)"
    return re.sub(pattern, lambda m: f"{m.group(1)}={redaction}", message)  # noqa
