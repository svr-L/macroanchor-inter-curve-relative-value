"""Generate publication-friendly, *descriptive* V2.3 figures from verified aggregate CSV tables.

All data come from results/ CSVs taken from the original executed frozen notebook.
This intentionally does NOT make a cumulative wealth curve from overlapping returns.
"""
from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / 'results'
FIG = ROOT / 'figures'
FIG.mkdir(parents=True,exist_ok=True)
NAVY = '#18324D'
TEAL = '#127D83'
CYAN = '#5DAAB0'
GREY = '#74849A'
GRID = '#D9E1E6'
RED = '#9D4B53'

plt.rcParams.update({
    'figure.facecolor': 'white', 'axes.facecolor': 'white',
    'font.family': 'DejaVu Sans', 'font.size': 10.2,
    'axes.titlesize': 16, 'axes.titleweight': 'bold',
    'axes.labelsize': 10, 'axes.edgecolor': GRID,
    'axes.spines.top': False, 'axes.spines.right': False,
    'axes.grid': False,
    'savefig.facecolor': 'white', 'savefig.dpi': 170,
})

def finish(fig,name,source,subnote=None):
    caption='Source: V2.3 executed snapshot; '+source
    if subnote: caption+='\n'+subnote
    fig.text(.055,.045,caption,ha='left',va='bottom',color=GREY,fontsize=8.1)
    fig.savefig(FIG/name,dpi=170,bbox_inches='tight',pad_inches=.22)
    plt.close(fig)

# Portfolio summary: the bar height is the 12m-forward proxy mean, not annualized live P&L.
df=pd.read_csv(RESULTS/'performance.csv')
name={'rank_top3_bottom3_DV01':'Top 3 / Bottom 3\nFrozen headline',
      'rank_top2_bottom2_DV01_sensitivity':'Top 2 / Bottom 2\nSensitivity',
      'continuous_score_DV01':'Continuous score\nSecondary'}
df=df.loc[df.strategy.isin(name),:].copy()
df['label']=df.strategy.map(name)
fig,ax=plt.subplots(figsize=(9.1,4.7))
fig.subplots_adjust(left=.10,right=.98,top=.79,bottom=.30)
xs=np.arange(len(df))
bars=ax.bar(xs,df.gross_ann_mean*100,width=.53,color=[TEAL,NAVY,CYAN],zorder=3)
ax.set_xticks(xs,df['label'],fontsize=10.2)
ax.set_ylim(0,.85)
ax.set_ylabel('Mean forward 12-month gross return (%)')
ax.grid(axis='y',color=GRID,alpha=.75,zorder=0)
ax.set_title('MacroAnchor inter-curve RV | Frozen V2.3',loc='left',pad=18,color=NAVY)
fig.text(.10,.82,'DV01-neutral, 10Y sovereigns · 363 monthly formations per specification',color=GREY,fontsize=10)
for b,(_,r) in zip(bars,df.iterrows()):
    ax.text(b.get_x()+b.get_width()/2,b.get_height()+.024,f"{r.gross_ann_mean*100:.3f}%",ha='center',va='bottom',fontweight='bold',fontsize=12,color=NAVY)
    ax.text(b.get_x()+b.get_width()/2,.05,f"NW(12) t = {r.NW_t:.2f}",ha='center',va='bottom',fontsize=9,color='white',fontweight='bold')
finish(fig,'performance.png','results/performance.csv', 'Overlapping forward 12-month proxies; not cumulative/realized annual portfolio performance.')

# Subperiods: emphasize sample size and NW t drop; no annualization assumptions.
s=pd.read_csv(RESULTS/'subperiods.csv')
sub_order=['pre_2008','2008_2015','2016_plus']
s=s[s.strategy.isin(['rank_top3_bottom3_DV01','continuous_score_DV01'])].copy()
fig,ax=plt.subplots(figsize=(9.2,4.8))
fig.subplots_adjust(left=.105,right=.97,top=.81,bottom=.27)
x=np.arange(3)
width=.33
for j,(strategy,color,label) in enumerate([
 ('rank_top3_bottom3_DV01',TEAL,'Top 3 / Bottom 3 (headline)'),
 ('continuous_score_DV01',NAVY,'Continuous score')]):
    part=s[s.strategy==strategy].set_index('regime').loc[sub_order]
    xx=x+(j-.5)*width
    bars=ax.bar(xx,part.gross_ann_mean.to_numpy()*100,width=.29,color=color,label=label,zorder=3)
    for b,(_,r) in zip(bars,part.iterrows()):
        ax.text(b.get_x()+b.get_width()/2,b.get_height()+.021,f"{r.gross_ann_mean*100:.2f}%",ha='center',fontsize=9.2,color=NAVY,fontweight='bold')
        ax.text(b.get_x()+b.get_width()/2,.04,f"t={r.NW_t:.2f}",ha='center',fontsize=8.1,color='white',fontweight='bold')
