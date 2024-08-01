# The example function below keeps track of the opponent's history and plays whatever the opponent played two plays ago. It is not a very good player so you will need to change the code to pass the challenge.

''' 
Notes 
- Quincy just cycles through "R", "R", "P", "P", "S"
- Mrugesh records your last 10 moves, and plays the counter to the most frequent one that you chose in the last 10
- Kris just plays the counter to your previous move
- Abbey is.... sophisticated
    Abbey takes notes of the order of ALL opponent previous plays
    Then focuses on the opponent last 2 plays, and +1 to that particular event, notes it down that it happened e.g. if last 2 plays is SS, SS gets +1
    It then looks at the opponent previous play
    and compares it against its recorded list of opponent previous plays 
    it looks at the subset of most frequent plays e.g. if opponent previously played S, it looks at its records for SR, SP and SS
    and the most frequent combination  is discovered e.g. SS may have the highest count
        the bot predicts that S will be played next since SS is the highest count
    and Abbey will play the counter to that most frequently played which is R
    ..
    actually doesnt this means Abbey just plays the counter based on opponent previous 2 plays?

    play_order[0] is just to access the dictionary in the list. Since it is a dictionary nested within the list


'''

def player(prev_play, opponent_history=[],
          play_order=[{
              "RR": 0,
              "RP": 0,
              "RS": 0,
              "PR": 0,
              "PP": 0,
              "PS": 0,
              "SR": 0,
              "SP": 0,
              "SS": 0,
          }]):

    if not prev_play:
        prev_play = 'R'

    opponent_history.append(prev_play)

    last_two = "".join(opponent_history[-2:])
    if len(last_two) == 2:
        play_order[0][last_two] += 1


    potential_plays = [prev_play + "R",  prev_play + "P", prev_play + "S"]

    sub_order = {
        k: play_order[0][k]
        for k in potential_plays if k in play_order[0]
    }

    prediction = max(sub_order, key=sub_order.get)[-1:]

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}

    debug_str = f'{last_two=} {prev_play=}, {sub_order=}, {potential_plays=} {prediction=}, {ideal_response[prediction]=}'
    #print(debug_str)

    return ideal_response[prediction]

