from scipy import stats
# from sklearn.metrics import mean_squared_error
# from sklearn.metrics import mean_absolute_error
import json
import pandas as pd
import os
import numpy as np

def evaluate(json_file_path, ground_truth_file):

    y_truth = load_json(ground_truth_file,1)
    y_pred = load_json(json_file_path,0)

    # print("%d vs %d"%(len(y_truth),len(y_pred)))
    if len(y_truth)!=len(y_pred):
        raise Exception('num of pred result incorrect!')

    spearmanr_corr = stats.spearmanr(y_truth, y_pred)[0]

    y_truth = np.array(y_truth)
    y_pred = np.array(y_pred)

    # print(y_truth.shape, y_pred.shape)

    # mse = np.mean((y_truth - y_pred) ** 2)

    mae = np.mean(np.abs(y_truth - y_pred))

    return spearmanr_corr, mae


def load_json(json_file_path,true_val):
    json_str = open(json_file_path,'r').read()
    # json_result = json.loads(json_str)['result']
    if json_str[0]=='[':
            json_result = json.loads(json_str)[0]["result"]
    else:
            json_result = json.loads(json_str)["result"]

    result = {"post_id":[],"popularity_score":[]}
    for row in json_result:
        # if true_val:
        #         # print row["post_id"][4:]
        #         result["post_id"].append((row["post_id"]))
        # else:
        #         result["post_id"].append('post'+str((row["post_id"])))
        result["post_id"].append((row["post_id"]))
        result["popularity_score"].append(row["popularity_score"])
    dataframe = pd.DataFrame(result)

    # print dataframe.sort_values('post_id')['post_id'].tolist()[0:10]
    # return dataframe.sort_values('post_id')['popularity_score'].tolist()
    return dataframe["popularity_score"].tolist()

def load_json_postid(json_file_path):
    json_str = open(json_file_path,'r').read()

    if json_str[0]=='[':
            json_result = json.loads(json_str)[0]["result"]
    else:
            json_result = json.loads(json_str)["result"]
    result = {"post_id":[],"popularity_score":[]}
    for row in json_result:
        result["post_id"].append(row["post_id"])
        result["popularity_score"].append(row["popularity_score"])
    dataframe = pd.DataFrame(result)
    return dataframe.sort_values('post_id')['post_id'].tolist()


# EXAMPLE USAGE
# evaluate('./test-sample.json','./validation.json')
