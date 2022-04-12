# importing Modules for other files

import converters
print(converters.kg_to_lbs(70))

# 2nd way to import is to use the 'from/import' method.

from converters import kg_to_lbs

print(kg_to_lbs(100))
