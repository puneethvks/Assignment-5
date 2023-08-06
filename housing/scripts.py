"""Module for listing down additional custom functions required for the notebooks."""

import pandas as pd

def median_house_value(df):
    """Bin the selling price column using quantiles."""
    return df["median_house_value"]