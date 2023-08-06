# Parse and update BOTW saves in Python

This is a simple library for parsing and updating BOTW save files in Python. *I
did not write more than a couple lines of this code*. It is taken almost wholly
from Mr. Cheeze's `save.py` script located on his
[BOTW tools repo](https://github.com/MrCheeze/botw-tools/blob/master/save.py),
to be simply converted into a library (with permission).

Simple usage examples:

```python
import uking_saves

save_file = uking_saves.parse_file("blah/game_data.sav") // Parse the save
save_file["MainField_WeaponDrop_1609063018"] = True // Set a flag value
uking_saves.update_file("blah/game_data.sav", save_file) // Save updated data
```
