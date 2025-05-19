import pandas as pd

def export_to_csv(profiles, filename="latam_output.csv"):
    df = pd.DataFrame(profiles)
    df.to_csv(filename, index=False)
    print(f"[+] Exported {len(df)} records to {filename}")
