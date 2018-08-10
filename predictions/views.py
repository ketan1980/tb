from django.shortcuts import render
from .models import Predictions, PrevMatches, HistRank, CompleteMatches
from django.db.models.functions import Concat
from django.db.models import CharField, Value as V, F
from .pyFunctions import GetOddsMatchbook as mb

# Create your views here.
def pred_list(request):
    #pass three queries to the template. Womens tournament, mens tournament names and then all the the data
    preds = Predictions.objects.all().order_by('Gender','Tournament')
    preds = preds.annotate(Gen_Tourn=Concat('Gender', V('s - '),'Tournament' ))
    #preds = preds.annotate(Test = mb.checkOdds('Player1','Player2',Odds.dfOdds))
    preds_m = preds.filter(Gender='Men').order_by('Tournament')
    preds_w = preds.filter(Gender='Women').order_by('Tournament')
    # buliding dict so can be looked up quickly
    compmatches = {}
    for i in CompleteMatches.objects.all():
        compmatches.update({i.Player1 + i.Player2 + i.Tourn + i.Round: i.Result})
    
    #using dictsortreversed (dictsort) on template to sort
    #preds = preds.values()
    try:
        Odds = mb.GetMatchbook()
        for pred in preds:
            pred.inplay=mb.getinplay(pred.Player1,pred.Player2,Odds.dfOdds)
            pred.p1Odds = mb.checkOdds(pred.Player1,pred.Player2,Odds.dfOdds, pred.inplay)
            pred.p2Odds = mb.checkOdds(pred.Player2,pred.Player1,Odds.dfOdds, pred.inplay)
            pred.p1Value = mb.checkvalue(pred.p1Odds, pred.Probability_Player1, pred.SurfaceWinRate_Player1, pred.RecentForm_Player1,pred.SurfaceWinRate_Player2, pred.RecentForm_Player2)
            pred.p2Value = mb.checkvalue(pred.p2Odds, pred.Probability_Player2, pred.SurfaceWinRate_Player2, pred.RecentForm_Player2,pred.SurfaceWinRate_Player1, pred.RecentForm_Player1)
            pred.result = compmatches.get(pred.Player1+pred.Player2+pred.Tournament+pred.Round)
            if pred.result == None:
                try:
                    pred.result = mb.revscore(compmatches.get(pred.Player2+pred.Player1+pred.Tournament+pred.Round))
                except:
                    pred.result = None
            
            pred.dateM=mb.getDate(pred.Player1,pred.Player2,Odds.dfOdds, pred.Date,pred.inplay)#used to sort
            if pred.result == None:
                pred.dateS=mb.getDate(pred.Player1,pred.Player2,Odds.dfOdds, pred.Date,pred.inplay,0)#same as above but function doesnt show unmatched dates - used on site
            else:
                pred.dateS = 'Completed'
            
            pred.url = mb.getfield(pred.Player1,pred.Player2,Odds.dfOdds, 'eventid')
                
    except:
        for pred in preds:
            pred.dateM=pred.Date#used to sort
            pred.dateS=pred.Date
            pred.result = compmatches.get(pred.Player1+pred.Player2+pred.Tournament+pred.Round)
            if pred.result == None:
                try:
                    pred.result = mb.revscore(compmatches.get(pred.Player2+pred.Player1+pred.Tournament+pred.Round))
                except:
                    pred.result = None

#        adding fields to dict below
#        pred['dateM']=mb.getDate(pred['Player1'],pred['Player2'],Odds.dfOdds, pred['Date'])
#        pred['p1Odds'] = mb.checkOdds(pred['Player1'],pred['Player2'],Odds.dfOdds)
#        pred['p2Odds'] = mb.checkOdds(pred['Player2'],pred['Player1'],Odds.dfOdds)
#        pred['p1Value'] = mb.checkvalue(pred['p1Odds'], pred['Probability_Player1'])
#        pred['p2Value'] = mb.checkvalue(pred['p2Odds'], pred['Probability_Player2'])
    
    return render(request, 'pred_list.html', {'preds': preds, 'preds_m': preds_m, 'preds_w': preds_w})


def spider_chart(request, pk):
    stats = Predictions.objects.get(MatchID=pk)
    return render(request, 'spider_ajax.html', {'stats': stats})


def player_stats(request, pk):
    stats = Predictions.objects.get(MatchID=pk)
    return render(request, 'player_stats_ajax.html', {'stats': stats})

def hhmatches(request, pk):
    stats = Predictions.objects.get(MatchID=pk)
    h2h = PrevMatches.objects.filter(ID_P1=stats.ID_P1, table = 'previousencounters').order_by('-DATE_R')
    return render(request, 'hhmatches.html', {'h2h': h2h, 'matchid' : pk, 'stats': stats})

def rankChart(request, pk):
    stats = Predictions.objects.get(MatchID=pk)
    p1HistRank = HistRank.objects.filter(ID_P1=stats.ID_P1)
    p2HistRank = HistRank.objects.filter(ID_P1=stats.ID_P2)
    return render(request, 'histrank.html', {'p1HistRank': p1HistRank,'p2HistRank': p2HistRank, 'matchid' : pk, 'stats': stats})

def pastmatches(request, pk, pl):
    stats = Predictions.objects.get(MatchID=pk)
    pm = PrevMatches.objects.filter(ID_P1=pl, table = 'previousmatches').order_by('-DATE_R')
    return render(request, 'pastmatches.html', {'pm': pm, 'matchid' : pk, 'stats': stats})


