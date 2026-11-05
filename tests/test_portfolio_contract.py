"""Deterministic smoke/contract checks using the actual notebook's constructor code.

Run `python -m unittest discover -s tests -v`. No real market data needed.
"""
import ast
import json
import unittest
from pathlib import Path

import numpy as np
import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
NB = json.loads((ROOT / 'notebooks' / '01_macroanchor_g10_10y_rv_v2_3_frozen.ipynb').read_text())
constructor_cell = ''.join(NB['cells'][5]['source'])
module = ast.parse(constructor_cell)
env = dict(np=np,pd=pd,MIN_COUNTRIES=6,HEADLINE_K=3,NW_LAG=12)
exec(compile(module, '<notebook constructor cell>', 'exec'),env)

class PortfolioContract(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        names=list('ABCDEFGHI')
        dates=pd.date_range('2020-01-31',periods=15,freq='ME')
        rows=[]
        for date in dates:
            for i,c in enumerate(names):
                rows.append(dict(date=date,country=c,y10=0.01+0.002*i,r3m=.01,slope=0.002*i,
                                 duration10=6.1+0.25*i,tp_z_past=float(i-4),
                                 y10_z_past=float(4-i),slope_z_past=float(4-i),
                                 rx=float(i-4)/1000))
        cls.panel=pd.DataFrame(rows)
    def test_headline_net_dv01_and_six_legs(self):
        p,w=env['form_portfolio_panel'](self.panel)
        self.assertEqual(len(p),15)
        for date,g in w.groupby('date'):
            self.assertEqual((g.weight.abs()>0).sum(),6)
            self.assertAlmostEqual(g.dv01_weight.sum(),0,places=12)
            self.assertAlmostEqual(g.weight.abs().sum(),1,places=12)
    def test_benchmark_remaps_score_without_duplicate_labels(self):
        p,w=env['form_portfolio_panel'](self.panel,mode='rank',signal='y10_z_past')
        self.assertEqual(len(p),15)
        self.assertLess(p['ret12'].mean(),0)  # selected yield-score longs have lower synthetic returns
        self.assertAlmostEqual(w.groupby('date').dv01_weight.sum().abs().max(),0,places=12)
    def test_continuous_neutrality(self):
        p,w=env['form_portfolio_panel'](self.panel,mode='continuous')
        self.assertEqual(len(p),15)
        self.assertAlmostEqual(p['net_dv01'].abs().max(),0,places=12)
        self.assertAlmostEqual(p['gross_notional'].mean(),1,places=12)
    def test_frozen_source_specs(self):
        config=''.join(NB['cells'][2]['source'])
        self.assertIn('HEADLINE_K = 3',config)
        self.assertIn('SENSITIVITY_K = 2',config)
        self.assertIn('H = 12',config)
        self.assertIn('NW_LAG = 12',config)
        self.assertNotIn("rename(columns={signal:'tp_z_past'})",constructor_cell)

if __name__=='__main__': unittest.main()
