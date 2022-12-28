import pdb

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

print(height)
print(width)

# 30373
# 25512
# 65332
# 33549
# 35390



def visible(row, col, height, width):
    if (row_idx == 0) | (col_idx == 0) | (row_idx == height - 1) | (col_idx == width - 1):
        return True
    else:
        return False





count = 0
for row_idx, row in enumerate(forest):
    for col_idx, tree in enumerate(row):
        tree_taller = True
        if visible(row_idx, col_idx, height, width):
            # print("on the outside")
            count += 1
        else:
            test_row_idx = row_idx            
            # north
            while (test_row_idx > 0) & tree_taller:
                test_row_idx -= 1
                test_tree = forest[test_row_idx][col_idx]
                if tree <= test_tree:
                    tree_taller = False
            if tree_taller:                
                count += 1          
            
            
            # south
            if not tree_taller:                
                # this finds all the trees who have yet to be counted
                # they aren't on the edge and they aren't visible from the north
                test_row_idx = row_idx
                tree_taller = True
                while (test_row_idx < height - 1) & tree_taller:                    
                    test_row_idx += 1
                    test_tree = forest[test_row_idx][col_idx]
                    if tree <= test_tree:
                        tree_taller = False                                        
                if tree_taller:
                    count += 1                          

            # # west
            if not tree_taller:                
                test_col_idx = col_idx                
                tree_taller = True
                while (test_col_idx > 0) & tree_taller:
                    test_col_idx -= 1
                    test_tree = forest[row_idx][test_col_idx]
                    if tree <= test_tree:
                        tree_taller = False
                if tree_taller:       
                    print(row_idx, col_idx, tree)         
                    count += 1
                print("")

            # east
            if not tree_taller:                
                test_col_idx = col_idx                
                tree_taller = True
                while (test_col_idx < width - 1) & tree_taller:
                    test_col_idx += 1
                    test_tree = forest[row_idx][test_col_idx]
                    if tree <= test_tree:
                        tree_taller = False
                if tree_taller:       
                    print(row_idx, col_idx, tree)         
                    count += 1
                print("")


            # east
            # pdb.set_trace()            
            
print(count)

        # for each tree, if it has a 0, then it counts
        # if not, go north by one, if that's lower keep going  until you hit the end or a tree of the same height or higher
        # north


        # 


# for each number, look north, south, east and west until you hit a tree of the same height or higher

# if you make it to the edge, that tree counts
# if you don't, it doesn't





# 3 0 3 7 3     16 (outside)
# 2 5 5 1 2     2 (north)
# 6 5 3 3 2     1 (south)
# 3 3 5 4 9     0 (west)
# 3 5 3 9 0     1 (east)
