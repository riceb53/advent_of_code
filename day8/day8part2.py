import pdb
import copy

f = open('day8input.txt','r')
lines = f.read().split("\n")

forest = []
for line in lines:    
    trees = []
    for tree in line:
        trees.append(int(tree))
    forest.append(trees)

height = len(forest)
width = len(forest[0])

# print(height)
# print(width)


# for each tree, find the height score (north * south * east * west visibility)
# all trees on the edge have 0 height score



# 30373
# 25512
# 65332
# 33549
# 35390



def edge(row, col, height, width):
    if (row_idx == 0) | (col_idx == 0) | (row_idx == height - 1) | (col_idx == width - 1):
        return True
    else:
        return False



highest_tree_score = 0
tree_score = 0
count = 0
forest_score = copy.deepcopy(forest)

# print(forest)

for row_idx, row in enumerate(forest):
    for col_idx, tree in enumerate(row):        
        tree_taller = True
        if edge(row_idx, col_idx, height, width):
            # print("on the outside")
            tree_score = 0            
            forest_score[row_idx][col_idx] = tree_score
            continue
            count += 1
        else:
            north_score = 0
            # start with tree, 
            # go north,
            # calculate tree score
            # add to north score
            test_row_idx = row_idx       
            # north
            while (test_row_idx > 0) & tree_taller:
                north_score += 1
                test_row_idx -= 1
                test_tree = forest[test_row_idx][col_idx]
                if tree <= test_tree:
                    tree_taller = False
            if tree_taller:                
                count += 1          
            
            
            
            # south
            # 1,2,1
            # 2,1,1
            # 1,1,1
            south_score = 0
            test_row_idx = row_idx
            tree_taller = True
            while (test_row_idx < height - 1) & tree_taller:     
                south_score += 1               
                test_row_idx += 1
                test_tree = forest[test_row_idx][col_idx]
                if tree <= test_tree:
                    tree_taller = False                                        
            if tree_taller:
                count += 1   

                                

            # # west

            west_score = 0       
            test_col_idx = col_idx                
            tree_taller = True
            while (test_col_idx > 0) & tree_taller:
                west_score += 1
                test_col_idx -= 1
                test_tree = forest[row_idx][test_col_idx]
                # if [row_idx, col_idx, tree] == [1,2,5]:
                if tree <= test_tree:    
                    # print()                
                    tree_taller = False
            if tree_taller:       
                # print(row_idx, col_idx, tree)         
                count += 1
            # print("")

            # 1,1,1
            # 1,1,1
            # 1,2,1

            # east
            east_score = 0
            test_col_idx = col_idx                
            tree_taller = True
            while (test_col_idx < width - 1) & tree_taller:                
                east_score += 1
                test_col_idx += 1
                test_tree = forest[row_idx][test_col_idx]
                if tree <= test_tree:
                    tree_taller = False
            if tree_taller:       
                # print(row_idx, col_idx, tree)         
                count += 1
            # print("")

            # print("east_score")
            # print(row_idx, col_idx, tree)         
            
            # print(east_score)
            tree_score = north_score * south_score * east_score * west_score
            if tree_score > highest_tree_score:
                highest_tree_score = tree_score            
            forest_score[row_idx][col_idx] = tree_score

            # 1,2,1
            # 3,1,1
            # 1,2,1


            # east
            
print(forest_score)
print(highest_tree_score)

        # for each tree, if it has a 0, then it counts
        # if not, go north by one, if that's lower keep going  until you hit the end or a tree of the same height or higher
        # north


        # 


# for each number, look north, south, east and west until you hit a tree of the same height or higher

# if you make it to the edge, that tree counts
# if you don't, it doesn't





# 3   0   3   7   3     16 (outside)
# 2   5(1)5(4)1(1)2     2 (north)
# 6   5(6)3(1)3(2)2     1 (south)
# 3   3(1)5(8)4(3)9     0 (west)
# 3   5   3   9   0     1 (east)


