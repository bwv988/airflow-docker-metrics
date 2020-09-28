# Random failure simulator app.
# RS27092020

import sys
import time
from random import random

SNOOZE = 1

def main():
    """
    This program will produce a non-zero exit code with p% probability, on average.

    Run: ./random_failure_app.py <p>
    """

    num_params = len(sys.argv)
    if (num_params == 2):
        p = float(sys.argv[1])    
    else:
        # Default: 30% failure rate.
        p = 0.3
    
    print(f"\nI may fail randomly!\n")
   
    # Throw a 10-sided die.
    if (random() <= p):
        sys.exit(-1)
    else:
        time.sleep(SNOOZE)    
        sys.exit(0)

if __name__ == "__main__":
    main()
