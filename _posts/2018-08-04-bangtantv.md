---
layout: post
comments: true
title: "An Analysis on BANGTANTV"
date: 2018-08-04
header: assets/bangtantv-header.png
image: assets/bangtantv-header.png
description: I tried scraping BTS' videos from BANGTANTV and here's what I found out.
---


Hey everyone! I'm excited to share this new project I've been working on for the past few days. As you all know (or didn't know), I'm a huge fan of the Korean group [BTS](https://en.wikipedia.org/wiki/BTS_(band)). They're a 7-member group that sings, raps, and dances well. They have a huge amount of content so I have always wanted to visualize their data to gain new insights about the group. [BANGTANTV](https://www.youtube.com/user/BANGTANTV/videos) is their official YouTube channel where they post videos about their daily lives, dance practices, logs, etc. It currently holds over 850+ videos and they recently hit 10M subscribers, so I was really excited to crunch their data through their YouTube channel. Throughout the blog post, I will be highlighting my favorite videos using :sparkles:. But enough of the intro, let's get to the process and the results!

The first thing I did was to scrape the data using the YouTube Data API. This was the first time I tried scraping data so I spent a lot of time trying to understand how the YouTube Data API works and how I can ask queries. It was a challenge since I had to go through three queries just to get the statistics of each video in BANGTANTV. But all in all, the tutorials and sample codes provided by YouTube was easy to follow so I was able to grasp on the proper sequence of queries. I also did a lot of data transformation to get the ID for each video and get its statistics. After scraping the data, I loaded the json file and flattened it to get my dataset.

**NOTE: I scraped the data last July 29, 2018 at 10 PM KST. All data and results below are based from the snapshot I made from this specific time and date.**


```python
import numpy as np
import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import datetime
import os
import json
import math
import seaborn as sns
import matplotlib.patches as mpatches
from matplotlib.colors import LinearSegmentedColormap, ColorConverter
import re
import matplotlib.dates as dates
from matplotlib.ticker import MaxNLocator
from pandas.io.json import json_normalize
import dateutil.parser
import aniso8601
from IPython.display import HTML
%matplotlib inline

pd.set_option('display.max_columns', None)
```


```python
json_videos = json.load(open('bangtantv_vids.json', encoding="utf8"))
videos = pd.DataFrame(json_normalize(json_videos['items']))
```


```python
header = ["contentDetails.videoId"]
videos.to_csv('videoIds.csv', columns=header, index=False)
```


```python
json_videoIds = json.load(open('videoIds.json', encoding="utf8"))
videoIds = pd.DataFrame(json_normalize(json_videoIds['items']))
```

After loading the data, I "cleaned" it by converting some values to its appropriate datatype.


```python
videoIds['contentDetails.duration'] = videoIds.apply(lambda row: aniso8601.parse_duration(row['contentDetails.duration']).total_seconds(), axis=1)
```


```python
videoIds['contentDetails.duration'].sum()
```

BTS has a total of 856 videos (as of July 29, 2018 at 10 PM KST). They started their account last December 16, 2012 and now has 1.5B+ views in total. BANGTANTV videos has a total duration of 2 days, 6 hours, and 36 seconds. To hardcore ARMYs who want to binge-watch BTS videos, you can allot 2 days of your life for it!


```python
videoIds.loc[videoIds['contentDetails.duration'].idxmin()]
```

**DID YOU KNOW?** The shortest video is **'[BANGTAN BOMB] 더우시죠? It is hot today, isn't it?'** clocking in with only 7 seconds. (I'm not going to complain over Jungkook fanning me for 7 seconds though). Here's the gem if you want a refresher: 


<a href="https://youtu.be/d3RgIc1AW7Y" target="_blank"><img src="https://i.ytimg.com/vi/d3RgIc1AW7Y/maxresdefault.jpg" 
alt="[BANGTAN BOMB] 더우시죠? It is hot today, isn't it?"/></a>


```python
videoIds.loc[videoIds['contentDetails.duration'].idxmax()]
```

**DID YOU KNOW?** The longest video is **'[FESTA 2017] BTS (방탄소년단) 꿀 FM 06.13 Happy BTS birthday!'** with 1 hour, 23 minutes, and 41 seconds. If you want to reminisce their FESTA 2017 Kkul FM, here's the link:


<a href="https://www.youtube.com/watch?v=cWA6f7g7NUQ" target="_blank"><img src="https://i.ytimg.com/vi/cWA6f7g7NUQ/maxresdefault.jpg" 
alt="[FESTA 2017] BTS (방탄소년단) 꿀 FM 06.13 Happy BTS birthday!"/></a>


# VIEWS

The first thing that comes in to mind when you talk about YouTube videos is the amount of views. BTS gradually grew a lot of viewers and subscribers so it's necessary to check which videos became a huge hit. With one line of code, I was able to extract the video with the highest and lowest number of views in BANGTANTV.


```python
videoIds['statistics.viewCount'] = videoIds['statistics.viewCount'].astype(float)
```


```python
videoIds.loc[videoIds['statistics.viewCount'].idxmax()]
```

The video with the highest views is **'[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)'** with 63.64 million views. This isn't surprising at all as this video is ranked [#17 as most viewed in the last 24 hours the day it was released](https://onehallyu.com/topic/598077-bts-go-go-dance-practice-ranked-17-as-most-viewed-in-the-last-24-hours/). 

To feed my curiosity more on the top videos in BANGTANTV, I've enumerated the top 10 videos with the highest and lowest number of views.


```python
top10_highest_views = videoIds.nlargest(10, 'statistics.viewCount')
top10_highest_views
```


## 10 Most-Viewed Videos in BANGTANTV

Video | Views | Year
:---|---:|---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 63,641,290 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 37,046,200 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 32,679,447 | 2016
[방탄소년단 'I NEED U' Dance Practice](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 29,434,845 | 2015                                                          
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 28,343,359 | 2014                                                             
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 25,950,392 | 2017                                          
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 24,491,873 | 2016
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 23,511,936 | 2015                                  
[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 22,244,522 | 2018                                          
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 18,915,957 | 2016

<p> </p>

Their top 10 highest viewed videos are all dance practices with an exception of one, their performance of Airplane pt. 2 in their comeback show.


```python
top10_smallest_views = videoIds.nsmallest(10, 'statistics.viewCount')
top10_smallest_views
```

## 10 Least-Viewed Videos in BANGTANTV

Video | Views | Year
:--- | ---: | :---
[130324 J HOPE](https://www.youtube.com/watch?v=cdbTO7UE81g) | 22,658 | 2013
[140103 제이홉](140103 제이홉) | 22,667 | 2014
[130904 진](https://www.youtube.com/watch?v=SL90Pe2VZ4M) | 24,953 | 2013
[131012 진](131012 진) | 25,061 | 2013                                                          
[130825 랩몬스터](https://www.youtube.com/watch?v=E4bzagMrGPk) | 25,244 | 2013                                                             
[130829 제이홉](https://www.youtube.com/watch?v=6axIdOnSrBI) | 25,415 | 2013                                          
[130118 RAP MONSTER](https://www.youtube.com/watch?v=L5ohdoW3YRU) | 25,506 | 2013
[130728 j hope](https://www.youtube.com/watch?v=chnBPfL6MUg) | 25,996 | 2013                                  
[131017 랩몬스터](https://www.youtube.com/watch?v=zXII5svk9KE) | 27,683 | 2013                                          
[130724 랩몬스터](https://www.youtube.com/watch?v=V8RmTPnWVfA) - BTS (방탄소년단) | 28,163 | 2013

<p> </p>

Sadly, their 10 lowest videos are all BTS logs but don't fret! They're all dated way back in 2013 and 2014 and because BANGTANTV do not produce their own subs, it was understandable that they'd get the lowest views.

Now, let's get the top 10 videos with the highest views per year (from 2013 - 2018). Note that I didn't include 2012 as BANGTANTV only uploaded 3 videos during this year.


```python
aniso8601.parse_datetime('2017-10-27T13:00:00.000Z')
```

```python
videoIds['snippet.publishedAt'] = videoIds.apply(lambda row: aniso8601.parse_datetime(row['snippet.publishedAt']), axis=1)
```


```python
videoIds['snippet.publishedAt.year'] = videoIds.apply(lambda row: row['snippet.publishedAt'].year, axis=1)
```


```python
pd.set_option('display.max_colwidth', -1)
vids_2018 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2018]
top10_highest_views_2018 = vids_2018.nlargest(10, 'statistics.viewCount')
top10_highest_views_2018
```


## 10 Most-Viewed Videos of BANGTANTV in 2018

Video | Views
:--- | ---: | :---
[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 22,244,522
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 18,396,812
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 13,864,096                                                          
[BTS (방탄소년단) - Anpanman @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=lOf16ZQDDdE) | 13,101,712        
[Official Trailer &#124; BTS: Burn The Stage](https://www.youtube.com/watch?v=xf-dywd3zx0) | 7,507,120
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 6,706,541                                         
[BTS (방탄소년단) - FAKE LOVE @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Hoz5OQjXEA8) | 6,351,694
:sparkles: [[BANGTAN BOMB] j-hope & Jimin Dancing in Highlight Reel (Focus ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 6,220,580                                  
:sparkles: [G.C.F in Osaka](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 5,999,901                                         
[[BANGTAN BOMB] 'MIC Drop' Special Stage (BTS focus) @MAMA - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 5,973,321

<p> </p>

For 2018, it was predictable to get their comeback show performances in the top 10 and JK's G.C.F. But what caught my eye was the Bangtan Bomb 'j-hope & Jimin Dancing in Highlight Reel (Focus ver.)'. I didn't expect this to be in the top 10 so I watched it again and regretted not expecting this on the top 10. I want to share to you all the glory of Hobi and Jimin's dancing so here's the link: 


<a href="https://www.youtube.com/watch?v=Zq89pRZqhk0" target="_blank"><img src="https://i.ytimg.com/vi/Zq89pRZqhk0/maxresdefault.jpg" 
alt="j-hope & Jimin Dancing in Highlight Reel (Focus ver.)"/></a>



```python
vids_2017 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2017]
top10_highest_views_2017 = vids_2017.nlargest(10, 'statistics.viewCount')
top10_highest_views_2017
```


## 10 Most-Viewed Videos of BANGTANTV in 2017

Video | Views
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 22,244,522
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 63,641,290
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 18,037,540                                                          
[[CHOREOGRAPHY] BTS (방탄소년단) '봄날 (Spring Day)' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 16,213,155        
[[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 13,802,749
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 12,131,897                                         
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 11,820,890
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 11,019,375                                 
:sparkles: [G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=XrTNLkqGrlc) | 10,185,890                                         
[[BANGTAN BOMB] '고민보다 GO (Halloween ver.)' Behind - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 7,701,114

<p> </p>

Their top videos on 2017 were mostly their FESTA content. If you didn't know, FESTA is a more-than-a-week long celebration of their anniversary, so BTS posts a lot of content during this time. G.C.F. in Tokyo is also placed in its rightful throne. But you know their GO GO Dance Practice was such a huge hit that even its behind the scenes video reached the top ten in 2017.


```python
vids_2016 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2016]
top10_highest_views_2016 = vids_2016.nlargest(10, 'statistics.viewCount')
top10_highest_views_2016
```

## 10 Most-Viewed Videos of BANGTANTV in 2016

Video | Views
:--- | ---: | :---
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice 	](https://www.youtube.com/watch?v=v8z1TtlY1no) | 37,046,200
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 32,679,447
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 24,491,873                                                         
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 18,915,957        
[[BANGTAN BOMB] 'Coming of age ceremony' Dance cover by Jimin & Jung Kook - BTS (방탄소년단)](https://www.youtube.com/watch?v=D4oIpsRemPA) | 9,834,735
[[CHOREOGRAPHY] BTS (방탄소년단) 정국이랑 지민이 ('Own it' choreography by Brian puspose) Dance practice](https://www.youtube.com/watch?v=HMprwPSFLyU) | 7,796,610                                         
[[BANGTAN BOMB] BTS (방탄소년단) a 400-meter relay race @ 2016 설특집 아육대](https://www.youtube.com/watch?v=9J-yfCdBbIY) | 7,428,177
[[BANGTAN BOMB] BTS' Relay race @ 2016 추석특집 아육대 - BTS (방탄소년단)](https://www.youtube.com/watch?v=0gqOz1OO-88) | 7,016,370                                 
:sparkles: [[BANGTAN BOMB] V's Dream came true - 'His Cypher pt.3 Solo Stage' - BTS (방탄소년단)](https://www.youtube.com/watch?v=GQ0XGbHjKRE) | 6,462,349                             
:sparkles: [[BANGTAN BOMB] Show Me Your BBA SAE!?!? - BTS (방탄소년단)](https://www.youtube.com/watch?v=ttSLLgU8F_I) | 6,306,461

<p> </p>

This was hard to predict as I wasn't a fan back in 2016 so I think I haven't seen half of the videos here in the list. (Please don't judge me, ARMY!) 

Actually, I want to thank this opportunity of allowing me to analyze BANGTANTV or else I wouldn't have found this gem. It has added 10 years to my life!! 

<a href="https://www.youtube.com/watch?v=ttSLLgU8F_I" target="_blank"><img src="https://i.ytimg.com/vi/ttSLLgU8F_I/maxresdefault.jpg" 
alt="Show Me Your BBA SAE!?!?"/></a>



```python
vids_2015 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2015]
top10_highest_views_2015 = vids_2015.nlargest(10, 'statistics.viewCount')
top10_highest_views_2015
```

## 10 Most-Viewed Videos of BANGTANTV in 2015

Video | Views
:--- | ---: | :---
[방탄소년단 'I NEED U' Dance Practice](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 29,434,845
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 23,511,936
:sparkles: [Rap Monster 'Do You' MV](https://www.youtube.com/watch?v=0XAxf8aFtL4) | 17,744,966                                                         
[방탄소년단 'RUN' Dance practice 	](https://www.youtube.com/watch?v=9S3ZhJGv8JM) | 17,636,564        
:sparkles: [안아줘 (Hug me) performed by V, j-hope 	](https://www.youtube.com/watch?v=tv_HQ-0upns) | 12,073,128
:sparkles: [[BANGTAN BOMB] it's tricky is title! BTS, here we go! (by Run–D.M.C.) 	](https://www.youtube.com/watch?v=PSdgzdDMIeE) | 11,931,523                                         
[방탄소년단 '쩔어' Dance Practice 	](https://www.youtube.com/watch?v=NnbIIXNPtPU) | 11,090,074
:sparkles: [방탄소년단-BTS- Special choreography Stage #2. 이불킥(Embarrassed) for 2015 FESTA](https://www.youtube.com/watch?v=Cvz-50w3IiE) | 8,501,420                                 
[Rap Monster '농담' MV 	](https://www.youtube.com/watch?v=TfenCTabhDY) | 7,982,668                                        
:sparkles: [[BANGTAN BOMB] UP DOWN UP UP DOWN (by EXID)](https://www.youtube.com/watch?v=5gEqOtODMH4) | 6,118,248

<p> </p>

At this point while I'm doing my analysis I've been feeling really regretful for not having to know that these kinds of videos exist! This just proves how BTS post a lot of free content that I just can't keep up! Enough of the fangirling, let's get to the serious parts. RM's MVs from his mixtape deserves its rightful place here in the top 10. V and J-Hope's version of Hug Me was also a hit so I kind of expected this video as well. Of course, it isn't a top 10 without BTS' dance practices. This goes to show that BTS aren't just some kind of band, they are *that* band (which I mean of course that their choreography and dancing skills are just one of their main assets).


```python
vids_2014 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2014]
top10_highest_views_2014 = vids_2014.nlargest(10, 'statistics.viewCount')
top10_highest_views_2014
```

## 10 Most-Viewed Videos of BANGTANTV in 2014

Video | Views
:--- | ---: | :---
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 28,343,359
[[BANGTAN BOMB] 'Just one day' practice (Appeal ver.)](https://www.youtube.com/watch?v=zNJMa43UVs0) | 17,306,745
[[BANGTAN BOMB] War of hormone in Halloween](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 14,960,302                                                        
[[BANGTAN BOMB] 방탄도령단 - 危險 (Appeal ver.)](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 11,620,014        
[방탄소년단 'Beautiful' dance practice](https://www.youtube.com/watch?v=sm4FFFBgbmg) | 10,718,401
[방탄소년단 '호르몬전쟁' Dance practice](https://www.youtube.com/watch?v=JumcC5jFcQc) | 8,825,709                                        
:sparkles: [[BANGTAN BOMB] Someone like you (sung & produced by V)](https://www.youtube.com/watch?v=56jN9-cMEBU) | 6,585,528
:sparkles: [[BANGTAN BOMB] Just watching Jung Kook lip sync show](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 6,446,505                                 
[[BANGTAN BOMB] Jump! Jimin entered the high jump!](https://www.youtube.com/watch?v=ivjnwAR91Sk) | 5,663,526                                         
[[BANGTAN BOMB] when BTS was practicing the showcase](https://www.youtube.com/watch?v=QKeXCmmpk28) | 5,461,331

<p> </p>

For 2014, there are more and more videos I haven't seen. Also, Danger deserves that top spot! I really loved their Danger choreo and while some people called that title track a flop (smh on these people), I think Danger really showed how BTS can up their game with a complicated dance routine. I also must give a shoutout to V's cover of Someone like you! This was one of the first videos I've seen in BTS and I'm so glad it's in the top 10 for this year.


```python
vids_2013 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2013]
top10_highest_views_2013 = vids_2013.nlargest(10, 'statistics.viewCount')
top10_highest_views_2013
```


## 10 Most-Viewed Videos of BANGTANTV in 2013

Video | Views
:--- | ---: | :---
[방탄소년단 We Are Bulletproof Pt.2 dance practice](https://www.youtube.com/watch?v=bV9Svms-LYY) | 11,342,973
[방탄소년단 SBS 가요대전 performance practice](https://www.youtube.com/watch?v=j2rS6vXApF0) | 8,240,594
[방탄소년단 BTS Dance break Practice](https://www.youtube.com/watch?v=xJg_FvMe4hE) | 7,160,389                                                          
[방탄소년들의 졸업](https://www.youtube.com/watch?v=sctrgmZ_JNM) | 7,056,277        
[방탄소년단 '진격의 방탄 (Attack on BTS)' Dance Practice](https://www.youtube.com/watch?v=ncRNKuwOEc0) | 6,613,310
:sparkles: [[BANGTAN BOMB] N.O (Trot ver.) by Jungkook and (Opera ver.) by BTS](https://www.youtube.com/watch?v=Qs2unC6IwBc) | 4,965,081                                         
:sparkles: [Beautiful by 방탄소년단 	](https://www.youtube.com/watch?v=f9_sHgPVQgM) | 4,774,546
[[BANGTAN BOMB] BTS Magic show](https://www.youtube.com/watch?v=VNfRVWGi-YQ) | 3,010,385                                 
[[BANGTAN BOMB] Jimin's 'GIRL'S DAY- FEMALE PRESIDENT' dance](https://www.youtube.com/watch?v=QUry0K0KE78) | 28,174,75                                        
[Dance practice by J-HOPE&지민&정국](https://www.youtube.com/watch?v=E8Z0aWn9T0o) | 2,544,500

<p> </p>

As what I've mentioned before, BTS' dance practices have always been placed at the top. But I didn't expect N.O (Trot ver.) to be here! I acknowledge this is a classic, but I probably forgotten that this was released early on in their career. Plus, who wouldn't forget about their iconic video of 'Beautiful'? This was such an awkward phase but I love it.

# LIKES


```python
videoIds['statistics.likeCount'] = videoIds['statistics.likeCount'].astype(float)
```


```python
videoIds.loc[videoIds['statistics.likeCount'].idxmax()]
```


The video with the highest number of likes is still **'[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)'** with 1.54M likes.


```python
top10_highest_likes = videoIds.nlargest(10, 'statistics.likeCount')
top10_highest_likes
```


## 10 Most-Liked Videos of BANGTANTV

Video | Likes | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 1,538,722 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 1,257,967 | 2018
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 991,707 | 2018                                                          
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=RbctNBlXBJc) | 928,815 | 2017        
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=GEIU_7v40Dw) | 921,266 | 2017
:sparkles: [G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=XrTNLkqGrlc) | 920,742 | 2017                                        
:sparkles: [G.C.F in Saipan 	](https://www.youtube.com/watch?v=M1F1RxkXrDE) | 920,561 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA 	](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 883,767 | 2018                                
:sparkles: [G.C.F in Osaka 	](https://www.youtube.com/watch?v=PMEkmiQP5bg) | 882,359 | 2018                                       
:sparkles: [G.C.F in USA](https://www.youtube.com/watch?v=9Lb6ta2bPu4) | 879,408 | 2018

<p> </p>

Amazing how all of JK's G.C.F. videos reached the top 10 in terms of number of likes even when they were just released recently!  It was also interesting how Jimin and JK's cover of 'We don't talk anymore' reached the upper half of this list. It must have gained a lot of likes especially with the JKxCharliePuth interactions!

Below is the list for the top 10 videos with the most likes for each year.


```python
vids_likes_2018 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2018]
top10_highest_likes_2018 = vids_likes_2018.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2018
```


## 10 Most-Liked Videos of BANGTANTV in 2018

Video | Likes
:--- | ---: | :---
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 1,257,967
[I’d do it all &#124; BTS: Burn the Stage Ep1 	](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 991,707
:sparkles: [G.C.F in Saipan 	](https://www.youtube.com/watch?v=M1F1RxkXrDE) | 920,561                                                          
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA 	](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 883,767        
:sparkles: [G.C.F in Osaka](https://www.youtube.com/watch?v=PMEkmiQP5bg) | 882,359
:sparkles: [G.C.F in USA](https://www.youtube.com/watch?v=9Lb6ta2bPu4) | 879,408                                         
[[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW 	](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 835,497
[BTS (방탄소년단) - Anpanman @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=lOf16ZQDDdE) | 726,775                                 
[BTS (방탄소년단) 'FAKE LOVE' Self MV @Music Bank Encore stage 	](https://www.youtube.com/watch?v=K6le0eU02mE) | 609,415                                        
[BTS (방탄소년단) '방탄회식' #2018BTSFESTA 	](https://www.youtube.com/watch?v=K4Melso7MPU) | 567,879

<p> </p>

The 'FAKE LOVE' Self MV was a surprise but it definitely deserves its spot!


```python
vids_likes_2017 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2017]
top10_highest_likes_2017 = vids_likes_2017.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2017[['snippet.title', 'statistics.likeCount']]
```


## 10 Most-Liked Videos of BANGTANTV in 2017

Video | Likes
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단) 	](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 1,538,722
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore' 	](https://www.youtube.com/watch?v=RbctNBlXBJc) | 928,815
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice 	](https://www.youtube.com/watch?v=GEIU_7v40Dw) | 921,266                                                          
:sparkles: [G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=XrTNLkqGrlc) | 920,742        
[G[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 591,858
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=W5JB4XsjSXY) | 591,781                                        
:sparkles: [[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=u2XBh23upio) | 565,300
[[CHOREOGRAPHY] BTS (방탄소년단) '봄날 (Spring Day)' Dance Practice](https://www.youtube.com/watch?v=_AlODdAInRY) | 561,624                                 
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 539,318                                        
[[BANGTAN BOMB] BTS 'MIC Drop' MV reaction - BTS (방탄소년단)](https://www.youtube.com/watch?v=HQsyxzOCuWA) | 529,320

<p> </p>

```python
vids_likes_2016 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2016]
top10_highest_likes_2016 = vids_likes_2016.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2016[['snippet.title', 'statistics.likeCount']]
```


## 10 Most-Liked Videos of BANGTANTV in 2016

Video | Likes
:--- | ---: | :---
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice 	](https://www.youtube.com/watch?v=v8z1TtlY1no) | 795,207
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 668,833
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 567,388                                                          
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 446,302        
[[CHOREOGRAPHY] BTS (방탄소년단) 정국이랑 지민이 ('Own it' choreography by Brian puspose) Dance practice](https://www.youtube.com/watch?v=HMprwPSFLyU) | 398,117
:sparkles: [[BANGTAN BOMB] Show Me Your BBA SAE!?!? - BTS (방탄소년단)](https://www.youtube.com/watch?v=ttSLLgU8F_I) | 345,326                                         
[[BANGTAN BOMB] 'Coming of age ceremony' Dance cover by Jimin & Jung Kook - BTS (방탄소년단)](https://www.youtube.com/watch?v=D4oIpsRemPA) | 337,123
:sparkles: [[BANGTAN BOMB] V's Dream came true - 'His Cypher pt.3 Solo Stage' - BTS (방탄소년단)](https://www.youtube.com/watch?v=GQ0XGbHjKRE) | 328,534                                
[[BANGTAN BOMB] 'WINGS' Short Film Special - Lie (Jimin solo dance) - BTS (방탄소년단)](https://www.youtube.com/watch?v=IUhmH7Qqkso) | 264,777                                      
:sparkles: [[BANGTAN BOMB] BTS' Vocal Duet 'SOPE-ME' Stage behind the scene - BTS (방탄소년단)](https://www.youtube.com/watch?v=nac1hoha570) | 219,130

<p> </p>

Glad that a SOPE stage reached the top 10 in terms of likes! 


```python
vids_likes_2015 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2015]
top10_highest_likes_2015 = vids_likes_2015.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2015[['snippet.title', 'statistics.likeCount']]
```


### 10 Most-Liked Videos of BANGTANTV in 2015

Video | Likes
:--- | ---: | :---
:sparkles: [Rap Monster 'Do You' MV](https://www.youtube.com/watch?v=0XAxf8aFtL4) | 729,499
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.) 	](https://www.youtube.com/watch?v=70SMjxn4FBA) | 495,325
[방탄소년단 'I NEED U' Dance Practice 	](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 464,221                                                          
:sparkles: [안아줘 (Hug me) performed by V, j-hope](https://www.youtube.com/watch?v=tv_HQ-0upns) | 451,954        
[Rap Monster '농담' MV 	](https://www.youtube.com/watch?v=TfenCTabhDY) | 378,279
[방탄소년단 'RUN' Dance practice](https://www.youtube.com/watch?v=9S3ZhJGv8JM) | 378,010                                         
:sparkles: [[BANGTAN BOMB] it's tricky is title! BTS, here we go! (by Run–D.M.C.)](https://www.youtube.com/watch?v=PSdgzdDMIeE) | 311,538
:sparkles: [방탄소년단-BTS- Special choreography Stage #2. 이불킥(Embarrassed) for 2015 FESTA](https://www.youtube.com/watch?v=Cvz-50w3IiE) | 226,235                                
[[BANGTAN BOMB] 'RUN' christmas ver.](https://www.youtube.com/watch?v=Cvz-50w3IiE) | 221,571                                     
[방탄소년단 '쩔어' Dance Practice](https://www.youtube.com/watch?v=NnbIIXNPtPU) | 197,355

<p> </p>

Do You at #1 and Awakening at #5! 


```python
vids_likes_2014 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2014]
top10_highest_likes_2014 = vids_likes_2014.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2014[['snippet.title', 'statistics.likeCount']]
```


## 10 Most-Liked Videos of BANGTANTV in 2014

Video | Likes
:--- | ---: | :---
[[BANGTAN BOMB] War of hormone in Halloween](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 396,042
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 366,512
:sparkles: [[BANGTAN BOMB] Someone like you (sung & produced by V)](https://www.youtube.com/watch?v=56jN9-cMEBU) | 340,708                                                          
[[BANGTAN BOMB] 'Just one day' practice (Appeal ver.)](https://www.youtube.com/watch?v=zNJMa43UVs0) | 310,708        
[[BANGTAN BOMB] 방탄도령단 - 危險 (Appeal ver.)](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 237,019
:sparkles: [[BANGTAN BOMB] Just watching Jung Kook lip sync show](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 226,503                                         
[방탄소년단 'Beautiful' dance practice](https://www.youtube.com/watch?v=sm4FFFBgbmg) | 218,694
[방탄소년단 '호르몬전쟁' Dance practice](https://www.youtube.com/watch?v=JumcC5jFcQc) | 195,179                                
:sparkles: [[BANGTAN BOMB] Let's speak English!](https://www.youtube.com/watch?v=cDlSqljhHD0) | 188,966                                     
[[BANGTAN BOMB] 눈,코,입 (EYES, NOSE, LIPS) of BTS](https://www.youtube.com/watch?v=J8uOSITy1t0) | 186,293

<p> </p>

The iconic bangtan bombs were shown on the list: Jungkook's lip sync show and Let's speak english.


```python
vids_likes_2013 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2013]
top10_highest_likes_2013 = vids_likes_2013.nlargest(10, 'statistics.likeCount')
top10_highest_likes_2013[['snippet.title', 'statistics.likeCount']]
```


## 10 Most-Liked Videos of BANGTANTV in 2013

Video | Likes
:--- | ---: | :---
[방탄소년들의 졸업](https://www.youtube.com/watch?v=sctrgmZ_JNM) | 353,776
[방탄소년단 We Are Bulletproof Pt.2 dance practice](https://www.youtube.com/watch?v=bV9Svms-LYY) | 195,062
[방탄소년단 BTS Dance break Practice](https://www.youtube.com/watch?v=xJg_FvMe4hE) | 192,247                                                          
[방탄소년단 SBS 가요대전 performance practice](https://www.youtube.com/watch?v=j2rS6vXApF0) | 179,687        
:sparkles: [[BANGTAN BOMB] N.O (Trot ver.) by Jungkook and (Opera ver.) by BTS](https://www.youtube.com/watch?v=Qs2unC6IwBc) | 178,503
:sparkles: [Beautiful by 방탄소년단](https://www.youtube.com/watch?v=f9_sHgPVQgM) | 165,918                                         
[방탄소년단 '진격의 방탄 (Attack on BTS)' Dance Practice](https://www.youtube.com/watch?v=ncRNKuwOEc0) | 159,963
:sparkles: [Born Singer by 방탄소년단](https://www.youtube.com/watch?v=2XsP4I9ds4c) | 135,583                                
:sparkles: [[Episode] BTS Debut day 130613](https://www.youtube.com/watch?v=UPJX6QK6etg) | 120,669                                     
[학교의눈물 by 방탄소년단](https://www.youtube.com/watch?v=Sby_6W_I0dQ) | 114,031

<p> </p>

Just looking at this list makes me nostalgic, with BTS Debut day and Born Singer.

# DISLIKES

It's unavoidable so I have to talk about the dislikes as well. The video with the highest number of dislikes is still their GO GO dance practice. Since this video has gained a lot of views, it isn't really surprising for it to get the higest number of dislikes as well. Below, I will be showing the top 10 videos with the highest number of dislikes.

```python
videoIds['statistics.dislikeCount'] = videoIds['statistics.dislikeCount'].astype(float)
```


```python
videoIds.loc[videoIds['statistics.dislikeCount'].idxmax()]
```

```python
top10_highest_dislikes = videoIds.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes[['snippet.title', 'statistics.dislikeCount', 'snippet.publishedAt.year']]
```

## 10 Most-Disliked Videos of BANGTANTV

Video | Dislikes | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 22,906 | 2017
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 8,807 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=GEIU_7v40Dw) | 7,472 | 2017                                                          
:sparkles: [Rap Monster 'Do You' MV](https://www.youtube.com/watch?v=0XAxf8aFtL4) | 7,070 | 2015        
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 6,815 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 6,420 | 2016                                         
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=RbctNBlXBJc) | 5,104 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 5,067 | 2016                                
[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 4,507 | 2018                                     
[Official Trailer &#124; BTS: Burn The Stage](https://www.youtube.com/watch?v=xf-dywd3zx0) | 4,264 | 2018

<p> </p>

It's so frustrating that RM's 'Do You' MV is part of this list even though it isn't part of the top 10 highest viewed videos nor in the top 10 highest liked videos. I don't get how people have the courage to dislike this amazing piece by RM.

Below are the top 10 videos with the highest number of dislikes per year. Some of them are old news and predictable as they were also part of the highest number of views list.


```python
vids_dislikes_2018 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2018]
top10_highest_dislikes_2018 = vids_dislikes_2018.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2018[['snippet.title', 'statistics.dislikeCount']]
```

## 10 Most-Disliked Videos of BANGTANTV in 2018

Video | Dislikes
:--- | ---: | :---
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 8,807
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 6,815
[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 4,507                                                          
[Official Trailer &#124; BTS: Burn The Stage](https://www.youtube.com/watch?v=xf-dywd3zx0) | 4,264        
[BTS (방탄소년단) - Anpanman @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=lOf16ZQDDdE) | 2,889
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 2,038                                         
:sparkles: [[BANGTAN BOMB] j-hope & Jimin Dancing in Highlight Reel (Focus ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 2,038
[BTS (방탄소년단) - FAKE LOVE @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Hoz5OQjXEA8) | 1,632                                
[[BANGTAN BOMB] 'MIC Drop' Special Stage (BTS focus) @MAMA - BTS (방탄소년단)](https://www.youtube.com/watch?v=floMqK_yHf8) | 1,585                                     
[G.C.F in Saipan](https://www.youtube.com/watch?v=M1F1RxkXrDE) | 1,327


<p> </p>

```python
vids_dislikes_2017 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2017]
top10_highest_dislikes_2017 = vids_dislikes_2017.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2017[['snippet.title', 'statistics.dislikeCount']]
```


## 10 Most-Disliked Videos of BANGTANTV in 2017

Video | Dislikes
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 22,906
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=GEIU_7v40Dw) | 7,472
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=RbctNBlXBJc) | 5,104                                                         
[[CHOREOGRAPHY] BTS (방탄소년단) '봄날 (Spring Day)' Dance Practice](https://www.youtube.com/watch?v=_AlODdAInRY) | 3,126        
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 2,963
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 2,581                                         
[G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=XrTNLkqGrlc) | 2,206
[[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=u2XBh23upio) | 1,987                                
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=W5JB4XsjSXY) | 1,848                                    
[[BANGTAN BOMB] BTS 'MIC Drop' MV reaction - BTS (방탄소년단)](https://www.youtube.com/watch?v=HQsyxzOCuWA) | 1,713

<p> </p>


```python
vids_dislikes_2016 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2016]
top10_highest_dislikes_2016 = vids_dislikes_2016.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2016[['snippet.title', 'statistics.dislikeCount']]
```

## 10 Most-Disliked Videos of BANGTANTV in 2016

Video | Dislikes
:--- | ---: | :---
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 6,420
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 5,067
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 3,208                                                         
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 1,793       
[[BANGTAN BOMB] 'Coming of age ceremony' Dance cover by Jimin & Jung Kook - BTS (방탄소년단)](https://www.youtube.com/watch?v=D4oIpsRemPA) | 1,000
:sparkles: [[BANGTAN BOMB] Show Me Your BBA SAE!?!? - BTS (방탄소년단)](https://www.youtube.com/watch?v=ttSLLgU8F_I) | 855                                         
[[EPISODE] BTS (방탄소년단) '불타오르네 (FIRE)' MV Shooting](https://www.youtube.com/watch?v=DZalBQgECn4) | 762
[[CHOREOGRAPHY] BTS (방탄소년단) 정국이랑 지민이 ('Own it' choreography by Brian puspose) Dance practice](https://www.youtube.com/watch?v=HMprwPSFLyU) | 753                                
[[EPISODE] BTS (방탄소년단) 'Save Me' MV Shooting](https://www.youtube.com/watch?v=y_mEk99kDjI) | 693                                    
[[BANGTAN BOMB] BTS' Relay race @ 2016 추석특집 아육대 - BTS (방탄소년단)](https://www.youtube.com/watch?v=0gqOz1OO-88) | 683

<p> </p>

```python
vids_dislikes_2015 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2015]
top10_highest_dislikes_2015 = vids_dislikes_2015.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2015[['snippet.title', 'statistics.dislikeCount']]
```


## 10 Most-Disliked Videos of BANGTANTV in 2015

Video | Dislikes
:--- | ---: | :---
:sparkles: [Rap Monster 'Do You' MV](https://www.youtube.com/watch?v=0XAxf8aFtL4) | 7,070
[방탄소년단 'I NEED U' Dance Practice](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 3,033
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 2,701
[Rap Monster '농담' MV](https://www.youtube.com/watch?v=TfenCTabhDY) | 2,169     
[방탄소년단 'RUN' Dance practice](https://www.youtube.com/watch?v=9S3ZhJGv8JM) | 1,907
:sparkles: [안아줘 (Hug me) performed by V, j-hope](https://www.youtube.com/watch?v=tv_HQ-0upns) | 1,887                                         
:sparkles: [[BANGTAN BOMB] it's tricky is title! BTS, here we go! (by Run–D.M.C.)](https://www.youtube.com/watch?v=PSdgzdDMIeE) | 1,367
[방탄소년단 '쩔어' Dance Practice](https://www.youtube.com/watch?v=NnbIIXNPtPU) | 1,153                               
[[Episode] 방탄소년단(BTS) '쩔어' Concept photo & MV shooting](https://www.youtube.com/watch?v=xO2KP7aGRrw) | 787                                    
:sparkles: [[BANGTAN BOMB] UP DOWN UP UP DOWN (by EXID)](https://www.youtube.com/watch?v=5gEqOtODMH4) | 644

<p> </p>

```python
vids_dislikes_2014 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2014]
top10_highest_dislikes_2014 = vids_dislikes_2014.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2014[['snippet.title', 'statistics.dislikeCount']]
```

## 10 Most-Disliked Videos of BANGTANTV in 2014

Video | Dislikes
:--- | ---: | :---
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 2,760
[[BANGTAN BOMB] War of hormone in Halloween](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 2,132
[[BANGTAN BOMB] 'Just one day' practice (Appeal ver.)](https://www.youtube.com/watch?v=zNJMa43UVs0) | 1,591
[방탄소년단 'Beautiful' dance practice](https://www.youtube.com/watch?v=sm4FFFBgbmg) | 1,112    
[[BANGTAN BOMB] 방탄도령단 - 危險 (Appeal ver.)](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 949
[[BANGTAN BOMB] 눈,코,입 (EYES, NOSE, LIPS) of BTS](https://www.youtube.com/watch?v=J8uOSITy1t0) | 820                                        
:sparkles: [[BANGTAN BOMB] Someone like you (sung & produced by V)](https://www.youtube.com/watch?v=56jN9-cMEBU) | 777
[방탄소년단 '호르몬전쟁' Dance practice](https://www.youtube.com/watch?v=JumcC5jFcQc) | 730                               
:sparkles: [[BANGTAN BOMB] Just watching Jung Kook lip sync show](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 634                                    
[[Episode] '상남자(Boy In Luv)' MV shooting Sketch 	](https://www.youtube.com/watch?v=GQEunnh8MKE) | 616

<p> </p>

```python
vids_dislikes_2013 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2013]
top10_highest_dislikes_2013 = vids_dislikes_2013.nlargest(10, 'statistics.dislikeCount')
top10_highest_dislikes_2013[['snippet.title', 'statistics.dislikeCount']]
```

## 10 Most-Disliked Videos of BANGTANTV in 2013

Video | Dislikes
:--- | ---: | :---
[방탄소년들의](https://www.youtube.com/watch?v=JumcC5jFcQc) | 1,482 
:sparkles: [Beautiful by 방탄소년단](https://www.youtube.com/watch?v=vJwHIpEogEY) | 1,361
[방탄소년단 We Are Bulletproof Pt.2 dance practice](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 934
[방탄소년단 SBS 가요대전 performance practice](https://www.youtube.com/watch?v=zNJMa43UVs0) | 683
[방탄소년단 BTS Dance break Practice](https://www.youtube.com/watch?v=sm4FFFBgbmg) | 579    
[방탄소년단 '진격의 방탄 (Attack on BTS)' Dance Practice](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 485
[학교의눈물 by 방탄소년단](https://www.youtube.com/watch?v=J8uOSITy1t0) | 450                                        
:sparkles: [[BANGTAN BOMB] N.O (Trot ver.) by Jungkook and (Opera ver.) by BTS](https://www.youtube.com/watch?v=56jN9-cMEBU) | 396                              
:sparkles: [[Episode] BTS Debut day 130613](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 281                                    
[[BANGTAN BOMB] BTS style 'Hush' of Miss A](https://www.youtube.com/watch?v=GQEunnh8MKE) | 269

<p> </p>

# COMMENTS

Guess which video is the most commented? Yep, it's still their Go Go Dance Practice. Nothing much to see here so you can move on to the top 10 videos with the highest number of comments.

```python
videoIds['statistics.commentCount'] = videoIds['statistics.commentCount'].astype(float)
```


```python
videoIds.loc[videoIds['statistics.commentCount'].idxmax()]
```


```python
top10_highest_comments = videoIds.nlargest(10, 'statistics.commentCount')
top10_highest_comments[['snippet.title', 'statistics.commentCount','snippet.publishedAt.year']]
```


## 10 Most-Commented Videos of BANGTANTV

Video | Comments | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=JumcC5jFcQc) | 117,084 | 2017
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=vJwHIpEogEY) | 108,490 | 2017
:sparkles: [G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 82,462 | 2017
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=zNJMa43UVs0) | 78,217 | 2018
:sparkles: [G.C.F in Saipan](https://www.youtube.com/watch?v=sm4FFFBgbmg) | 76,330 | 2018    
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 75848 | 2018
:sparkles: [G.C.F in Osaka](https://www.youtube.com/watch?v=J8uOSITy1t0) | 69,322 | 2018                                        
:sparkles: [G.C.F in USA](https://www.youtube.com/watch?v=56jN9-cMEBU) | 68,913 | 2018                              
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 57,784 | 2016                                    
[We don't talk anymore by JK](https://www.youtube.com/watch?v=GQEunnh8MKE) | 54,657 | 2017

<p> </p>

JK received a lot of love in this list, with 6 of the videos coming from him. His G.C.F. videos are really the talk of the town because of his amazing (and hidden) talent in video editing so these videos deserve to be in the top 10.

Below are the lists of top 10 videos with the highest number of comments per year.


```python
vids_comments_2018 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2018]
top10_highest_comments_2018 = vids_comments_2018.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2018[['snippet.title', 'statistics.commentCount']]
```


## 10 Most-Commented Videos of BANGTANTV in 2018

Video | Comments
:--- | ---: | :---
[I’d do it all &#124; BTS: Burn the Stage Ep1](https://www.youtube.com/watch?v=j6zWwAoEi_w) | 78,217 
:sparkles: [G.C.F in Saipan](https://www.youtube.com/watch?v=M1F1RxkXrDE) | 76,330
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 75,848
:sparkles: [G.C.F in Osaka](https://www.youtube.com/watch?v=f3lEi_bp6f4) | 69,322
:sparkles: [G.C.F in USA](https://www.youtube.com/watch?v=9Lb6ta2bPu4) | 68,913    
[BTS (방탄소년단) '방탄회식' #2018BTSFESTA](https://www.youtube.com/watch?v=K4Melso7MPU) | 50,604
:sparkles: [[BANGTAN BOMB] V&Jungkook Singing at standby time - BTS (방탄소년단)](https://www.youtube.com/watch?v=3-FXW0CW_8o) | 47,305                                        
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 46,072                              
[BTS (방탄소년단) - Airplane pt.2 @BTS COMEBACK SHOW](https://www.youtube.com/watch?v=Fj3euSYAtnc) | 45,718                                    
[[BANGTAN BOMB] JIMIN's Piano solo showcase - BTS (방탄소년단)](https://www.youtube.com/watch?v=zVeN6bABNhk) | 37,399


<p> </p>

```python
vids_comments_2017 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2017]
top10_highest_comments_2017 = vids_comments_2017.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2017[['snippet.title', 'statistics.commentCount']]
```

## 10 Most-Commented Videos of BANGTANTV in 2017

Video | Comments
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 117,084 
[[FESTA 2017] BTS (방탄소년단) Jimin, JK 'We don't talk anymore'](https://www.youtube.com/watch?v=RbctNBlXBJc) | 108,490
:sparkles: [G.C.F in Tokyo (정국&지민)](https://www.youtube.com/watch?v=XrTNLkqGrlc) | 82,462
[We don't talk anymore by JK](https://www.youtube.com/watch?v=C4wMGXpD3PY) | 54,657
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=GEIU_7v40Dw) | 52,411    
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 43,076
:sparkles: [[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=u2XBh23upio) | 42,993                                        
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=W5JB4XsjSXY) | 39,839                              
[[FESTA 2017] BTS (방탄소년단) 꿀 FM 06.13 Happy BTS birthday!](https://www.youtube.com/watch?v=cWA6f7g7NUQ) | 37,314                                    
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 35,836


<p> </p>

```python
vids_comments_2016 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2016]
top10_highest_comments_2016 = vids_comments_2016.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2016[['snippet.title', 'statistics.commentCount']]
```


## 10 Most-Commented Videos of BANGTANTV in 2016

Video | Comments
:--- | ---: | :---
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 57,784
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 43,633
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 32,099
[[CHOREOGRAPHY] BTS (방탄소년단) 정국이랑 지민이 ('Own it' choreography by Brian puspose) Dance practice](https://www.youtube.com/watch?v=HMprwPSFLyU) | 25,873
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 25,867    
:sparkles: [[BANGTAN BOMB] V's Dream came true - 'His Cypher pt.3 Solo Stage' - BTS (방탄소년단)](https://www.youtube.com/watch?v=GQ0XGbHjKRE) | 18,664
:sparkles: [[BANGTAN BOMB] Show Me Your BBA SAE!?!? - BTS (방탄소년단)](https://www.youtube.com/watch?v=ttSLLgU8F_I) | 16,009                                        
[[BANGTAN BOMB] 'Coming of age ceremony' Dance cover by Jimin & Jung Kook - BTS (방탄소년단)](https://www.youtube.com/watch?v=D4oIpsRemPA) | 15,921                              
:sparkles: [[BANGTAN BOMB] Happy new year 2017! - BTS (방탄소년단)](https://www.youtube.com/watch?v=ALMWtt8cGm8) | 13,997                                   
[[FESTA 2016] BTS (방탄소년단) 꿀 FM 06.13 3rd BTS birthday](https://www.youtube.com/watch?v=cWA6f7g7NUQ) | 13,031


<p> </p>

```python
vids_comments_2015 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2015]
top10_highest_comments_2015 = vids_comments_2015.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2015[['snippet.title', 'statistics.commentCount']]
```


## 10 Most-Commented Videos of BANGTANTV in 2015

Video | Comments
:--- | ---: | :---
:sparkles: [Rap Monster 'Do You' MV](https://www.youtube.com/watch?v=0XAxf8aFtL4) | 40,602
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 34,091
[방탄소년단 'RUN' Dance practice](https://www.youtube.com/watch?v=9S3ZhJGv8JM) | 27,954
:sparkles: [안아줘 (Hug me) performed by V, j-hope](https://www.youtube.com/watch?v=tv_HQ-0upns) | 20,987
[방탄소년단 'I NEED U' Dance Practice](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 16,743   
[Rap Monster '농담' MV](https://www.youtube.com/watch?v=TfenCTabhDY) | 16,278
[[BANGTAN BOMB] 'RUN' christmas ver.](https://www.youtube.com/watch?v=sjwrE0I-cXM) | 14,958                                        
[Lost Stars by Jung Kook](https://www.youtube.com/watch?v=VLzRQCIZrmE) | 11,844                             
:sparkles: [[BANGTAN BOMB] it's tricky is title! BTS, here we go! (by Run–D.M.C.)](https://www.youtube.com/watch?v=PSdgzdDMIeE) | 11,587
:sparkles: [[BANGTAN BOMB] Jimin: I got yes jam](https://www.youtube.com/watch?v=e4S9czAIF40) | 9,981


<p> </p>

```python
vids_comments_2014 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2014]
top10_highest_comments_2014 = vids_comments_2014.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2014[['snippet.title', 'statistics.commentCount']]
```

## 10 Most-Commented Videos of BANGTANTV in 2014

Video | Comments
:--- | ---: | :---
[[BANGTAN BOMB] War of hormone in Halloween](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 26,000
[[BANGTAN BOMB] 'Just one day' practice (Appeal ver.)](https://www.youtube.com/watch?v=zNJMa43UVs0) | 19,503
:sparkles: [[BANGTAN BOMB] Someone like you (sung & produced by V)](https://www.youtube.com/watch?v=56jN9-cMEBU) | 18,506
:sparkles: [[BANGTAN BOMB] Let's speak English!](https://www.youtube.com/watch?v=cDlSqljhHD0) | 15,774
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 15,293  
[[BANGTAN BOMB] 방탄도령단 - 危險 (Appeal ver.)](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 11,749
:sparkles: [[BANGTAN BOMB] Just watching Jung Kook lip sync show](https://www.youtube.com/watch?v=0-XR2iLEUQY) | 11,570                                      
:sparkles: [[BANGTAN BOMB] Runway in the night](https://www.youtube.com/watch?v=f1zVUalWabo) | 8,190                           
[[BANGTAN BOMB] 눈,코,입 (EYES, NOSE, LIPS) of BTS](https://www.youtube.com/watch?v=J8uOSITy1t0) | 7,817
[[BANGTAN BOMB] medley show time! (performed by BTS)](https://www.youtube.com/watch?v=heTHSxEJIew) | 7,401

<p> </p>

```python
vids_comments_2013 = videoIds.loc[videoIds['snippet.publishedAt.year'] == 2013]
top10_highest_comments_2013 = vids_comments_2013.nlargest(10, 'statistics.commentCount')
top10_highest_comments_2013[['snippet.title', 'statistics.commentCount']]
```


## 10 Most-Commented Videos of BANGTANTV in 2013

Video | Comments
:--- | ---: | :---
[방탄소년들의 졸업](https://www.youtube.com/watch?v=sctrgmZ_JNM) | 23,233
:sparkles: [Beautiful by 방탄소년단](https://www.youtube.com/watch?v=f9_sHgPVQgM) | 11,841
[방탄소년단 We Are Bulletproof Pt.2 dance practice](https://www.youtube.com/watch?v=bV9Svms-LYY) | 9531
:sparkles: [[BANGTAN BOMB] N.O (Trot ver.) by Jungkook and (Opera ver.) by BTS](https://www.youtube.com/watch?v=Qs2unC6IwBc) | 8,599
[방탄소년단 SBS 가요대전 performance practice](https://www.youtube.com/watch?v=j2rS6vXApF0) | 7,319
[학교의눈물 by 방탄소년단](https://www.youtube.com/watch?v=Sby_6W_I0dQ) | 5,893
:sparkles: [Born Singer by 방탄소년단](https://www.youtube.com/watch?v=2XsP4I9ds4c) | 5,420                                      
:sparkles: [[Episode] BTS Debut day 130613](https://www.youtube.com/watch?v=UPJX6QK6etg) | 5,403                           
:sparkles: [흔한 연습생의 Harlem shake.avi](https://www.youtube.com/watch?v=uLEf36edQws) | 5,377
[방탄소년단 BTS Dance break Practice](https://www.youtube.com/watch?v=xJg_FvMe4hE) | 5,337

<p> </p>

There were a lot of videos in this list that weren't part of the top 10 videos with the highest number of views and likes. They were mostly bangtan bombs of them goofing around so I think if you're looking for something fun and popular, I think these lists would come in handy.

# Number of Views By Year

I wanted to know how their number of views fared along the years so I made this scatter plot to check if there are any interesting results.


```python
fig, ax = plt.subplots(figsize=(15,10))
time = videoIds['snippet.publishedAt']
views = videoIds['statistics.viewCount']
fig.autofmt_xdate()
ax.scatter(time.values, views, alpha=0.4, s=100)
plt.savefig('views-per-time', dpi=300)
plt.show()
```


![Number of views in BANGTANTV by year]({{ site.url }}/assets/views-per-time.png)


...except, I can't find anything. I also tried to remove the outlier (their Go Go dance practice) to get better results but still there aren't.


```python
#pd.set_option('display.max_rows', None)
videoIds_wo_outlier = videoIds.copy()
videoIds_wo_outlier = videoIds_wo_outlier.drop(videoIds_wo_outlier.index[87])
#videoIds_wo_outlier[videoIds_wo_outlier['snippet.title'] != '[BANGTAN BOMB] \'고민보다 GO (GOGO)\' Dance Practice (Halloween ver.) - BTS (방탄소년단)']
videoIds_wo_outlier.shape
```


```python
fig, ax = plt.subplots(figsize=(15,10))
time = videoIds_wo_outlier['snippet.publishedAt']
views = videoIds_wo_outlier['statistics.viewCount']
fig.autofmt_xdate()
ax.scatter(time.values, views, alpha=0.4, s=100)
comeback = [pd.to_datetime('2013-06-13'), pd.to_datetime('2013-09-11'), pd.to_datetime('2014-02-12'), pd.to_datetime('2014-05-14'), pd.to_datetime('2014-08-19'), pd.to_datetime('2015-04-29'), pd.to_datetime('2015-11-30'), pd.to_datetime('2016-05-02'), pd.to_datetime('2016-10-10'), pd.to_datetime('2017-02-13'), pd.to_datetime('2017-09-18'), pd.to_datetime('2018-05-18')]
for xc in comeback:
    ax.axvline(x=xc, color='red', linestyle='--', lw=1, alpha=0.7)
plt.savefig('views-per-time-comeback', dpi=300)
plt.show()
```

I also plotted this with markers of their comeback which shows that their is a spike of views in their videos right after their comebacks. But I noticed that beginning from their 'You Never Walk Alone' comeback, the dots became less dense which means that there is a notable amount of increase of views in their videos! However, this was expected as they got a huge number of following after the events of the BBMAs in early 2017. Also as expected, the dots at the top of the chart are mostly dance practices and performance videos.

![Number of views in BANGTANTV by year]({{ site.url }}/assets/views-per-time-comeback.png)


# Number of Likes By Year

It's also important to see how the likes in BANGTANTV grew over the years.

```python
fig, ax = plt.subplots(figsize=(15,10))
time = videoIds['snippet.publishedAt']
likes = videoIds['statistics.likeCount']
fig.autofmt_xdate()
ax.scatter(time.values, likes, alpha=0.4, s=100)
comeback = [pd.to_datetime('2013-06-13'), pd.to_datetime('2013-09-11'), pd.to_datetime('2014-02-12'), pd.to_datetime('2014-05-14'), pd.to_datetime('2014-08-19'), pd.to_datetime('2015-04-29'), pd.to_datetime('2015-11-30'), pd.to_datetime('2016-05-02'), pd.to_datetime('2016-10-10'), pd.to_datetime('2017-02-13'), pd.to_datetime('2017-09-18'), pd.to_datetime('2018-05-18')]
for xc in comeback:
    ax.axvline(x=xc, color='red', linestyle='--', lw=1, alpha=0.7)
    
#for i, txt in enumerate(videoIds['snippet.title']):
 #   if i != 87:
  #      ax.annotate(txt, ((videoIds['snippet.publishedAt'].values)[i],videoIds['statistics.likeCount'][i]))
plt.savefig('likes-per-time-comeback', dpi=300)
plt.show()
```

I plotted another scatter plot to see the patterns in terms of YouTube likes. It's apparent that there's a slow build up since HYYH Pt. 2 until YOU NEVER WALK ALONE, where the number of likes have grown much faster.

![Number of likes in BANGTANTV by year]({{ site.url }}/assets/likes-per-time-comeback.png)


# Number of Comments By Year


```python
fig, ax = plt.subplots(figsize=(15,10))
time = videoIds['snippet.publishedAt']
comments = videoIds['statistics.commentCount']
fig.autofmt_xdate()
ax.scatter(time.values, comments, alpha=0.4, s=100)
comeback = [pd.to_datetime('2013-06-13'), pd.to_datetime('2013-09-11'), pd.to_datetime('2014-02-12'), pd.to_datetime('2014-05-14'), pd.to_datetime('2014-08-19'), pd.to_datetime('2015-04-29'), pd.to_datetime('2015-11-30'), pd.to_datetime('2016-05-02'), pd.to_datetime('2016-10-10'), pd.to_datetime('2017-02-13'), pd.to_datetime('2017-09-18'), pd.to_datetime('2018-05-18')]
for xc in comeback:
    ax.axvline(x=xc, color='red', linestyle='--', lw=1, alpha=0.7)
plt.savefig('comments-per-time-comeback', dpi=300)
plt.show()
```

Similar to the chart above, this scatterplot also shows how there was a drastic increase in the number of comments beginning from YOU NEVER WALK ALONE. It's amazing to see how BTS have fared through the years using their YouTube data. 

![Number of likes in BANGTANTV by year]({{ site.url }}/assets/comments-per-time-comeback.png)


# Relationship between Wiews and Likes

I was also curious how a scatterplot with their number of views and likes would look like so I plotted them. I expected a linear pattern and I was right.


```python
fig, ax = plt.subplots(figsize=(15,10))
likes = videoIds['statistics.likeCount']
views = videoIds['statistics.viewCount']
fig.autofmt_xdate()
ax.scatter(views, likes, alpha=0.4, s=100)
plt.savefig('rel-view-likes', dpi=300)
plt.show()
```


![Relationship between likes and views]({{ site.url }}/assets/rel-view-likes.png)


There are a few notable points, though. JK's G.C.F. videos are placed higher in the chart, even though they were just recently posted and does not have a lot of views. Their MV Shooting of Danger was also slightly off because it has a lot of views but lesser number of likes.

# Relationship between Views and Comments

To check the relationship between views and comments, I plotted a scatter plot as well. 


```python
fig, ax = plt.subplots(figsize=(15,10))
comments = videoIds['statistics.commentCount']
views = videoIds['statistics.viewCount']
fig.autofmt_xdate()
ax.scatter(views, comments, alpha=0.4, s=100)
plt.savefig('rel-view-comments', dpi=300)
plt.show()
```


![Relationship between comments and views]({{ site.url }}/assets/rel-view-comments.png)


BTS' choreography and dance practice videos certainly gained a lot of views but lesser comments. Meanwhile, Jimin and JK's cover of 'We don't talk anymore' and JK's G.C.F. tell the opposite. Also I want to give the video 'V & Jungkook Singing at standby time' a huge shoutout for being placed high up even with lesser number of views compared to other videos. (Actually, I just wanted to find an excuse to watch this video again so here it is.)


<a href="https://www.youtube.com/watch?v=3-FXW0CW_8o" target="_blank"><img src="https://i.ytimg.com/vi/3-FXW0CW_8o/maxresdefault.jpg" 
alt="V & Jungkook Singing at standby time"/></a>


BANGTANTV is home of hundreds of videos; some of them are tagged as 'Bangtan Bombs', 'Choreography', 'Episode', and 'Dance Practice'. I took the time to arrange my data and group them accordingly. Here are the statistics for each type of video.

# BANGTAN BOMBS

There are 437 Bangtan Bombs in BANGTANTV. That composes 51% of all videos in the YouTube channel. The top 10 videos with the highest number of views, likes, and comments are shown below.


```python
bangtan_bombs = videoIds[videoIds['snippet.title'].str.contains('\[BANGTAN BOMB\]|\[Bangtan Bomb\]')]
len(bangtan_bombs)
```


```python
top10_highest_views_bombs = bangtan_bombs.nlargest(10, 'statistics.viewCount')
top10_highest_views_bombs[['snippet.title', 'statistics.viewCount', 'snippet.publishedAt.year']]
```


## 10 Most-Viewed Bangtan Bombs

Video | Views | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 63,641,290 | 2017
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 24,491,873 | 2016
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 23,511,936 | 2015
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 18,915,957 | 2016
[[BANGTAN BOMB] 'Just one day' practice (Appeal ver.)](https://www.youtube.com/watch?v=zNJMa43UVs0) | 17,306,745 | 2014
[[BANGTAN BOMB] War of hormone in Halloween](https://www.youtube.com/watch?v=ZxEly3yz-1g) | 14,960,302 | 2014
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 12,131,897 | 2017
:sparkles: [[BANGTAN BOMB] it's tricky is title! BTS, here we go! (by Run–D.M.C.)](https://www.youtube.com/watch?v=PSdgzdDMIeE) | 11,931,523 | 2015
[[BANGTAN BOMB] 방탄도령단 - 危險 (Appeal ver.)](https://www.youtube.com/watch?v=rvj2O-O6JGQ) | 11,620,014 | 2014
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 11,019,375 | 2017

<p> </p>


```python
top10_highest_likes_bombs = bangtan_bombs.nlargest(10, 'statistics.likeCount')
top10_highest_likes_bombs[['snippet.title', 'statistics.likeCount', 'snippet.publishedAt.year']]
```


## 10 Most-Liked Bangtan Bombs

Video | Likes | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 1,538,722 | 2017
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 668,833 | 2016
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 591,858 | 2017
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 591,781 | 2017
[[BANGTAN BOMB] BTS 'MIC Drop' MV reaction - BTS (방탄소년단)](https://www.youtube.com/watch?v=HQsyxzOCuWA) | 529,320 | 2017
:sparkles: [[BANGTAN BOMB] j-hope & Jimin Dancing in Highlight Reel (Focus ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 523,269 | 2018
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 495,325 | 2015
[[BANGTAN BOMB] 'MIC Drop' Special Stage (BTS focus) @MAMA - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 476,864 | 2018
:sparkles: [[BANGTAN BOMB] V&Jungkook Singing at standby time - BTS (방탄소년단)](https://www.youtube.com/watch?v=3-FXW0CW_8o) | 448,712 | 2018
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 446,302 | 2016


<p> </p>

```python
top10_highest_comments_bombs = bangtan_bombs.nlargest(10, 'statistics.commentCount')
top10_highest_comments_bombs[['snippet.title', 'statistics.commentCount', 'snippet.publishedAt.year']]
```


## 10 Most-Commented Bangtan Bombs

Video | Comments | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 117,084 | 2017
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 57,784 | 2016
:sparkles: [[BANGTAN BOMB] V&Jungkook Singing at standby time - BTS (방탄소년단)](https://www.youtube.com/watch?v=3-FXW0CW_8o) | 47,305 | 2018
[[BANGTAN BOMB] BTS 'DNA' MV REAL reaction @6:00PM (170918) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Cx6ZYcZnoW4) | 43,076 | 2017
[[BANGTAN BOMB] 613 BTS HOME PARTY Practice - Unit stage '삼줴이(3J)' - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 39,839 | 2017
[[BANGTAN BOMB] JIMIN's Piano solo showcase - BTS (방탄소년단)](https://www.youtube.com/watch?v=zVeN6bABNhk) | 37,399 | 2018
:sparkles: [[BANGTAN BOMB] j-hope & Jimin Dancing in Highlight Reel (Focus ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 36,624 | 2018
[[BANGTAN BOMB] BTS 'MIC Drop' MV reaction - BTS (방탄소년단)](https://www.youtube.com/watch?v=HQsyxzOCuWA) | 34,586 | 2017
[[BANGTAN BOMB] '호르몬전쟁' dance performance (Real WAR ver.)](https://www.youtube.com/watch?v=70SMjxn4FBA) | 34,091 | 2015
:sparkles: [[BANGTAN BOMB] BTS PROM PARTY : UNIT STAGE BEHIND - 땡 - BTS (방탄소년단)](https://www.youtube.com/watch?v=h2nKAqf6bvY) | 33,842 | 2018

<p> </p>


# EPISODE

There are 61 episodes in BANGTANTV. Usually, they show exclusive behind the scenes content on BTS important events. These videos are usually long, with the recent ones ranging from 20-30 minutes each. Below are the top 10 videos tagged as episodes.


```python
episode = videoIds[videoIds['snippet.title'].str.contains('\[Episode\]|\[EPISODE\]')]
len(episode)
```

```python
top10_highest_views_eps = episode.nlargest(10, 'statistics.viewCount')
top10_highest_views_eps[['snippet.title', 'statistics.viewCount', 'snippet.publishedAt.year']]
```


## 10 Most-Viewed Episodes

Video | Views | Year
:--- | ---: | :---
[[EPISODE] BTS (방탄소년단) 'DNA' MV Shooting](https://www.youtube.com/watch?v=rgRDwhO983s) | 6,711,481 | 2017
:sparkles: [[EPISODE] BTS (방탄소년단) @ Billboard Music Awards 2017](https://www.youtube.com/watch?v=FBLx-6l24-Q) | 6,311,151 | 2017
[[EPISODE] BTS (방탄소년단) '불타오르네 (FIRE)' MV Shooting](https://www.youtube.com/watch?v=FBLx-6l24-Q) | 4,747,979 | 2016
[[Episode] 방탄소년단(BTS) '쩔어' Concept photo & MV shooting](https://www.youtube.com/watch?v=xO2KP7aGRrw) | 4,746,911 | 2015
[[EPISODE] BTS (방탄소년단) 'Save Me' MV Shooting](https://www.youtube.com/watch?v=y_mEk99kDjI) | 4,727,814 | 2016
[[EPISODE] BTS (방탄소년단) 'MIC Drop' MV Shooting](https://www.youtube.com/watch?v=c5_LROaHGtw) | 4,605,153 | 2017
[[Episode] '상남자(Boy In Luv)' MV shooting Sketch](https://www.youtube.com/watch?v=GQEunnh8MKE) | 3,946,962 | 2014
[[Episode] 방탄소년단 'I NEED U' MV shooting](https://www.youtube.com/watch?v=I_QObBbAYNQ) | 3,737,658 | 2015
[[EPISODE] BTS (방탄소년단) 'FAKE LOVE' MV Shooting](https://www.youtube.com/watch?v=ZaOvpvw1NwA) | 3,496,272 | 2018
:sparkles: [[EPISODE] BTS (방탄소년단) @ AMAs 2017](https://www.youtube.com/watch?v=OMjMmULhl_M) | 2,962,220 | 2017

<p> </p>

```python
top10_highest_likes_eps = episode.nlargest(10, 'statistics.likeCount')
top10_highest_likes_eps[['snippet.title', 'statistics.likeCount', 'snippet.publishedAt.year']]
```

## 10 Most-Liked Episodes

Video | Likes | Year
:--- | ---: | :---
[[EPISODE] BTS (방탄소년단) 'FAKE LOVE' MV Shooting](https://www.youtube.com/watch?v=ZaOvpvw1NwA) | 490,525 | 2018
[[EPISODE] BTS (방탄소년단) 'Euphoria : Theme of LOVE YOURSELF 起 Wonder' Shooting](https://www.youtube.com/watch?v=kDKnN42BOiI) | 470,270 | 2018
[[EPISODE] BTS (방탄소년단) LOVE YOURSELF 轉 'Tear' Jacket shooting sketch](https://www.youtube.com/watch?v=YWM1fCHbp-Q) | 423,222 | 2018
[[EPISODE] BTS (방탄소년단) 'DNA' MV Shooting](https://www.youtube.com/watch?v=rgRDwhO983s) | 401,021 | 2017
[[EPISODE] BTS (방탄소년단) 'MIC Drop' MV Shooting](https://www.youtube.com/watch?v=c5_LROaHGtw) | 373,802 | 2017
:sparkles: [[EPISODE] j-hope 1st mixtape MV Shooting #1](https://www.youtube.com/watch?v=-viInMgMD3o) | 326,114 | 2018
:sparkles: [[EPISODE] BTS (방탄소년단) @ Billboard Music Awards 2017](https://www.youtube.com/watch?v=FBLx-6l24-Q) | 293,530 | 2017
:sparkles: [[EPISODE] BTS (방탄소년단) @ AMAs 2017](https://www.youtube.com/watch?v=OMjMmULhl_M) | 290,924 | 2017
:sparkles: [[EPISODE] j-hope 1st mixtape MV Shooting #2](https://www.youtube.com/watch?v=Ip7eVuFxiEE) | 281,594 | 2018
[[EPISODE] BTS (방탄소년단) ‘Highlight Reel’ sketch](https://www.youtube.com/watch?v=-uy9KdBPpCg) | 247,887 | 2017

<p> </p>

```python
top10_highest_comments_eps = episode.nlargest(10, 'statistics.commentCount')
top10_highest_comments_eps[['snippet.title', 'statistics.commentCount', 'snippet.publishedAt.year']]
```

## 10 Most-Commented Episodes

Video | Comments | Year
:--- | ---: | :---
:sparkles: [[EPISODE] BTS (방탄소년단) @ AMAs 2017](https://www.youtube.com/watch?v=OMjMmULhl_M) | 20,421 | 2017
[[EPISODE] BTS (방탄소년단) 'FAKE LOVE' MV Shooting](https://www.youtube.com/watch?v=ZaOvpvw1NwA) | 20,137 | 2018
:sparkles: [[EPISODE] j-hope 1st mixtape MV Shooting #2](https://www.youtube.com/watch?v=Ip7eVuFxiEE) | 20,095 | 2018
[[EPISODE] BTS (방탄소년단) 'Euphoria : Theme of LOVE YOURSELF 起 Wonder' Shooting](https://www.youtube.com/watch?v=kDKnN42BOiI) | 18232 | 2018
:sparkles: [[EPISODE] j-hope 1st mixtape MV Shooting #1](https://www.youtube.com/watch?v=-viInMgMD3o) | 17,121 | 2018
:sparkles: [[EPISODE] BTS (방탄소년단) @ Billboard Music Awards 2017](https://www.youtube.com/watch?v=FBLx-6l24-Q) | 16,525 | 2017
[[EPISODE] BTS (방탄소년단) 'MIC Drop' MV Shooting](https://www.youtube.com/watch?v=c5_LROaHGtw) | 16,198 | 2017
[[EPISODE] BTS (방탄소년단) LOVE YOURSELF 轉 'Tear' Jacket shooting sketch](https://www.youtube.com/watch?v=YWM1fCHbp-Q) | 15,999 | 2018
[[EPISODE] BTS @2017 SBS 가요대전](https://www.youtube.com/watch?v=R-ceLUo4fgs) | 13,344 | 2018
[[EPISODE] BTS @2017 MMA](https://www.youtube.com/watch?v=SjFQifUtOIA) | 12,248 | 2018

<p> </p>

# Dance Practice and Choreography

There are a total of 29 dance practice videos in BANGTANTV. From the previous results, we get the idea that dance practice videos usually chart higher in terms of number of views and likes. But listed below are the top 10 dance practice videos.


```python
dance_practice = videoIds[videoIds['snippet.title'].str.contains('Dance Practice|Dance practice|dance practice|\[CHOREOGRAPHY\]|\[Choreography\]')]
len(dance_practice)
```

```python
top10_highest_views_prac = dance_practice.nlargest(10, 'statistics.viewCount')
top10_highest_views_prac[['snippet.title', 'statistics.viewCount', 'snippet.publishedAt.year']]
```

## 10 Most-Viewed Dance Practice/Choreography Videos

Video | Views | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 63,641,290 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 37,046,200 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 32,679,447 | 2016
[방탄소년단 'I NEED U' Dance Practice](https://www.youtube.com/watch?v=hvUZb9NT7EY) | 29,434,845 | 2015
[방탄소년단 'Danger' dance practice](https://www.youtube.com/watch?v=vJwHIpEogEY) | 28,343,359 | 2014
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 25,950,392 | 2017
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 24,491,873 | 2016
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 18,915,957 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 18,396,812 | 2018
[방탄소년단 'RUN' Dance practice](https://www.youtube.com/watch?v=9S3ZhJGv8JM) | 17,636,564 | 2015


<p> </p>

```python
top10_highest_likes_prac = dance_practice.nlargest(10, 'statistics.likeCount')
top10_highest_likes_prac[['snippet.title', 'statistics.likeCount', 'snippet.publishedAt.year']]
```


## 10 Most-Liked Dance Practice/Choreography Videos

Video | Likes | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Fl54gG0B8I0) | 1,538,722 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 1,257,967 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 921,266 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 883,767 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 795,207 | 2016
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 668,833 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) '불타오르네 (FIRE)' Dance Practice](https://www.youtube.com/watch?v=sWuYspuN6U8) | 567,388 | 2016
:sparkles: [[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=u2XBh23upio) | 565,300 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) '봄날 (Spring Day)' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 561,624 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 539,318 | 2017

<p> </p>


```python
top10_highest_comments_prac = dance_practice.nlargest(10, 'statistics.commentCount')
top10_highest_comments_prac[['snippet.title', 'statistics.commentCount', 'snippet.publishedAt.year']]
```

## 10 Most-Commented Dance Practice/Choreography Videos

Video | Comments | Year
:--- | ---: | :---
[[BANGTAN BOMB] '고민보다 GO (GOGO)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 117,084 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'FAKE LOVE' Dance Practice](https://www.youtube.com/watch?v=nQySbNGu4g0) | 75,848 | 2018
[[BANGTAN BOMB] '21세기 소녀 (21st Century Girl)' Dance Practice (Halloween ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=6tUumjx2BWw) | 57,784 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) 'DNA' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 52,411 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'Golden Disk Awards 2018' Dance Practice #2018BTSFESTA](https://www.youtube.com/watch?v=6tJP3Y0QhV4) | 46,072 | 2018
[[CHOREOGRAPHY] BTS (방탄소년단) '피 땀 눈물 (Blood Sweat & Tears)' Dance Practice](https://www.youtube.com/watch?v=v8z1TtlY1no) | 43,633 | 2016
:sparkles: [[CHOREOGRAPHY] BTS (방탄소년단) '좋아요 Part 2' Dance Practice](https://www.youtube.com/watch?v=u2XBh23upio) | 42,993 | 2017
[[CHOREOGRAPHY] BTS (방탄소년단) 'Not Today' Dance Practice](https://www.youtube.com/watch?v=_PwYjNh1bww) | 35,836 | 2017
:sparkles: [[BANGTAN BOMB] '뱁새' Dance Practice (흥 ver.) - BTS (방탄소년단)](https://www.youtube.com/watch?v=V1i_x2_TGE0) | 32,099 | 2016
[[CHOREOGRAPHY] BTS (방탄소년단) '봄날 (Spring Day)' Dance Practice](https://www.youtube.com/watch?v=Zq89pRZqhk0) | 29,131 | 2017

<p> </p>

That's it for my analysis on BANGTANTV. It was quite a long read but if you have comments, questions, suggestions, or just anything you want to say if you have found a gem through this post, tweet me!

{% if page.comments %}
<div id="disqus_thread"></div>
<script>

/**
*  RECOMMENDED CONFIGURATION VARIABLES: EDIT AND UNCOMMENT THE SECTION BELOW TO INSERT DYNAMIC VALUES FROM YOUR PLATFORM OR CMS.
*  LEARN WHY DEFINING THESE VARIABLES IS IMPORTANT: https://disqus.com/admin/universalcode/#configuration-variables*/
/*
var disqus_config = function () {
this.page.url = PAGE_URL;  // Replace PAGE_URL with your page's canonical URL variable
this.page.identifier = PAGE_IDENTIFIER; // Replace PAGE_IDENTIFIER with your page's unique identifier variable
};
*/
(function() { // DON'T EDIT BELOW THIS LINE
var d = document, s = d.createElement('script');
s.src = 'https://binkymilk-github-io.disqus.com/embed.js';
s.setAttribute('data-timestamp', +new Date());
(d.head || d.body).appendChild(s);
})();
</script>
<noscript>Please enable JavaScript to view the <a href="https://disqus.com/?ref_noscript">comments powered by Disqus.</a></noscript>
                            
{% endif %}

