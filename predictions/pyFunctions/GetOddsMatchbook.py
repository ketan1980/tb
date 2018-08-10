import requests
import simplejson as sjson
import pandas as pd
import datetime
import time



def find_in_obj(obj, condition, path=None):
    #results in path in dictionary
    if path is None:
        path = []
    # In case this is a list
    if isinstance(obj, list):
        for index, value in enumerate(obj):
            new_path = list(path)
            new_path.append(index)
            for result in find_in_obj(value, condition, path=new_path):
                yield result

    # In case this is a dictionary
    if isinstance(obj, dict):
        for key, value in obj.items():
            new_path = list(path)
            new_path.append(key)
            for result in find_in_obj(value, condition, path=new_path):
                yield result

            if condition in key:
                new_path = list(path)
                new_path.append(key)
                yield new_path


def getFromDict(dataDict, mapList):
#gets value from dictionery based on list path
	for k in mapList:
		dataDict = dataDict[k]
	return dataDict


class GetMatchbook():
    
    def __init__(self):
        global matchbooktime
        self.dfOdds= self.getodds()

    def getodds(self):
        global matchbooktime
        payload = sjson.dumps({"username": "samiresquire", "password": "Snowpeak1"})
        headers = {"Content-Type": "application/json;", "Content-Encoding": "gzip", "Cache-Control": "no-cache"}
        requests.post('https://www.matchbook.com/edge/rest/security/session', data=payload, headers=headers)
        tennis_odds_url = 'https://www.matchbook.com/edge/rest/events?sport-ids=9&per-page=1000&name=moneyline&exchange-type=back-lay&side=back'
        tennis_odds_dict=sjson.loads(requests.get(tennis_odds_url, headers=headers).content)
    
        columns_n = ['date_m','match', 'player', 'odds', 'available-amount', 'side', 'inplay']
        df =  pd.DataFrame(columns=columns_n)
        for item in find_in_obj(tennis_odds_dict,"decimal-odds"):
            lst = item[:len(item)-5]
            lst.append('market-type')
            if getFromDict(tennis_odds_dict,lst) == 'money_line':
                odds= (getFromDict(tennis_odds_dict,item))
                lst = item[:len(item)-5]
                lst.append('start')
                date_m = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-5]
                lst.append('in-running-flag')
                inplay = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-3]
                lst.append('name')
                player = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-7]
                lst.append('name')
                match = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-1]
                lst.append('available-amount')
                available_amount = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-1]
                lst.append('side')
                side = (getFromDict(tennis_odds_dict,lst))
                lst = item[:len(item)-3]
                lst.append('event-id')
                eventid = (getFromDict(tennis_odds_dict,lst))
                
                #old code to get URL - just need eventid
#                lst = item[:len(item)-7]
#                lst.append('meta-tags')
#                meta = (getFromDict(tennis_odds_dict,lst))
#                metaURL = ''
#                for subdic in meta:
#                    metaURL = metaURL+ subdic.get('url-name') + "/"
#                metaURL = metaURL+str(eventid)
                
                
                df=df.append({'date_m':date_m, 'match':match, 'player':player ,'odds':odds ,'available-amount':available_amount, 'side':side, 'inplay':inplay, 'eventid':eventid},ignore_index=True)
                
        df['date_m'] = pd.to_datetime(df['date_m'])
        df=df.groupby(['date_m','match','player'], as_index=False).first()
        matchbooktime = datetime.datetime.now().timestamp()
        return df

def checkOdds(value, arg, df_odds,inplay):
    if inplay==True:
        return 'In play'
    else:
        try:
            odds = df_odds['odds'][(df_odds['match'].str.contains(value.split()[-1]))&(df_odds['match'].str.contains(arg.split()[-1]))&(df_odds['player'].str.contains('^'+value.split()[0][0]+'.*'+value.split()[-1]+'$'))].iloc[0]
        except Exception as inst:
            odds= '-'
        return odds

def getinplay(value, arg, df_odds):
    try:
        odds = df_odds['inplay'][(df_odds['match'].str.contains(value.split()[-1]))&(df_odds['match'].str.contains(arg.split()[-1]))&(df_odds['player'].str.contains('^'+value.split()[0][0]+'.*'+value.split()[-1]+'$'))].iloc[0]
    except Exception as inst:
        odds= 'False'
    return odds


def checkvalue(odds, prob,surfA, formA, surfB, formB):
    "Multiplies the arg and the value"
    if (odds == 'NA') or (odds == 0) or (isinstance(odds, str)):
        return 0 
    if (odds * prob >=1.1) and (surfA >=0.7*surfB) and (formA >=formB):
        cv= 1
    else:
        cv= 0
    return cv

def getDate(value, arg, df_odds, dbDate, inplay, fillD=1):
    "Check dates"

    try:
        if (inplay==True) and (fillD!=1):
            dateM = "In play"
        else:
            dateM = df_odds['date_m'][(df_odds['match'].str.contains(value.split()[-1]))&(df_odds['match'].str.contains(arg.split()[-1]))&(df_odds['player'].str.contains('^'+value.split()[0][0]+'.*'+value.split()[-1]+'$'))].iloc[0]
    except Exception as inst:
        if fillD==1:
            dateM = pd.to_datetime(dbDate)+pd.DateOffset(days=10)#adding 10days to put to bottom
        else: 
             dateM = ''
    return dateM

def getfield(value, arg, df_odds, field):
    try:
        odds = df_odds[field][(df_odds['match'].str.contains(value.split()[-1]))&(df_odds['match'].str.contains(arg.split()[-1]))&(df_odds['player'].str.contains('^'+value.split()[0][0]+'.*'+value.split()[-1]+'$'))].iloc[0]
    except Exception as inst:
        odds= 'False'
    return odds


def revscore(score):
    new = []
    j = 0
    for i in range(len(score)):
         if (score[i] == ' '):
             new.append(score[j:i][::-1] + ' ')
             j = i + 1
         elif (i == len(score)-1):
             new.append(score[j:i+1][::-1])
    new = "".join(new)
    new = new.replace(')' , '#')
    new = new.replace('(' , ')')
    new = new.replace('#' , '(')
    return new