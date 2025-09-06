from __future__ import annotations

import numpy as np


def startSimulation(numberOfTrials : int = 10000, threshold=0.75) -> float:
    """
    ::
        Will India announce a new space mission launch before January 2026?

        BASE: 96% (0.96) -> based on fermi and poisson distribution.

        The simulation is based on 3 basic components: Political, Budget, and Technical.
        Political-ISRO is independent and no effect if US relation is sour. 95% that tarrifs or supply chain
            would not affect the space missions in any way.
        Budget-Tarrifs and shrinking have affected the GDP -> 0.5 less than projected - therefore assumed
            the budget for space missions will shrink by the ratio of 0.5/7.8 = 6.4% or 93.6.
        Technical-If there are a lot of failures than there would be review and possibly a pause on space missions
            and therefore on space missions announcements.

        BLACK SWAN - 1%.

        Parameters:
            numberOfSimulations (int)  : The total number of trials.
            threshold (float)          : The chance that the requested event will happen.
        Returns:
            estimatedProbability(float): The probabilty that the event will happend based on the number of trials.
    """
    successCount = 0

    weights = {
        'base': 0.38,
        'political': 0.19,
        'budget': 0.33,
        'technical': 0.10,
    }

    for _ in range(numberOfTrials):

        base = np.random.random() < 0.96
        political = np.random.random() < 0.95
        budget = np.random.random() < 0.934
        technical = np.random.random() < 0.45

        blackSwan = np.random.random() < 0.01
        if blackSwan:
            base *= 0.1
            political *= 0.1
            budget *= 0.1
            technical *= 0.1

        score = (political * weights['political'] +
                 budget * weights['budget'] +
                 technical * weights['technical'] +
                 base * weights['base'])
        if score >= threshold:
            successCount+=1

    estimatedProbability=successCount/numberOfTrials
    return(estimatedProbability)

if __name__ == "__main__":
    print(startSimulation())
