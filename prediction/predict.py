from args import loadArgs
import torch
import numpy as np
from models import PatchTST
import os


def predict(setting: str):

    # load args
    args = loadArgs(setting)
    model = PatchTST.Model(args).float()
    path = os.path.join("./prediction/results/", setting, 'checkpoints')
    best_model_path = path + '/' + 'checkpoint.pth'
    model.load_state_dict(torch.load(
        best_model_path, map_location=torch.device('cpu')))
    batch_x = torch.rand(1, args.seq_len, 10).to(torch.device('cpu'))
    outputs = model(batch_x)
    pred = outputs.detach().cpu().numpy()[0]  # .squeeze()
    return pred


setting = 'PatchTST_AAPL_336_96'
preds = predict(setting)
print(preds.shape)
