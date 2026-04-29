import os
import subprocess

data_folder = "/home/jovyan/SHIP_DETECTION_DATA_HORMUZ"
output_folder = "/home/jovyan/output"
gpt_path = "/home/jovyan/snap/bin/gpt"
graph = "Ship_Detection_Graph.xml"

files = [f for f in os.listdir(data_folder) if f.endswith(".zip")]

print("Total Sentinel-1 files found:", len(files))

for file in files:
    
    input_path = os.path.join(data_folder, file)
    output_name = file.replace(".zip", ".dim")
    output_path = os.path.join(output_folder, output_name)

    command = [
        gpt_path,
        graph,
        f"-Pinput={input_path}",
        f"-Poutput={output_path}"
    ]

    print("Processing:", file)
    subprocess.run(command)

print("All processing finished.")
