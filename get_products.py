import pandas as pd
import requests
from io import StringIO
from agents import function_tool

@function_tool
def get_product_data_from_sheet() ->list:
    """
    Fetches the complete list of products from the connected Google Sheet.

    Returns:
        List[Dict[str, str]]: A list of dictionaries, where each dictionary contains:
            - name (str): The product's name
            - brand (str): The product's brand
            - price (str): The product's price in PKR

    Purpose:
        This tool is used to retrieve up-to-date product information for the 
        E-commerce Customer Support Agent, enabling it to answer customer queries accurately.
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
    
    # Convert DataFrame to list of dicts
    return df.to_dict(orient="records")
