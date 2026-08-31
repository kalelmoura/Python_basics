import os, random, time, sys

TOP    = '▀'
BOTTOM = '▄'
FULL   = '█'

# Set the snowstorm density to the command line argument:
DENSITY = 4  # Default snow density is 4%
if len(sys.argv) > 1:
    DENSITY = int(sys.argv[1])

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

while True:
    clear()  # Clear the terminal window.

    # Loop over each row and column:
    for y in range(20):
        for x in range(40):
            # 4% because if the random number is 4 then it won't print snow
            if random.randint(0, 99) < DENSITY:
                # Print snow:
                print(random.choice([TOP, BOTTOM]), end='')
            else:
                # Print empty space:
                print(' ', end='')
        print()  # Print a newline.

    # Print the snow covered ground:
    print(FULL * 40 + '\n' + FULL * 40)
    print('(Ctrl-C to stop.)')

    time.sleep(0.2)  # Pause for a bit.