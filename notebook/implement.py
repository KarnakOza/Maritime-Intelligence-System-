!ls /home/jovyan/output | grep ".dim" | wc -l

!grep -i "target" -r /home/jovyan/output

######################################################################

import rasterio
import os

data_folder = "/home/jovyan/output"

for folder in os.listdir(data_folder):
    if folder.endswith(".data"):
        print(folder)
        print(os.listdir(os.path.join(data_folder, folder)))
        break

