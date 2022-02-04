import collections
with open("maze.txt") as maze:
    maz = []
    objects = collections.defaultdict(list)
    for i in maze:
        line = []
        for o in i.strip():
            line.append(o)
        maz.append(line)
    for block in maz:
        for lett in block:
            pos = (block.index(lett), maz.index(block), lett)
            objects[lett] += pos
    print(objects)
