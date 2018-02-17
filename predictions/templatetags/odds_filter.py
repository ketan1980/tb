from django import template
import requests
import simplejson as sjson
import pandas as pd


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


register = template.Library()


payload = sjson.dumps({"username": "samiresquire", "password": "Snowpeak1"})
headers = {"Content-Type": "application/json;", "Content-Encoding": "gzip", "Cache-Control": "no-cache"}
r = requests.post('https://www.matchbook.com/edge/rest/security/session', data=payload, headers=headers)
tennis_odds_url = 'https://www.matchbook.com/edge/rest/events?sport-ids=9&per-page=100&name=moneyline'
tennis_odds_dict=sjson.loads(requests.get(tennis_odds_url, headers=headers).content)

columns_n = ['date_m','match', 'player', 'odds', 'available-amount', 'side']
df =  pd.DataFrame(columns=columns_n)
for item in find_in_obj(tennis_odds_dict,"decimal-odds"):
    lst = item[:len(item)-5]
    lst.append('market-type')
    if getFromDict(tennis_odds_dict,lst) == 'money_line':
        odds= (getFromDict(tennis_odds_dict,item))
        lst = item[:len(item)-5]
        lst.append('start')
        date_m = (getFromDict(tennis_odds_dict,lst))
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
        df=df.append({'date_m':date_m, 'match':match, 'player':player ,'odds':odds ,'available-amount':available_amount, 'side':side},ignore_index=True)
df['date_m'] = pd.to_datetime(df['date_m'])
df=df[df['side']=='back'].groupby(['date_m','match','player'], as_index=False).first()


@register.filter
def lower(value):
    # Only one argument.
    """Converts a string into all lowercase"""
    return value.lower()


@register.filter
def checkOdds(value, arg):
	try:
		#odds=df['odds'][(df['match'].str.contains(value.split()[-1]))].iloc[0]
		odds = df['odds'][(df['match'].str.contains(value.split()[-1]))&(df['match'].str.contains(arg.split()[-1]))&(df['player'].str.contains(value.split()[-1]))].iloc[0]
	except Exception as inst:
		odds= 'NA'
	return odds

@register.filter
def conpercent(value):
    "Multiplies the arg and the value"
    return value * 100


@register.filter
def checkvalue(value, arg):
    "Multiplies the arg and the value"
    if value * arg >=1.25:
        cv='Y'
    else:
        cv='N'
    return cv
