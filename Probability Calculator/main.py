import copy
import random

# Create a hat that can hold balls of varying types
class Hat:
    def __init__(self, **balls):
        # Store all of the balls inside of the hat
        self.contents = []
        for k, v in balls.items():
            for _ in range(v):
                self.contents.append(k)
    
    # Remove random balls from `contents` and return the removed balls
    def draw(self, num_balls):
        drawn_balls = []
        # If no. of drawn balls > no. balls in `contents`, take all of the balls in `contents`
        if (num_balls >= len(self.contents)):
            drawn_balls = copy.copy(self.contents)
            self.contents.clear()
        # Otherwise draw a number of random balls
        else:
            for _ in range(num_balls):
                rand_ball = random.choice(self.contents)
                drawn_balls.append(rand_ball)
                self.contents.remove(rand_ball)
                
        # Return all of the balls drawn
        return drawn_balls

# Run an experiment to calculate (and return) the approximate probability of a group of balls being found in a draw from a hat
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    # For use with draw()
    hat.original_contents = hat.contents

    # Count times `expected_balls` are found in draw
    times_balls_found = 0

    for _ in range(num_experiments):
        hat.contents = copy.copy(hat.original_contents) # Refresh contents of hat
        drawn = hat.draw(num_balls_drawn) # Draw number of random balls

        # If `expected_balls` found in `drawn_balls`, increment `times_balls_found`
        found_balls = all(drawn.count(ball) >= num 
        for ball, num in expected_balls.items())
        if found_balls:
            times_balls_found += 1
    
    # Calculate probability
    return times_balls_found/num_experiments

# Test groups
if __name__ == '__main__':
  
    #-----------------------------------------------
    hat_one = Hat(black = 6, red = 4, green = 3)
    probability1 = experiment(hat = hat_one,
                    expected_balls = {"red": 2, "green": 1},
                    num_balls_drawn = 4,
                    num_experiments = 2000)
    print(f"Chance of finding 2 red and a green ball in Hat One in a draw of 5: {probability1 * 100}%\n------------")
  
    #-----------------------------------------------
    hat_two = Hat(yellow = 3, blue = 2, green = 6)
    probability2 = experiment(hat = hat_two,
                    expected_balls = {"yellow": 1, "blue": 1, "green": 3},
                    num_balls_drawn = 8,
                    num_experiments = 2000)
    print(f"Chance of finding a yellow, a blue and 3 green balls in Hat Two in a draw of 8: {probability2 * 100}%\n------------")
  
    #-----------------------------------------------
    hat_three = Hat(red = 5, orange = 4)
    probability3 = experiment(hat = hat_three,
                    expected_balls = {"red": 5, "orange": 2},
                    num_balls_drawn = 9,
                    num_experiments = 2000)
    print(f"Chance of finding 5 red and 2 orange balls in Hat Three in a draw of 9 : {probability3 * 100}%\n------------")
  
    #-----------------------------------------------
    hat_four = Hat(red = 5, orange = 4, black = 1, blue = 0, pink = 2, striped = 9)
    probability4 = experiment(hat = hat_four,
                    expected_balls = {"red": 1, "orange": 2, "black": 1, "striped": 3},
                    num_balls_drawn = 13,
                    num_experiments = 2000)
    print(f"Chance of finding a red, 2 orange, a black and 3 striped balls in Hat Four in a draw of 13: {probability4 * 100}%\n------------")
