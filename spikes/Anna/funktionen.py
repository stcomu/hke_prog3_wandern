def filter_schwierigkeit(tourdaten, schwierigkeit):
    """ Filtert die Touren nach der gewollten Schwierigkeit."""
    return [tour for tour in tourdaten if tour ['Schwierigkeit'] == schwierigkeit]

def filter_distanz(tourdaten, min_distanz, max_distanz):
    """ Filtert die Touren nach der gewollten Distanz."""
    return [tour for tour in tourdaten if min_distanz <= tour['Distanz'] <= max_distanz]    

def filter_hoehenmeter(tourdaten, min_hoehenmeter, max_hoehenmeter):
    """ Filtert die Touren nach der gewollten Höhenmeterzahl."""
    return [tour for tour in tourdaten if min_hoehenmeter <= tour['Höhenmeter'] <= max_hoehenmeter]     

def filter_dauer(tourdaten, min_dauer, max_dauer):
    """ Filtert die Touren nach der gewollten Dauer."""
    return [tour for tour in tourdaten if min_dauer <= tour['Dauer'] <= max_dauer]  

Passende_touren = []
