from Selfcheck import check as sc
import json, sys
config = json.load(open('./config.json', 'r', encoding='utf-8'))
data = sc.selfcheck(*list(config["auth"].values()))
print(data)
sys.exit(0)