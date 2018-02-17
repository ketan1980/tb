from django.db import models

# Create your models here.


class Predictions(models.Model):
    index = models.IntegerField(default =1)
    ID_P1 = models.IntegerField(null=True)
    ID_P2 = models.IntegerField(null=True)
    DATE_R = models.IntegerField(null=True)
    p2point = models.IntegerField(null=True)
    p2pos = models.IntegerField(null=True)
    p1point = models.IntegerField(null=True)
    p1pos = models.IntegerField(null=True)
    RESULT_G = models.CharField(max_length=200)
    NAME_T = models.CharField(max_length=200)
    Player1 = models.CharField(max_length=200)
    Player2 = models.CharField(max_length=200)
    Player1Bday = models.DateTimeField( blank=True, null=True)
    Player2Bday = models.DateTimeField( blank=True, null=True)
    p1country = models.CharField(max_length=10)
    p2country = models.CharField(max_length=10)
    NAME_C = models.CharField(max_length=10)
    Round = models.CharField(max_length=10)
    PRIZE_T = models.CharField(max_length=10)
    COUNTRY_T = models.CharField(max_length=10)
    TIER_T = models.CharField(max_length=10)
    p1height = models.IntegerField(null=True)
    p1weight = models.IntegerField(null=True)
    p1hand = models.CharField(max_length=50)
    p1bhand = models.CharField(max_length=50)
    p2height = models.IntegerField(null=True)
    p2weight = models.IntegerField(null=True)
    p2hand = models.CharField(max_length=50)
    p2bhand = models.CharField(max_length=50)
    FS_1 = models.FloatField(null=True)
    FSOF_1 = models.FloatField(null=True)
    ACES_1 = models.FloatField(null=True)
    DF_1 = models.FloatField(null=True)
    UE_1 = models.FloatField(null=True)
    W1S_1 = models.FloatField(null=True)
    W1SOF_1 = models.FloatField(null=True)
    W2S_1 = models.FloatField(null=True)
    W2SOF_1 = models.FloatField(null=True)
    WIS_1 = models.FloatField(null=True)
    BP_1 = models.FloatField(null=True)
    BPOF_1 = models.FloatField(null=True)
    NA_1 = models.FloatField(null=True)
    NAOF_1 = models.FloatField(null=True)
    TPW_1 = models.FloatField(null=True)
    FAST_1 = models.FloatField(null=True)
    A1S_1 = models.FloatField(null=True)
    A2S_1 = models.FloatField(null=True)
    FS_2 = models.FloatField(null=True)
    FSOF_2 = models.FloatField(null=True)
    ACES_2 = models.FloatField(null=True)
    DF_2 = models.FloatField(null=True)
    UE_2 = models.FloatField(null=True)
    W1S_2 = models.FloatField(null=True)
    W1SOF_2 = models.FloatField(null=True)
    W2S_2 = models.FloatField(null=True)
    W2SOF_2 = models.FloatField(null=True)
    WIS_2 = models.FloatField(null=True)
    BP_2 = models.FloatField(null=True)
    BPOF_2 = models.FloatField(null=True)
    NA_2 = models.FloatField(null=True)
    NAOF_2 = models.FloatField(null=True)
    TPW_2 = models.FloatField(null=True)
    FAST_2 = models.FloatField(null=True)
    A1S_2 = models.FloatField(null=True)
    A2S_2 = models.FloatField(null=True)
    RPW_1 = models.FloatField(null=True)
    RPWOF_1 = models.FloatField(null=True)
    RPW_2 = models.FloatField(null=True)
    RPWOF_2 = models.FloatField(null=True)
    ID_B_O = models.FloatField(null=True)
    K1 = models.FloatField(null=True)
    K2 = models.FloatField(null=True)
    resultscore = models.FloatField(null=True)
    resultsstatus = models.CharField(max_length=50)
    resultscore1_1 = models.CharField(max_length=50)
    resultscore1_2 = models.CharField(max_length=50)
    resultscore1_3 = models.CharField(max_length=50)
    resultscore1_4 = models.CharField(max_length=50)
    resultscore1_5 = models.CharField(max_length=50)
    p1games = models.FloatField(null=True)
    p2games = models.FloatField(null=True)
    p1age = models.FloatField(null=True)
    p2age = models.FloatField(null=True)
    totalgames = models.FloatField(null=True)
    p1homecountry = models.FloatField(null=True)
    p2homecountry = models.FloatField(null=True)
    winloss = models.FloatField(null=True)
    p1betprob = models.FloatField(null=True)
    p2betprob = models.FloatField(null=True)
    matchnumber = models.IntegerField(null=True)
    winlosslag1 = models.FloatField(null=True)
    acumlative_matches = models.FloatField(null=True)
    acumlative_wins = models.FloatField(null=True)
    winrate = models.FloatField(null=True)
    one = models.FloatField(null=True)
    form_1year = models.FloatField(null=True)
    matches_1year = models.FloatField(null=True)
    winrate1year = models.FloatField(null=True)
    uncertainty = models.FloatField(null=True)
    uncertainty90 = models.FloatField(null=True)
    uncertainty180 = models.FloatField(null=True)
    form_90 = models.FloatField(null=True)
    matches_90 = models.FloatField(null=True)
    winrate90 = models.FloatField(null=True)
    form_30 = models.FloatField(null=True)
    matches_30 = models.FloatField(null=True)
    winrate30 = models.FloatField(null=True)
    opponentrankingpointswon = models.IntegerField(null=True)
    winningpoints30 = models.FloatField(null=True)
    fatigue = models.FloatField(null=True)
    acumlative_matches_surface = models.FloatField(null=True)
    acumlative_wins_surface = models.FloatField(null=True)
    winrate_surface = models.FloatField(null=True)
    form_surface_30 = models.FloatField(null=True)
    matches_surface_30 = models.FloatField(null=True)
    winratesurface30 = models.FloatField(null=True)
    form_surface_90 = models.FloatField(null=True)
    matches_surface_90 = models.FloatField(null=True)
    winratesurface90 = models.FloatField(null=True)
    form_surface_365 = models.FloatField(null=True)
    matches_surface_365 = models.FloatField(null=True)
    winratesurface365 = models.FloatField(null=True)
    dayssincelastmatch = models.FloatField(null=True)
    winlosslag1opponent = models.IntegerField(null=True)
    lastopponentresult = models.CharField(max_length=50)
    acumlative_matchesvopponent = models.IntegerField(null=True)
    acumlative_winsvopponent = models.IntegerField(null=True)
    winratevopponent = models.FloatField(null=True)
    year = models.IntegerField(null=True)
    commonwinrate180 = models.FloatField(null=True)
    winlosslag1tournament = models.FloatField(null=True)
    tournamentmatches = models.FloatField(null=True)
    tournamentwins = models.FloatField(null=True)
    tournamentform = models.FloatField(null=True)
    tournamentwin = models.FloatField(null=True)
    tournamentwinlag1 = models.FloatField(null=True)
    tournamentswon = models.FloatField(null=True)
    totalgames5 = models.FloatField(null=True)
    winninggames5 = models.FloatField(null=True)
    gameswon5 = models.FloatField(null=True)
    p1servewon = models.FloatField(null=True)
    servepoints30 = models.FloatField(null=True)
    servepointswon30 = models.FloatField(null=True)
    servepointsrate30 = models.FloatField(null=True)
    servepoints90 = models.FloatField(null=True)
    servepointswon90 = models.FloatField(null=True)
    servepointsrate90 = models.FloatField(null=True)
    returnpoints30 = models.FloatField(null=True)
    returnpointswon30 = models.FloatField(null=True)
    returnpointsrate30 = models.FloatField(null=True)
    returnpoints90 = models.FloatField(null=True)
    returnpointswon90 = models.FloatField(null=True)
    returnpointsrate90 = models.FloatField(null=True)
    winrate_opponent = models.FloatField(null=True)
    acumlative_matches_opponent = models.IntegerField(null=True)
    acumlative_wins_opponent = models.IntegerField(null=True)
    form_1year_opponent = models.IntegerField(null=True)
    matches_1year_opponent = models.IntegerField(null=True)
    winrate1year_opponent = models.FloatField(null=True)
    form_90_opponent = models.IntegerField(null=True)
    matches_90_opponent = models.IntegerField(null=True)
    winrate90_opponent = models.FloatField(null=True)
    form_30_opponent = models.IntegerField(null=True)
    matches_30_opponent = models.IntegerField(null=True)
    winrate30_opponent = models.FloatField(null=True)
    opponentrankingpointswon_opponent = models.IntegerField(null=True)
    winningpoints30_opponent = models.IntegerField(null=True)
    fatigue_opponent = models.IntegerField(null=True)
    acumlative_matches_surface_opponent = models.IntegerField(null=True)
    acumlative_wins_surface_opponent = models.IntegerField(null=True)
    winrate_surface_opponent = models.FloatField(null=True)
    form_surface_30_opponent = models.IntegerField(null=True)
    matches_surface_30_opponent = models.IntegerField(null=True)
    winratesurface30_opponent = models.FloatField(null=True)
    form_surface_90_opponent = models.IntegerField(null=True)
    matches_surface_90_opponent = models.IntegerField(null=True)
    winratesurface90_opponent = models.FloatField(null=True)
    form_surface_365_opponent = models.IntegerField(null=True)
    matches_surface_365_opponent = models.IntegerField(null=True)
    winratesurface365_opponent = models.FloatField(null=True)
    dayssincelastmatch_opponent = models.FloatField(null=True)
    lastopponentresult_opponent = models.CharField(max_length=50)
    acumlative_matchesvopponent_opponent = models.IntegerField(null=True)
    acumlative_winsvopponent_opponent = models.IntegerField(null=True)
    winratevopponent_opponent = models.IntegerField(null=True)
    commonwinrate180_opponent = models.IntegerField(null=True)
    tournamentform_opponent = models.IntegerField(null=True)
    tournamentwin_opponent = models.IntegerField(null=True)
    tournamentswon_opponent = models.IntegerField(null=True)
    totalgames5_opponent = models.IntegerField(null=True)
    winninggames5_opponent = models.IntegerField(null=True)
    gameswon5_opponent = models.FloatField(null=True)
    servepoints30_opponent = models.IntegerField(null=True)
    servepointswon30_opponent = models.IntegerField(null=True)
    servepointsrate30_opponent = models.FloatField(null=True)
    servepoints90_opponent = models.IntegerField(null=True)
    servepointswon90_opponent = models.IntegerField(null=True)
    servepointsrate90_opponent = models.FloatField(null=True)
    returnpoints30_opponent = models.IntegerField(null=True)
    returnpointswon30_opponent = models.IntegerField(null=True)
    returnpointsrate30_opponent = models.FloatField(null=True)
    returnpoints90_opponent = models.IntegerField(null=True)
    returnpointswon90_opponent = models.IntegerField(null=True)
    returnpointsrate90_opponent = models.FloatField(null=True)
    uncertainty90_opponent = models.FloatField(null=True)
    uncertainty180_opponent = models.FloatField(null=True)
    relheight = models.FloatField(null=True)
    relweight = models.FloatField(null=True)
    relage = models.FloatField(null=True)
    relhc = models.FloatField(null=True)
    relwratesurf30 = models.FloatField(null=True)
    relwratesurf90 = models.FloatField(null=True)
    relwratesurf365 = models.FloatField(null=True)
    relwrateo = models.FloatField(null=True)
    relgw5 = models.FloatField(null=True)
    relfatigue = models.IntegerField(null=True)
    relserve30 = models.IntegerField(null=True)
    relserve90 = models.IntegerField(null=True)
    relret30 = models.IntegerField(null=True)
    relret90 = models.IntegerField(null=True)
    relserveret30 = models.IntegerField(null=True)
    relserveret90 = models.IntegerField(null=True)
    relhanded = models.IntegerField(null=True)
    relcom180 = models.IntegerField(null=True)
    relwinpoints30 = models.IntegerField(null=True)
    relams = models.IntegerField(null=True)
    relpoints = models.IntegerField(null=True)
    reldays = models.IntegerField(null=True)
    relmatches30 = models.IntegerField(null=True)
    relmatches90 = models.IntegerField(null=True)
    reluncertainty90 = models.IntegerField(null=True)
    reluncertainty180 = models.IntegerField(null=True)
    winlossclass = models.CharField(max_length=50)
    ProbabilityPlayer2rf = models.FloatField(null=True)
    ProbabilityPlayer1rf = models.FloatField(null=True)
    traderf = models.CharField(max_length=50)
    TradeSignalrf = models.IntegerField(null=True)
    WinningSignalrf = models.IntegerField(null=True)
    TradeOddsrf = models.FloatField(null=True)
    Returnrf = models.FloatField(null=True)
    ProbabilityPlayer2xgb = models.FloatField(null=True)
    ProbabilityPlayer1xgb = models.FloatField(null=True)
    tradexgb = models.CharField(max_length=50)
    TradeSignalxgb = models.IntegerField(null=True)
    WinningSignalxgb = models.IntegerField(null=True)
    TradeOddsxgb = models.FloatField(null=True)
    Returnxgb = models.FloatField(null=True)
    ProbabilityPlayer2earth = models.FloatField(null=True)
    ProbabilityPlayer1earth = models.FloatField(null=True)
    tradeearth = models.CharField(max_length=50)
    TradeSignalearth = models.IntegerField(null=True)
    WinningSignalearth = models.IntegerField(null=True)
    TradeOddsearth = models.FloatField(null=True)
    Returnearth = models.FloatField(null=True)
    ProbabilityPlayer1rfxgb = models.FloatField(null=True)
    ProbabilityPlayer2rfxgb = models.FloatField(null=True)
    traderfxgb = models.CharField(max_length=50)
    TradeSignalrfxgb = models.IntegerField(null=True)
    WinningSignalrfxgb = models.IntegerField(null=True)
    TradeOddsrfxgb = models.FloatField(null=True)
    Returnrfxgb = models.FloatField(null=True)
    playerprobp2 = models.FloatField(null=True)
    playerprobp1 = models.FloatField(null=True)
    tradepm = models.CharField(max_length=50)
    TradeSignalpm = models.IntegerField(null=True)
    WinningSignalpm = models.IntegerField(null=True)
    TradeOddspm = models.FloatField(null=True)
    Returnpm = models.FloatField(null=True)
    ProbabilityPlayer1rfxgbpm = models.FloatField(null=True)
    ProbabilityPlayer2rfxgbpm = models.FloatField(null=True)
    traderfxgbpm = models.CharField(max_length=50)
    TradeSignalrfxgbpm = models.IntegerField(null=True)
    WinningSignalrfxgbpm = models.IntegerField(null=True)
    TradeOddsrfxgbpm = models.FloatField(null=True)
    Returnrfxgbpm = models.FloatField(null=True)
    Risk = models.CharField(max_length=50)
