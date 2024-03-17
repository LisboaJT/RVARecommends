import pandas as pd
from django.conf import settings
from django.core.cache import cache
import os


def load_combined_results():
    # Attempt to get the cached DataFrame
    df = cache.get('combined_results_df')
    if df is None:
        csv_path = os.path.join(settings.BASE_DIR, 'data', 'combined_results.csv')
        df = pd.read_csv(csv_path)
        # Cache the DataFrame for future use, specify the cache timeout as needed
        cache.set('combined_results_df', df, timeout=3600)  # For example, cache for 1 hour
    return df
