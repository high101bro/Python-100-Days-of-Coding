#! /usr/bin/env python3

import module_helper

print(f"The default first name from the module is: {module_helper.first}")
print(f"The default last name from the module is: {module_helper.last}")

print(f"The default fullname from the module is: {module_helper.fullname(module_helper.first,module_helper.last)}")

your_first = input(f"Input your first name: ")
your_last = input(f"Input your last name: ")
print(f"Your fullname created using the module: {module_helper.fullname(your_first,your_last)}")
