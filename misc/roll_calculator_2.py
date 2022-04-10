# import time


def calculate_pull(startStates: dict):
    newStates = dict()
    for state, startOdds in startStates.items():
        X = setup_outcomes_genshin_char(state)
        for newState in X:
            jumpOdds = X[newState]
            if newState not in newStates:
                newStates[newState] = 0
            newStates[newState] += startOdds * jumpOdds
    return newStates


def setup_outcomes_genshin_char(start_state):
    """
    This function generates a dictionary of possible outcomes of a single character wish in the Genshin Impact
    character event banner given a certain starting state.
    Since soft pity has not been not officially confirmed or mathematically determined, it is ignored here.
    """
    outcomes = dict()
    successes, lastFail, pity = start_state
    newpity = pity + 1
    if newpity == 90:
        if lastFail:
            outcomes[(successes + 1, False, 0)] = 1.0
        else:
            outcomes[(successes, True, 0)] = 0.5
            outcomes[(successes + 1, False, 0)] = 0.5
    else:
        pullodds = 0.006
        outcomes[(successes, lastFail, newpity)] = 1.0 - pullodds
        if lastFail:
            outcomes[(successes + 1, False, 0)] = pullodds
        else:
            outcomes[(successes, True, 0)] = pullodds / 2
            outcomes[(successes + 1, False, 0)] = pullodds / 2
    return outcomes


def simulate_genshin_banner_character_odds(startPity, wishesLeft: set, lost5050=False):
    """

    """
    start = {(0, lost5050, startPity): 1.0}
    wishLimit = max(wishesLeft)
    end = start
    for i in range(wishLimit):
        end = calculate_pull(start)
        start = end
    return end


def calculate_odds(odds_raw, include_5050=True):
    X = dict()
    for k in odds_raw:
        k2 = (k[0], k[1]) if include_5050 else k[0]
        if k2 not in X:
            X[k2] = 0
        X[k2] += odds_raw[k]
    return X


def main():
    odds=simulate_genshin_banner_character_odds(52, {190})
    res=calculate_odds(odds)
    for e in res:
        print(e,res[e])
    return


if __name__ == "__main__":
    main()
