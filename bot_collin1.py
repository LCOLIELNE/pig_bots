
    if player == 1:
        if scores[1] + round_score >= 100:
            return False
        if scores[0] == scores[1] + 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14:
            if 14 <= round_score <= 18:
                return False
        if scores[0] >= scores[1] + 15:
            if 20 <= round_score <= 30:
                return False
        if scores[1] == scores[0] + 5 or 6 or 7 or 8 or 9:
            if 16 <= round_score <= 24:
                return False
        if scores[1] >= scores[0] + 10:
            if 20 >= round_score >= 30:
                return False
