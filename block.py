# block.py
# Dylan Palmieri
# 9/19/19
# Contains Block parent class


class Block:
    def isCollidable(self):
        return True


class Wall(Block):
    pass


class Paddle(Block):
    pass


class Background(Block):
    def isCollidable(self):
        return False
