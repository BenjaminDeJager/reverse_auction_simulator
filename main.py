from random import random, randint


def convert_strategy(strategy):
    return [strategy[j + 1] - strategy[j] for j in range(len(strategy) - 1)]


def generate_strategy(history):
    strategy = [0]

    for i in range(len(history)):
        strategy.append(strategy[-1] + history[i])

    # firing_range[i] = firing_range[i-1] + i'th interval's length
    return strategy


def array_proportions(array, sig_figs = None):
    if sum(array):
        if sig_figs:
            return [round(x / sum(array), sig_figs) for x in array]
        return [x / sum(array) for x in array]


class Player:
    def __init__(self, start_value, num_choices):
        self.memory = [start_value * num_choices] * num_choices
        self.strategy = [start_value * x for x in range(num_choices)]

    def __str__(self):
        return str([round(x / sum(convert_strategy(self.strategy)), 4) for x in convert_strategy(self.strategy) if x != 0])

    def pick_Num(self, history, targets):
        # we want a random integer inside the range [0, total] such that when mapped inside <targets>,
        # we know which weighted choice to go with.
        total_wins = sum(history)
        choice = -1

        if total_wins > len(history):
            ranNum = round(random() * total_wins)
            for j in range(len(targets) - 1):
                if targets[j] <= ranNum < targets[j + 1]:
                    choice = j
        else:
            choice = randint(0, len(history) - 1)

        return choice

    def update_memorys(self, new_memory):
        for i in range(len(new_memory)):
            self.memory[i] += new_memory[i]


class ReverseAuction:
    def __init__(self, start_value, num_choices, num_players):
        self.history = [num_choices * start_value] * num_choices
        self.players = [Player(start_value, num_choices)] * num_players
        self.losses = 0
        self.total_games = 0

    def game_map(self):
        return array_proportions(self.history)

    def __str__(self):
        return "total=" + str([x for x in self.history]) \
               + " proportions=" + str([round(x / sum(self.history), 4) for x in self.history]) \
               + " losses="+str(self.losses)

    # return a array of a integer for each play in play_list that gives the winnings to that player by lowest_unique rules
    def lowest_unique_winnings(self, play_list):
        if len(play_list) < 1:
            print("empty play_list!:", play_list)
            return None

        unique = sorted(set(play_list))
        least = -1

        for play in unique:
            if play_list.count(play) == 1:
                least = play
                break

        winners = [0] * len(play_list)
        if least > -1:
            winners[play_list.index(least)] += 1

        return winners

    def play_round(self):
        plays = []

        for player in self.players:
            player.strategy = generate_strategy(self.history)
            plays.append(player.pick_Num(self.history, player.strategy))

        winners = self.lowest_unique_winnings(plays)
        for j in range(len(self.players)):
            if winners[j] > 0:
                self.history[plays[j]] += winners[j]
            self.players[j].update_memorys(winners)
        if sum(winners) == 0:
            self.losses += 1
        self.total_games += 1

    def stability(self):
        total = [0]*len(self.history)
        for player in self.players:
            for i in range(len(self.history)):
                total[i] += abs(self.history[i] - player.memory[i])

        return sum(total)/(len(total)*sum(self.history))

    def run_set(self, set_size, num_prints):
        temp = []
        for i in range(set_size):
            if num_prints and (i + 1) % round(set_size / num_prints) == 0:
                print("game " + str(i + 1) + " out of " + str(set_size) + ": " + str(self))
                temp = ""
                for j in range(len(self.players)):
                    temp += "\tplayer " + str(j+1) + ": " + str(self.players[j]) + "\n"
                print(temp)
            self.play_round()


num_sets = 20
num_games = 10
run_size = 200
num_players = 3
num_choices = 3
test_games = [ReverseAuction(1, num_players, num_choices)]*num_games
results = [0]*num_games
set_averages = []*num_sets
temp = [0]*num_choices

for i in range(num_sets):
    for j in range(num_games):
        test_games[j].run_set(run_size*(i+1), 0)
        # print("size, total)", run_size*i*j, test_games[j].total_games, "):", array_proportions(test_games[j].history, 4))

    totals = [0]*num_choices

    for j in range(num_choices):
        for k in range(num_games):
            totals[j] += test_games[k].history[j]

        totals[j] = totals[j]/num_games

    set_averages.append(totals)

    print("set#", i, "\taverages:\t", totals,
          "change:\t", [int(totals[j]-temp[j]) for j in range(num_choices)])
    temp = totals

for i in range(num_sets-1):
    print(set_averages[i])