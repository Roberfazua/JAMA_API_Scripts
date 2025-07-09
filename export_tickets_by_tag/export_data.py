# export_data.py
import pandas as pd
import json
from datetime import datetime

def export_all(projects, tags, tag_id, tickets):
    timestamp = datetime.now().strftime("%y%m%d - %H%M%S")
    # Export tickets to CSV
    csv_filename = f"{timestamp} - ExportedData.csv"
    pd.DataFrame(tickets).to_csv(csv_filename, index=False)
    # Optionally, export other data as JSON
    # (already handled in previous steps)