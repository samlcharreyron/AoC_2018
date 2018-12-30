import sys
from collections import deque

def p1(n): 
    recipes = [3,7]
    elves = [0, 1]
    currents = [0, 1]

    while len(recipes) < n+10:
        L = len(recipes)
        new_recipes = [int(ch) for ch in str(sum(recipes[currents[i]] for i in elves))]
        recipes.extend(new_recipes)
        L = len(recipes)

        for i in elves:
            currents[i] = (currents[i] + recipes[currents[i]] + 1) % L

        #print recipes
        #print currents
    print ''.join(str(i) for i in recipes[-10:])

def p2(n): 
    recipes = '37'
    elves = [0, 1]
    currents = [0, 1]

    while n not in recipes[-7:]:
        L = len(recipes)
        new_recipes = ''.join([str(ch) for ch in str(sum(int(recipes[currents[i]]) for i in elves))])
        recipes += new_recipes
        L = len(recipes)

        for i in elves:
            currents[i] = (currents[i] + int(recipes[currents[i]]) + 1) % L

    print recipes.index(n)
        

if __name__ == '__main__':
    #p1(int(sys.argv[1]))
    p2(sys.argv[1])

