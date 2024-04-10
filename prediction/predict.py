from args import loadArgs
import torch
from exp.exp_main import Exp_Main
import random
import numpy as np


def predict(setting: str, data_path: str):

    # load args
    args = loadArgs(setting)

    # random seed
    fix_seed = args.random_seed
    random.seed(fix_seed)
    torch.manual_seed(fix_seed)
    np.random.seed(fix_seed)

    # check GPU status and exit if not available
    if not torch.cuda.is_available():
        print('GPU is not available')
        exit()

    args.use_gpu = True if torch.cuda.is_available() and args.use_gpu else False

    if args.use_gpu and args.use_multi_gpu:
        args.dvices = args.devices.replace(' ', '')
        device_ids = args.devices.split(',')
        args.device_ids = [int(id_) for id_ in device_ids]
        args.gpu = args.device_ids[0]

    Exp = Exp_Main

    # change data path to the one to predict
    args.data_path = data_path
    args.date_header = 'Timestamp'

    exp = Exp(args)  # set experiments
    print(
        '>>>>>>>predicting : {}<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<'.format(setting))
    preds = exp.predict(setting, True)

    torch.cuda.empty_cache()

    return preds


setting = 'AAPL_336_96_PatchTST_custom_ftM_sl336_ll48_pl96_dm128_nh16_el3_dl1_df256_fc1_ebtimeF_dtTrue_Exp_0'
preds = predict(setting)
print(preds)