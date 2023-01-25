# Python program
import pandas as pd
import yaml

# read config file
config_path = "/Users/antony.vargasulead.ac.cr/BigData/Clase1/config/config.yml"
config = yaml.safe_load(open(config_path))
df = pd.read_csv( config["file_path"])


# print all players
print(df)
