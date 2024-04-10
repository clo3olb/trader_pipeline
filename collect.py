from dotenv import dotenv_values
from collection.alphavantage import getMonths, createMergedCSV, fetchDailyPriceData
import os
import pandas as pd
from collection import alphavantage

# Load the environment variables from the .env file
env_vars = dotenv_values("local.env")

symbols = [
    "AAPL", "MSFT", "AMZN", "GOOGL", "NFLX",
    "JPM", "BAC", "C", "WFC", "GS",
    "KO", "PG", "MCD", "DIS", "NKE",
    "JNJ", "PFE", "MRK", "ABT", "BMY",
    "XOM", "CVX", "COP", "SLB", "PSX",
]


interval = "15min"
month = "2022-01"
api_key = env_vars['ALPHA_VANTAGE_API_KEY']
file_path = "./data/alphavantage/2022-01_AAPL.csv"

data = alphavantage.getMonthlyData("AAPL", interval, month, api_key, file_path)
print(data.head())
