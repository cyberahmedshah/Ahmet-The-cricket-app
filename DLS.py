def calculateDLS(target, overs, runs):
    if overs <= 20:
        par_score = target * (1 - (overs / 20))
    else:
        par_score = target * (1 - (overs / 50))
    
    if runs >= par_score:
        return "Team batting second is ahead"
    else:
        return "Team batting second is behind"
    
    