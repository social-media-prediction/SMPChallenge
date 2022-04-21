# Social Media Headline Prediction Challenge (SMHP)

### Materials List
 1. Train Data (include image paths, meta data and labels)
 
    https://drive.google.com/open?id=0B7CzfJRX7ZuzWFRQUnlKTGJYUWM

 2. Train Image Urls
   
    https://drive.google.com/open?id=0B7CzfJRX7ZuzU3AxbTVsRE9pUEE

 3. Train Data for Time Zone
    
    https://drive.google.com/open?id=0B5DNzEjbQhUZdnp2cUFwQmNLbTQ
   
 4. Test Data (include image paths, meta data and without labels) 
    
    https://drive.google.com/open?id=0B5DNzEjbQhUZUXQtRjRpbkQwSE0
    
 5. Test Data for Time Zone
    
    https://drive.google.com/open?id=0B5DNzEjbQhUZVEJTclN5NWlGX2M
    
### Evaluation Script
    https://github.com/social-media-prediction/PredictionChallenge/blob/master/Task2Eval_SMHP2018.py


#### If you intend to publish results that use the information and resources provided by SMHP Challenge, please include the following references:
```
@inproceedings{Wu2017DTCN,
  title={Sequential Prediction of Social Media Popularity with Deep Temporal Context Networks},
  author={Wu, Bo and Cheng, Wen-Huang and Zhang, Yongdong and Qiushi, Huang and Jintao, Li and Mei, Tao},
  booktitle={IJCAI},
  year={2017},
  location = {Melbourne, Australia}}
@inproceedings{Wu2016TimeMatters,
  author = {Wu, Bo and Cheng, Wen-Huang and Zhang, Yongdong and Mei, Tao},
  title = {Time Matters: Multi-scale Temporalization of Social Media Popularity},
  booktitle = {ACM Multimedia},
  year = {2016},
  location = {Amsterdam, The Netherlands}}
 ```
#### Note that the data will ONLY be released to participants who have registered the challenge during the competition.
  
### Data Introduction

#### train_data.txt or test_data.txt
Each row of data has a unique picture id (pid) along with user id (uid). Also, metadata of the picture such as the posted date (postdate), category it belongs to (category and subcategory), concept, path alias for image, whether public to all users (ispublic), media status, title, media type, all tags, geo information (latitude, longitude, and geoaccuracy). In the dataset, all fields are wrapped by double quote.

```
uid pid category subcategory concept pathalias ispublic mediastatus title mediatype alltags postdate latitude geoaccuracy longitude
...
"70478@N10" "564687" "Whether&Season" "Raining" "umbrella" "None" "1" "ready" "Sarah Moon 3" "photo" "black hat fashion yellow umbrella" "1457068974" "0" "0" "0"
"37810@N60" "565202" "Fashion" "Girls,Fashion" "skirt" "None" "1" "ready" "2016-03-06 22.19.08" "photo" "orange sexy philadelphia hockey nhl sweater bra skirt blonde flowing cheerleader cleavage plaid flyers philadelphiaflyers icegirls" "1457273948" "0" "0" "0"
"25893@N22" "565381" "Whether&Season" "Raining" "puddle" "hoo_nose_68" "1" "ready" "Tristesse at the Federal Chancellery" "photo" "blackandwhite bw white black reflection berlin wet water rain canon germany puddle deutschland eos blackwhite wasser symmetry sw schwarzweiss puddles reflexion weiss federal schwarz regen tristesse trist reflektion kanzleramt pfuetze 6d nass bundeskanzleramt 2016 symmetrie pftze weis pftzen chancellery schwarzweis federalchancellery pfuetzen canoneos6d hoonose68 againstautotagging sgrossien grossien" "1457239452" "52.520213" "16" "13.373097"
...
```


#### train_label.txt

The label file contains the popularity score (log-views). The picture id and user id of the labels are corresponding with associate data raws in data files.
```
popularityscore
...
3.2
2.3
...
```

#### test_label.json (example)

```
   {
    "version": "VERSION 1.2",
    "result": [
        {
            "post_id": "post6374637",
            "ranking_position": 1,
            "popularity_score": 2.1345
        },
        ...
        {
            "post_id": "post3637373",
            "ranking_position": 5,
            "popularity_score": 3.1415
        }
    ],
    "external_data": {
        "used": "true",
        "details": "VGG-19 pre-trained on ImageNet training set"
    }
}

```

