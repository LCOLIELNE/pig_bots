    if player == 1:
        if scores[1] + round_score >= 100:
            return False
        if scores[1] >= scores[0]:
            if 13 <= round_score <= 19:
                return False
        if scores [1] <= scores[0]:
            if 17 <= round_score <= 28:
                return False
        if scores[1] == scores[0]:
            if 15 <= round_score <= 25:
                return False
        if round_score == 0:
            if 13 <= round_score <= 20:
                return False
