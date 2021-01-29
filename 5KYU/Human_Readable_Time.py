def make_readable(seconds):
    return "{hou:02d}:{min:02d}:{sec:02d}".format(hou=seconds//3600, min=(seconds%3600)//60, sec=(seconds%3600)%60)