"""Audit the exact frozen code and reported analysis sample using stored evidence."""
from pathlib import Path
import json, hashlib
import pandas as pd
root=Path(__file__).resolve().parents[1]
nb=json.loads((root/'notebooks'/'01_macroanchor_g10_10y_rv_v2_3_frozen.ipynb').read_text())
sha=hashlib.sha256(''.join(''.join(c.get('source',[])) for c in nb['cells'] if c['cell_type']=='code').encode()).hexdigest()
m=json.loads((root/'results'/'manifest.json').read_text())
assert sha==m['source_code_sha256'], 'Frozen source code was modified'
p=pd.read_csv(root/'results'/'performance.csv')
s=pd.read_csv(root/'results'/'spanning.csv')
assert int(p.loc[p.strategy=='rank_top3_bottom3_DV01','months'].iloc[0])==363
assert int(s.loc[s.model.str.startswith('rank_top3') & s.model.str.contains('yield/slope'), 'n'].iloc[0])==243
print('PASS: frozen code SHA, headline formation count, and full spanning sample')
