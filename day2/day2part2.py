# part 2
  # X means lose
  # Y means draw
  # Z means win


# split into me vs them
# based on their choice pick your choice
# then add up the score

outcomes = {
  'X': {
    'A': 'C',
    'B': 'A',
    'C': 'B',
  },
  'Y': {
    'A': 'A',
    'B': 'B',
    'C': 'C',
  },
  'Z': {
    'A': 'B',
    'B': 'C',
    'C': 'A',
  }
}



outcome_points = {
  'X': 0,
  'Y': 3,
  'Z': 6
}

selection_points = {
  'A': 1,
  'B': 2,
  'C': 3,
}

f = open('day2input.txt','r')
lines = f.read().split("\n")



total_points = 0
for line in lines:
    opponent_selection = line.split(" ")[0]
    outcome = line.split(" ")[1]
    my_selection = outcomes[outcome][opponent_selection]
    total_points += selection_points[my_selection]
    total_points += outcome_points[outcome] 

print(total_points)   


# print(total_points)