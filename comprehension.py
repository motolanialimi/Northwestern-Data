# -*- coding: UTF-8 -*-
"""Comprehensions

This module collects the names of five people the user knows, and then
injects them into an invitation to a wedding.

Example:

  $ python comprehensions.py

"""

names = []
for _ in range(5):
    name = input("Please enter the name of someone you know. ")
    names.append(name)
name

import pdb; pdb.set_trace()
lowercased = [name.lower() for name in names]
titlecased = [name.title() for name in lowercased]
invitations = [
    f"Dear {name}, please come to the wedding this Saturday!" for name in titlecased]

for invitation in invitations:
    print(invitation)