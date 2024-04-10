import requests
import pandas as pd
from sentiment_analysis import classify

start = "20220101T0001"


def get_news_sentiment(start_time, end_time):
    try:
        url = f"https://www.alphavantage.co/query?function=NEWS_SENTIMENT&tickers=AAPL&apikey=DVNF5GFMRR0ES1J6&sort=EARLIEST&limit=1000&time_from={start_time}&time_to={end_time}"
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception if the request was unsuccessful

        json_data = response.json()
        if json_data["items"] is None:
            print("No data found")

    except Exception as e:
        print("Error occurred:", e)
        return

    feed = json_data["feed"]
    print(len(feed))

    # create dataframe with colums time_published, summary, and sentiment
    df = pd.DataFrame(columns=["time_published", "summary", "sentiment"])

    # add feed["time_published"] and feed["summary"] to the dataframe
    df["time_published"] = [item["time_published"] for item in feed]
    df["summary"] = [item["summary"] for item in feed]

    # iterate through df and add sentiment to the dataframe
    for i in range(len(df)):
        score = feed[i]["overall_sentiment_score"]
        if score > 0.15:
            df["sentiment"][i] = "positive"
        elif score < -0.15:
            df["sentiment"][i] = "negative"
        else:
            df["sentiment"][i] = "neutral"

        # Use this when model is ready
        # df["sentiment"][i] = classify("good")

    print(df.head())


get_news_sentiment("20220101T0001", "20221231T2359")
