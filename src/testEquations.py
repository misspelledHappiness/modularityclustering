from equations import computeModularity

network = {1:[{2:1, 3:1, 4:1}, 1],
           2:[{1:1, 5:1}, 1],
           3:[{1:1, 4:1, 5:1}, 2],
           4:[{1:1, 3:1, 5:1}, 2],
           5:[{2:1, 3:1, 4:1}, 2],
}

if  __name__ == '__main__':
    print(computeModularity(network))