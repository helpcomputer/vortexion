
def rect_overlap(x1, y1, w1, h1, x2, y2, w2, h2):
    return x1 < x2 + w2 and \
            x1 + w1 > x2 and \
            y1 < y2 + h2 and \
            y1 + h1 > y2

