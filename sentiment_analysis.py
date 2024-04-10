import torch
import transformers


def tokenize(tokenizer, text):
    encoded_text = tokenizer(
        text,
        None,
        pad_to_max_length=True,
        max_length=150,
        add_special_tokens=True,
        return_attention_mask=True,
    )

    # Convert the dictionary of encoded text to tensors
    return {
        "input_ids": torch.tensor(encoded_text["input_ids"], dtype=torch.long),
        "attention_mask": torch.tensor(
            encoded_text["attention_mask"], dtype=torch.long
        ),
        "token_type_ids": torch.tensor(
            encoded_text["token_type_ids"], dtype=torch.long
        ),
    }


loaded_model = torch.load("classifier/entire_model.pth")
device = torch.device("cuda")
sentiment_map = {0: "positive", 1: "neutral", 2: "negative"}

tokenizer = transformers.BertTokenizer.from_pretrained("ProsusAI/finbert")


def classify(text):
    token = tokenize(tokenizer, text)
    loaded_model.eval()
    with torch.no_grad():
        result = loaded_model(
            ids=token["input_ids"].unsqueeze(0).to(device),
            mask=token["attention_mask"].unsqueeze(0).to(device),
            token_type_ids=token["token_type_ids"].to(device),
        )
    return sentiment_map[torch.argmax(result).item()]


def get_news_sentiment(start_date, end_date, news):
    sentiment = []
    for i in range(len(news)):
        if start_date <= news[i]["date"] <= end_date:
            sentiment.append(classify(news[i]["title"]))
    return sentiment
