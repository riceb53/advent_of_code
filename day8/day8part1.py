import pdb

f = open('day8inputtest.txt','r')
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
            # go north.
            while (test_row_idx > 0) & tree_taller:
                test_row_idx -= 1
                test_tree = forest[test_row_idx][col_idx]
                if tree <= test_tree:
                    tree_taller = False
                # print(row_idx, col_idx, tree)
                # print(test_row_idx, col_idx, forest[test_row_idx][col_idx])
                # print("")
            if tree_taller:
                # print("tree taller")
                # print(row_idx, col_idx, tree)
                count += 1          
            else:
                pass
                # print("tree not taller")
                # print(row_idx, col_idx, tree)
            
            
            # print("starting southward test!")
            # print(row_idx, col_idx, tree)
            if not tree_taller:                
                # this finds all the trees who have yet to be counted
                # they aren't on the edge and they aren't visible from the north
                # print("test")
                print(row_idx, col_idx, tree)
                # pdb.set_trace()

                # should print out
                # 1 3 1
                    # test should be
                        # 2 3 3                        
                        # fail
                # 2 1 5
                    # test should be
                        # 3 1 3
                        # 4 1 5
                        # fail
                # 2 2 3
                    # test should be
                        # 3 2 5
                        # fail                        
                # 2 3 3
                    # test should be 
                        # 3 3 4
                        # fail
                # 3 1 3
                    # test should be 
                        # 4 1 5
                        # fail
                # 3 2 5
                    # test should be
                        # 4 2 5
                        # pass
                # 3 3 4
                    # test should be
                        # 4 3 9
                        # fail



                test_row_idx = row_idx
                tree_taller = True
                while (test_row_idx < height - 1) & tree_taller:                    
                    print("test_row_idx")
                    print(test_row_idx)
                    test_row_idx += 1
                    test_tree = forest[test_row_idx][col_idx]
                    if tree <= test_tree:
                        tree_taller = False
                    print(row_idx, col_idx, tree)
                    print(test_row_idx, col_idx, forest[test_row_idx][col_idx])
                    if (test_row_idx == 4) & (col_idx == 2):
                        pdb.set_trace()
                if tree_taller:
                    print("tree taller")
                    print(row_idx, col_idx, tree)
                    count += 1          
                else:                    
                    print("tree not taller")
                    print(row_idx, col_idx, tree)
                print("")

                # go east
            # pdb.set_trace()            
            
print(count)

        # for each tree, if it has a 0, then it counts
        # if not, go north by one, if that's lower keep going  until you hit the end or a tree of the same height or higher
        # north


        # 


# for each number, look north, south, east and west until you hit a tree of the same height or higher

# if you make it to the edge, that tree counts
# if you don't, it doesn't


