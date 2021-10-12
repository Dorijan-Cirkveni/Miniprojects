# import time


def calculate_pull(startStates: dict, outcomes: dict):
    newStates = dict()
    for state, startOdds in startStates.items():
        for (newState, jumpOdds) in outcomes[state]:
            if newState not in newStates:
                newStates[newState] = 0
            newStates[newState] += startOdds * jumpOdds
    return newStates


def setup_outcomes_genshin_char():
    """
    This function generates a dictionary of possible outcomes of a single character wish in the Genshin Impact
    character event banner. Since soft pity has not been not officially confirmed or mathematically determined,
    it is ignored here.
    """
    outcomes = dict()
    x = '0-0'
    for i in range(89):
        y = '0-' + str(i + 1)
        outcomes[x] = [(y, 0.994), ('1-0', 0.003), ('0-0', 0.003)]
        x = y
    outcomes['0-89'] = [('1-0', 0.5), ('0-0', 0.5)]
    x = '1-0'
    for i in range(89):
        y = '1-' + str(i + 1)
        outcomes[x] = [(y, 0.994), ('0-0', 0.006)]
        x = y
    outcomes['1-89'] = [('0-0', 1)]
    return outcomes


def simulate_genshin_banner_character_odds(startPity, wishesLeft, lost5050=False):
    """

    """
    # startTime = time.time()
    outcomes = setup_outcomes_genshin_char()
    start = {str(lost5050 * 1) + '-' + str(startPity): 1}
    resultOdds = 0
    for i in range(wishesLeft):
        end = calculate_pull(start, outcomes)
        if '0-0' in end:  # This is a temporary solution.
            resultOdds += end['0-0']
            end:dict
            end.pop('0-0')
        # print(time.time() - startTime)
        start = end
    return resultOdds


def main():
    res = simulate_genshin_banner_character_odds(34,63)
    print(res)
    return


if __name__ == "__main__":
    main()
