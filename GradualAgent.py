from prison import Player


class GradualAgent(Player):
    """
    The gradualPlayer is similar to TfT such that it cooperates on the first move, 
    but if any of the opponents defects, the agent will defect as well. 
    After n defections of any of the 2 opponents, the agent will also defect n times, 
    and calms down with 2 cooperations to reset the opponent if the opponent is forgiving.
    """

    def __init__(self):
        self.defectionsLeft = -2

    def studentID(self):
        """ Returns the creator's numeric studentID """
        return "20536826"

    def agentName(self):
        """ Returns a creative name for the agent """
        return self.__class__.__name__

    def play(self, myHistory, oppHistory1, oppHistory2):
        """ 
        Given a history of play, computes and returns your next move
        ( 0 = cooperate; 1 = defect )
        myHistory = list of int representing your past plays
        oppHistory1 = list of int representing opponent 1's past plays
        oppHistory2 = list of int representing opponent 2's past plays
        NB: use len(myHistory) to find the number of games played
        """
        # Cooperate on first round
        if len(myHistory) == 0:
            return 0

        # Defect defectionsLeft times
        if self.defectionsLeft > 0:
            self.defectionsLeft -= 1
            return 1

        # Calm down with 2 cooperations
        if self.defectionsLeft == 0 or self.defectionsLeft == -1:
            self.defectionsLeft -= 1
            return 0

        # If both opponents defect, use the greater of the 2
        if oppHistory1[-1] == 1 and oppHistory2[-1] == 1:
            self.defectionsLeft = max(oppHistory1.count(1), oppHistory2.count(1)) - 1
            return 1

        # If an opponent defected n times, defect n times
        if oppHistory1[-1] == 1:
            self.defectionsLeft = oppHistory1.count(1) - 1
            return 1
        elif oppHistory2[-1] == 1:
            self.defectionsLeft = oppHistory2.count(1) - 1
            return 1

        return 0

