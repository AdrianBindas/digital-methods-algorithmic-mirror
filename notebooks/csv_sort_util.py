import csv
import pandas as pd
import json

ndjson_fp = 'data/csv/emma_scroll_time2.ndjson'
csv_fp = 'data/csv/emma 2nd scroll.csv'
output_fp = 'data/csv/emma 2nd scroll - processed.csv'
dfs = []

with open(ndjson_fp, encoding='utf8') as f:
    for line in f.readlines():
        json_data = pd.json_normalize(json.loads(line))
        dfs.append(json_data)
df = pd.concat(dfs, sort=False)
#df['index'] = df.groupby('timestamp_collected').cumcount()
df['index'] = range(0, len(df))
print(df)

with open(csv_fp, newline='', encoding='utf8') as csvfile:
    with open(output_fp, newline='', encoding='utf8', mode='w') as new_file:

        reader = csv.DictReader(csvfile)

        fieldnames = list(reader.fieldnames)
        fieldnames.append('timestamp_collected')
        fieldnames.append('index')

        writer = csv.DictWriter(new_file,fieldnames=fieldnames)
        writer.writeheader()

        for row in reader:
            item_id = str(row['id'])
            try:
                row['timestamp_collected'] = df[df["item_id"] == item_id]['timestamp_collected'].item()
                row['index'] = df[df["item_id"] == item_id]['index'].item()
                writer.writerow(row)
            except Exception as e:
                print(item_id)
