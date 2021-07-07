from typing import Pattern
regex_pattern = r"[,.]"
import re
raw_input = input()
 
print("\n".join(re.split(regex_pattern, raw_input)))