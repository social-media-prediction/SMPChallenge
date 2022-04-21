from scipy import stats
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
import json
import pandas as pd
import os


def calc_mae(pred_df,truth_df):

  pred_df = sorted(pred_df, key=lambda x:x['post_id'])
  pred_df = pd.DataFrame(pred_df)
  truth_df = sorted(truth_df, key=lambda x:x['post_id'])
  truth_df = pd.DataFrame(truth_df)

  truth_pops = truth_df['popularity_score'].tolist()
  pred_pops = pred_df['popularity_score'].tolist()
  mae=mean_absolute_error(truth_pops, pred_pops)
  return mae

def calc_spearman(pred_df,truth_df):

  pred_df = sorted(pred_df, key=lambda x:x['post_id'])
  pred_df = pd.DataFrame(pred_df)
  truth_df = sorted(truth_df, key=lambda x:x['post_id'])
  truth_df = pd.DataFrame(truth_df)

  truth_pops = truth_df['popularity_score'].tolist()
  pred_pops = pred_df['popularity_score'].tolist()
  spearmanr_corr = stats.spearmanr(truth_pops, pred_pops)[0]
  return spearmanr_corr

# MAE, Spearmanr's Rho
def evaluate(json_file_path,ground_truth_file,hit_top=5):
  print ground_truth_file
  pred_df = load_json(json_file_path)
  truth_df = load_json(ground_truth_file)
  mae = calc_mae(pred_df,truth_df)
  spearmanr = calc_spearman(pred_df,truth_df)
  print("MAE: %.4f, Spearman: %.4f"%(json_file_path,mae,spearmanr))

def load_json(json_file_path):
  json_str = open(json_file_path,'r').read()
  json_result = json.loads(json_str)['result']

  return json_result

# use this method as main method
# directory: a directory contains all candidates' json submission
# ground_truth_file: a json file contains the ground truth
def evaluate_jsons(directory,ground_truth_file):
  for filename in os.listdir(directory):
    if filename.endswith(".json"):
        json_file_path = (os.path.join(directory, filename))
        evaluate(json_file_path,ground_truth_file)

team_list = ["team_name"]
# EXAMPLE USAGE
for team_name in team_list:
  print 'team_name', team_name
  evaluate_jsons(team_name,'./T2Validation.json')#../


