# left side
  # a rock
  # b paper
  # c scissors

# right side
  # x rock
  # y paper
  # z scissors

# calculate points
  # 1 for X (rock)
  # 2 for Y (paper)
  # 3 for Z (scissors)

  # 0 for loss
  # 3 for tie
  # 6 for win

# part 2
  # X means lose
  # Y means draw
  # Z means win


outcome_points = {
  'A X': 3,
  'A Y': 6,
  'A Z': 0,
  'B X': 0,
  'B Y': 3,
  'B Z': 6,
  'C X': 6,
  'C Y': 0,
  'C Z': 3,
}

selection_points = {
  'X': 1,
  'Y': 2,
  'Z': 3,
}



f = open('day2input.txt','r')
lines = f.read().split("\n")



total_points = 0
for line in lines:
  total_points += outcome_points[line]
  total_points += selection_points[line[-1]]

print(total_points)