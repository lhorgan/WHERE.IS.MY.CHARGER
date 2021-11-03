import random

# ring=charger
# box=compartment
# For some reason, that was easier for me to think about.

# box_count: the number of boxes!
# confidence: how sure you the ring is in the box
def trial(box_count, confidence):
  ring_in_boxes = random.random() < confidence # decide if the ring is in ANY of the boxes
  boxes = [False for x in range(box_count)] # Each box is an entry in this array, and they all start off empty
  boxes[0] = ring_in_boxes # If it turns out there's a ring in one of the boxes, which happens with probability=confidence, then boxes[0]=True
  random.shuffle(boxes) # Shuffle the boxes around so that the box with the ring, if there is one, is in a random spot
  
  # we're taking this really literally.
  # look at each box.
  # if we find the ring before we get to the last box
  # then this trial doesn't match the parameters of the
  # Tweet.  Abort.
  for x in range(len(boxes) - 1):
    if boxes[x] == True:
      return None

  # If there was a ring at all, it was in the last box, as per the Tweet.
  return boxes[-1]

# box_count: the number of boxes!
# confidence: how sure you the ring is in the box
# trials: how many trials to run
def go(box_count=4, confidence=0.8, trials=1000):
  total_trials = 0
  total_valid_trials = 0 # trials where there weren't any rings in any box but potentially the last
  total_successes = 0 # valid trials where the ring was in the last box
  for x in range(trials):
    res = trial(box_count, confidence) # res is None, True, or False
    if res is not None: # None is an "invalid" trial, ie we found the ring before we got to the last box
      total_valid_trials += 1
      if res == True: # Not only was this trial valid, but there was also a ring in the last box.  This is a success.
        total_successes += 1
    total_trials += 1

  if (confidence == 1):
    r = float("inf")
  else:
    r = (confidence / box_count) / (1 - confidence)

  # prediction = 1 - (1 / (((confidence / box_count) / (1 - confidence)) + 1))
  prediction = 1 - (1 / (1 + r))

  # total_successes / total_valid_trials is the approximate solution to the Tweet if box_count=4 and confidence=0.8
  # prediction is the exact solution

  return [total_trials, total_valid_trials, total_successes, total_successes / total_valid_trials, prediction]

# usage:

# $ python3
# >> import prob as p
# >> p.go(4, 0.8, 100)
# [100, 38, 18, 0.47368421052631576, 0.5]
# >> p.go(70, 0.99, 100000)
# [100000, 2449, 1423, 0.5810534912209064, 0.5857988165680471]
# >> p.go(4, 1, 100)
# [1000, 242, 242, 1.0, 1.0]