# You are visiting a farm that has a single row of fruit trees arranged from left to right. The trees are represented by an integer array fruits where fruits[i] is the type of fruit the ith tree produces.

# You want to collect as much fruit as possible. However, the owner has some strict rules that you must follow:

# You only have two baskets, and each basket can only hold a single type of fruit. There is no limit on the amount of fruit each basket can hold.
# Starting from any tree of your choice, you must pick exactly one fruit from every tree (including the start tree) while moving to the right. The picked fruits must fit in one of your baskets.
# Once you reach a tree with fruit that cannot fit in your baskets, you must stop.
# Given the integer array fruits, return the maximum number of fruits you can pick.

def totalFruit(fruits):
    start = 0
    end = 0
    maxFruits = 0
    fruitTypes = {}

    for end in range(len(fruits)):
        if ((len(fruitTypes)<2) and (fruits[end] not in fruitTypes)):
            fruitTypes[fruits[end]] = True
            maxFruits = max(maxFruits, (end - start +1))
        elif (fruits[end] in fruitTypes):
            maxFruits = max(maxFruits, (end-start+1))
        else:
            fruitTypes = {}
            fruitTypes[fruits[end-1]]=True
            fruitTypes[fruits[end]]=True
            start = end - 1

            while fruits[start] == fruits[start-1]:
                start -= 1

            maxFruits = max(maxFruits, (end-start+1))
        
    return maxFruits

fruits = [0,1,2,2]

print(totalFruit(fruits))