import pandas as pd
from pathlib import Path


base_dir = Path(__file__).resolve().parent
df = pd.read_excel(base_dir / 'FILES/sp_helpingFile.xlsx', sheet_name="Full Name")
names = df['Full Name'].tolist()
print(len(names))