ax.set_xticks(x,['Before 2008\nn = 168','2008–2015\nn = 96','2016 onward\nn = 99'])
ax.set_ylabel('Mean forward 12-month gross return (%)')
ax.set_ylim(0,.82)
ax.grid(axis='y',color=GRID,alpha=.75,zorder=0)
ax.set_title('Subperiod stability | weaker recent inference',loc='left',pad=12,color=NAVY)
ax.legend(loc='upper right',frameon=False,ncol=2,fontsize=8.8)
finish(fig,'subperiods.png','results/subperiods.csv','Subperiod NW t-statistics annotated inside bars; each mean uses overlapping forward returns.')

# Cost proxy grid.
c=pd.read_csv(RESULTS/'cost_fx_stress_zero_drag.csv')
fig,ax=plt.subplots(figsize=(9.15,4.6))
fig.subplots_adjust(left=.105,right=.98,top=.81,bottom=.25)
for strategy,label,color in [
 ('rank_top3_bottom3_DV01','Top 3 / Bottom 3 (headline)',TEAL),
 ('continuous_score_DV01','Continuous score',NAVY)]:
    a=c[c.strategy==strategy].sort_values('oneway_cost_bp')
    ax.plot(a.oneway_cost_bp,a.net_ann_mean*100,marker='o',ms=5,lw=2.5,color=color,label=label)
ax.axhline(0,lw=1,color=RED,ls='--',alpha=.7)
ax.set_xticks([0,1,2,5,10,25])
ax.set_xlim(-.8,25.8)
ax.set_ylim(0,.72)
ax.set_ylabel('Estimated net mean forward 12m return (%)')
ax.set_xlabel('Assumed one-way cost (bp per unit traded)')
ax.grid(axis='y',color=GRID,alpha=.75)
ax.legend(frameon=False,loc='upper right',fontsize=9)
ax.set_title('Cost sensitivity | simplified target-turnover model',loc='left',pad=12,color=NAVY)
finish(fig,'cost_sensitivity.png','results/cost_fx_stress_zero_drag.csv','Zero additional FX drag; costs are assumptions, not executable bond/hedge spreads.')

# Country concentration.
e=pd.read_csv(RESULTS/'country_exposure.csv').sort_values('avg_abs_notional_weight')
fig,ax=plt.subplots(figsize=(9,5.3))
fig.subplots_adjust(left=.16,right=.96,top=.85,bottom=.21)
bars=ax.barh(e.country,e.avg_abs_notional_weight*100,color=[GREY]*len(e),height=.7)
for b,v in zip(bars,e.avg_abs_notional_weight*100):
    ax.text(v+.35,b.get_y()+b.get_height()/2,f'{v:.1f}%',va='center',color=NAVY,fontsize=9.5)
ax.set_xlim(0,20)
ax.set_xlabel('Average absolute portfolio notional (%)')
ax.grid(axis='x',color=GRID,alpha=.8,zorder=0)
ax.set_axisbelow(True)
ax.set_title('Geographic allocation | gross exposure, not P&L',loc='left',pad=10,color=NAVY)
finish(fig,'country_exposure.png','results/country_exposure.csv','Ex ante/average absolute notional weights, summed over the frozen V2.3 universe.')

# Spanning with approximate HAC intervals, explicitly separate sample sizes.
f=pd.read_csv(RESULTS/'spanning.csv')
f=f[f.model.str.startswith('rank_top3_bottom3')].copy().sort_values('n',ascending=False)
labels=['Global 10Y only\nn = 363','Global + yield RV + slope/carry RV\nn = 243']
fig,ax=plt.subplots(figsize=(9.2,4.7))
fig.subplots_adjust(left=.11,right=.95,top=.81,bottom=.25)
y=np.array([1,0])
a=f.alpha_ann.to_numpy()*100
se=np.abs(a/f.alpha_t_NW.to_numpy())
ax.errorbar(a,y,xerr=1.96*se,fmt='o',markersize=10,color=TEAL,capsize=5,lw=2.3)
ax.set_yticks(y,labels)
ax.set_xlim(-.3,1.07)
ax.set_ylim(-.48,1.55)
ax.axvline(0,ls='--',color=GREY,lw=1)
ax.set_xlabel('Intercept on 12m forward proxy return (%)')
ax.grid(axis='x',color=GRID,alpha=.7)
ax.set_axisbelow(True)
for yy,(_,r) in zip(y,f.iterrows()):
    ax.text(.87,yy,f"NW t={r.alpha_t_NW:.2f}",color=NAVY,ha='right',va='center',fontsize=9.5)
ax.set_title('Factor spanning | differing sample sizes',loc='left',pad=10,color=NAVY)
finish(fig,'factor_spanning.png','results/spanning.csv', 'Approx. 95% NW normal CIs from alpha/t; different n = NOT a common-sample nested test.')

print('Generated:', ', '.join(p.name for p in sorted(FIG.glob('*.png'))))
