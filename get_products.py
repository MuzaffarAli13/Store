import pandas as pd
import requests
from io import StringIO
from agents import function_tool

@function_tool
def get_product_data_from_sheet()->list:
    """
    Fetches the complete list of products from the connected Google Sheet.

    Returns:
        list: A list of dictionaries, where each dictionary contains:
            - name (str): The product's name
            - brand (str): The product's brand
            - price (float): The product's price

    Purpose:
        This tool is used to retrieve up-to-date product information for the E-commerce Customer Support Agent,
        enabling it to answer customer queries accurately.
    """
    
    sheet_url = "https://docs.google.com/spreadsheets/d/1H-CZXBiWAKAzHu6oRWDQCiLWezHxp6XnjPYA5t-nYXE/export?format=csv&gid=0"
    
    try:
        response = requests.get(sheet_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        return [{"error": f"Failed to fetch data from Google Sheet: {e}"}]
    
    try:
        df = pd.read_csv(StringIO(response.text))
    except Exception as e:
        return [{"error": f"Failed to parse CSV data: {e}"}]
    
    return df.to_dict(orient="records")
