from django.db import models

# Create your models here.


class PrevMatches(models.Model):
    ID_P1 = models.IntegerField(blank=True, null=True)
    ID_P2 = models.IntegerField(blank=True, null=True)
    Player1 = models.CharField(blank=True, max_length=200)
    Player2 = models.CharField(blank=True, max_length=200)
    p1pos = models.IntegerField(blank=True, null=True)
    p2pos = models.IntegerField(blank=True, null=True)
    DATE_R = models.DateField(blank=True, null=True)
    NAME_T = models.CharField(blank=True, max_length=200)
    NAME_C = models.CharField(blank=True, max_length=50)
    Round = models.CharField(blank=True, max_length=200)
    RESULT_G = models.CharField(blank=True, max_length=50)
    winloss = models.IntegerField(blank=True, null=True)
    matchnumber = models.IntegerField(blank=True, null=True)
    table = models.CharField(blank=True, max_length=50)
    Gender = models.CharField(blank=True, max_length=50)


class HistRank(models.Model):
    Player1 = models.CharField(blank=True, max_length=200)
    ID_P1 = models.IntegerField(blank=True, null=True)
    p1age = models.FloatField(blank=True, null=True)
    p1pos = models.IntegerField(blank=True, null=True)
    DATE_R = models.DateField(blank=True, null=True)
    Gender = models.CharField(blank=True, max_length=50)


class CompleteMatches(models.Model):
    Player1 = models.CharField(blank=True, max_length=200)
    Player2 = models.CharField(blank=True, max_length=200)
    Tourn = models.CharField(blank=True, max_length =200,null=True)
    Round = models.CharField(blank=True, max_length =20,null=True)
    Gender = models.CharField(blank=True, max_length=50)
    Result = models.CharField(blank=True, max_length=50)



class Predictions(models.Model):
    MatchID = models.IntegerField(blank=True, null=True)
    ID_P1 = models.IntegerField(blank=True,null=True)
    ID_P2 = models.IntegerField(blank=True,null=True)
    Country = models.CharField(blank=True, max_length =5,null=True)
    Tournament = models.CharField(blank=True, max_length =200,null=True)
    Surface = models.CharField(blank=True, max_length =100,null=True)
    Tier = models.CharField(blank=True, max_length =200,null=True)
    Round = models.CharField(blank=True, max_length =20,null=True)
    Date = models.DateField(blank=True,null=True)
    Year = models.IntegerField(blank=True,null=True)
    Player1 = models.CharField(blank=True, max_length =200,null=True)
    Player2 = models.CharField(blank=True, max_length =200,null=True)
    Odds_Player1 = models.FloatField(blank=True,null=True)
    Odds_Player2 = models.FloatField(blank=True,null=True)
    Probability_Player1 = models.FloatField(blank=True,null=True)
    Probability_Player2 = models.FloatField(blank=True,null=True)
    Country_Player1 = models.CharField(blank=True, max_length =5,null=True)
    Country_Player2 = models.CharField(blank=True, max_length =5,null=True)
    Trade = models.CharField(blank=True, max_length =200,null=True)
    TradeOdds = models.FloatField(blank=True,null=True)
    Risk = models.CharField(blank=True, max_length =20,null=True)
    Rank_Player1 = models.IntegerField(blank=True,null=True)
    Rank_Player2 = models.IntegerField(blank=True,null=True)
    RankingPoints_Player1 = models.IntegerField(blank=True,null=True)
    RankingPoints_Player2 = models.IntegerField(blank=True,null=True)
    Age_Player1 = models.FloatField(blank=True,null=True)
    Age_Player2 = models.FloatField(blank=True,null=True)
    Hand_Player1 = models.CharField(blank=True, max_length =20,null=True)
    Hand_Player2 = models.CharField(blank=True, max_length =20,null=True)
    Backhand_Player1 = models.CharField(blank=True, max_length =20,null=True)
    Backhand_Player2 = models.CharField(blank=True, max_length =20,null=True)
    Height_Player1 = models.IntegerField(blank=True,null=True)
    Height_Player2 = models.IntegerField(blank=True,null=True)
    Weight_Player1 = models.IntegerField(blank=True,null=True)
    Weight_Player2 = models.IntegerField(blank=True,null=True)
    Last5matches_Player1 = models.CharField(blank=True, max_length =10,null=True)
    Last5matches_Player2 = models.CharField(blank=True, max_length =10,null=True)
    Head2HeadWins_Player1 = models.IntegerField(blank=True,null=True)
    Head2HeadWins_Player2 = models.IntegerField(blank=True,null=True)
    WinRate_Player1 = models.FloatField(blank=True,null=True)
    WinRate_Player2 = models.FloatField(blank=True,null=True)
    SurfaceWinRate_Player1 = models.FloatField(blank=True,null=True)
    SurfaceWinRate_Player2 = models.FloatField(blank=True,null=True)
    RecentForm_Player1 = models.FloatField(blank=True,null=True)
    RecentForm_Player2 = models.FloatField(blank=True,null=True)
    Head2Head_Player1 = models.IntegerField(blank=True,null=True)
    Head2Head_Player2 = models.IntegerField(blank=True,null=True)
    CommonOpponent_Player1 = models.FloatField(blank=True,null=True)
    CommonOpponent_Player2 = models.FloatField(blank=True,null=True)
    CommonOpponentSurface_Player1 = models.FloatField(blank=True,null=True)
    CommonOpponentSurface_Player2 = models.FloatField(blank=True,null=True)
    TotalTitles_Player1 = models.IntegerField(blank=True,null=True)
    TotalTitles_Player2 = models.IntegerField(blank=True,null=True)
    ATPTitles_Player1 = models.IntegerField(blank=True,null=True)
    ATPTitles_Player2 = models.IntegerField(blank=True,null=True)
    ChalTitles_Player1 = models.IntegerField(blank=True,null=True)
    ChalTitles_Player2 = models.IntegerField(blank=True,null=True)
    ServeForm_Player1 = models.FloatField(blank=True,null=True)
    ServeForm_Player2 = models.FloatField(blank=True,null=True)
    ReturnForm_Player1 = models.FloatField(blank=True,null=True)
    ReturnForm_Player2 = models.FloatField(blank=True,null=True)
    Experience_Player1 = models.IntegerField(blank=True,null=True)
    Experience_Player2 = models.IntegerField(blank=True,null=True)
    Reliability_Player1 = models.FloatField(blank=True,null=True)
    Reliability_Player2 = models.FloatField(blank=True,null=True)
    Gender = models.CharField(blank=True, max_length =5,null=True)
    WTATitles_Player1 = models.IntegerField(blank=True,null=True)
    WTATitles_Player2 = models.IntegerField(blank=True,null=True)
    S125kTitles_Player1 = models.IntegerField(blank=True,null=True)
    S125kTitles_Player2 = models.IntegerField(blank=True,null=True)
    WinRateOpponentquality_Player1 = models.FloatField(blank=True,null=True)
    WinRateOpponentquality_Player2 = models.FloatField(blank=True,null=True)
    QualityForm_Player1 = models.FloatField(blank=True,null=True)
    QualityForm_Player2 = models.FloatField(blank=True,null=True)
    Momentum_Player1 = models.FloatField(blank=True,null=True)
    Momentum_Player2 = models.FloatField(blank=True,null=True)
