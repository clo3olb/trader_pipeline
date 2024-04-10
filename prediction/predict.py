import torch
import numpy as np
from models import PatchTST
import os
import pickle

# './prediction/results/PatchTST_AAPL_336_96/args.pkl'
# "./prediction/results/PatchTST_AAPL_336_96/checkpoints/checkpoint.pth"


def loadArgs(path: str):
    with open(path, 'rb') as f:
        args = pickle.load(f)
        return args


def predict(model_path: str, args_path: str, data: np.ndarray):

    # Load model
    args = loadArgs(args_path)
    model = PatchTST.Model(args).float()
    path = os.path.join(model_path)
    model.load_state_dict(torch.load(
        path, map_location=torch.device('cpu')))

    # Predict
    batch_x = torch.tensor(data).float().to(torch.device('cpu'))
    outputs = model(batch_x)
    pred = outputs.detach().cpu().numpy()[0]  # .squeeze()
    return pred
