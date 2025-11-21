import pandas as pd
from pathlib import Path

def run_flow(config):
    input_path = Path(config['input_folder'])
    output_path = Path(config['output_folder'])
    output_path.mkdir(exist_ok=True)
    df_list = [pd.read_csv(f) for f in input_path.glob('*.csv')]
    if not df_list:
        print('No CSV files found.'); return
    merged = pd.concat(df_list, ignore_index=True)
    drop_cols = config.get('drop_columns',[])
    merged = merged.drop(columns=[c for c in drop_cols if c in merged], errors='ignore')
    sort_by = config.get('sort_by',[])
    if sort_by:
        merged = merged.sort_values(sort_by)
    if 'summary' in config:
        grp = config['summary']['group_by']
        sum_cols = config['summary']['sum_columns']
        summary = merged.groupby(grp)[sum_cols].sum().reset_index()
        summary.to_csv(output_path/'summary.csv',index=False)
    merged.to_csv(output_path/'merged.csv',index=False)
    print('Processing completed.')
