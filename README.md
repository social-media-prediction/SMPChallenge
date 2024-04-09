# SMP Challenge

Home: [www.smp-challenge.com](https://smp-challenge.com)  
Download: [SMPD Dataset](https://smp-challenge.com/download.html)  
Evaluation: [SMP Eval Server](https://eval.ai/web/challenges/challenge-page/543/overview)  
Leadearboard: [SMP Challenge](https://smp-challenge.com/leaderboard.html)

## [Social Media Prediction Challenge](https://smp-challenge.com)
SMP Challenge is an annual challenge that seeks excellent research teams on new ways of forecasting problems and meaningfully improving people’s social lives and business scenarios. The enormous amounts of online content lead to overconsumption, online word-of-mouth helps us to efficiently discover interesting news, emerging topics, the latest stories, or amazing products from the information ocean. Therefore, predicting online popularity became an emerging and significant task for online media, brand marketing, social influencers, or our individuals. We formulated this task as the Social Media Popularity Prediction. It focuses on predicting the impact of online post sharing on social media. It is central to various scenarios, such as online advertising, social recommendation, demand forecasting, etc.


## [SMPD Dataset](https://smp-challenge.com/download.html)  
Social Media Prediction Dataset (SMPD) is a massive-scale, multimodal, and temporal dataset with over 486K social multimedia posts from 70K users and various social media information including anonymized photo-sharing records, user profiles, images, texts, times, or other metadata. SMPD is collected from Flickr's online streams. For keeping temporal properties, we conducted a chronological split for training and testing data (commonly, by date and time).

| Dataset | Posts |  Users |  Categories  |  Time Range (Months) | Tags |
| :----:  |    :----:   |    :----:   |    :----:   |    :----:   |    :----:   |
| SMPD  | 486K  | 70K | 756 | 16  | 29  | 250K  |

## Social Media Popularity Prediction
We formulated the task as the Social Media Popularity Prediction. It focuses on predicting the impact of online post-sharing on social media. It is central to various scenarios, such as online advertising, social recommendation, demand forecasting, etc.

## Evaluation
By quantitative evaluation, we measure the systems submitted to this challenge on a testing set. We adopt multiple metrics including Spearman’s Rho (SR) and Mean Absolute Error (MAE). The ranking for the competition is based on quantitative evaluation.

## Reference
```BibTeX
@inproceedings{SMP2023,
  title={SMP Challenge: An Overview and Analysis of Social Media Prediction Challenge},
  author={Wu, Bo and Liu, Peiye and Cheng, Wen-Huang and Liu, Bei and Zeng, Zhaoyang and Wang, Jia and Huang, Qiushi and Luo, Jiebo},
  booktitle={Proceedings of the 31st ACM International Conference on Multimedia},
  year={2023}}
@inproceedings{Wu2017DTCN,
  title={Sequential Prediction of Social Media Popularity with Deep Temporal  Context Networks},
  author={Wu, Bo and Cheng, Wen-Huang and Zhang, Yongdong and Qiushi, Huang and   Jintao, Li and
  Mei, Tao},
  booktitle={International Joint Conference on Artificial Intelligence (IJCAI)},
  year={2017}}
@inproceedings{Wu2016TemporalPrediction,
  author = {Wu, Bo and Mei, Tao and Cheng, Wen-Huang and Zhang, Yongdong},
  title = {Unfolding Temporal Dynamics: Predicting Social Media Popularity Using  Multi-scale Temporal
  Decomposition},
  booktitle = {Proceedings of the Thirtieth AAAI Conference on Artificial Intelligence (AAAI)}
  year = {2016}}
@inproceedings{Wu2016time,
  title={Time matters: Multi-scale temporalization of social media popularity},
  author={Wu, Bo and Cheng, Wen-Huang and Zhang, Yongdong and Mei, Tao},
  booktitle={Proceedings of the 24th ACM international conference on Multimedia},
  year={2016}}
```
