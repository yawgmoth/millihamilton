
import os
import sys

def load_gadget(fname):
    if os.path.exists(fname):
        f = open(fname)
        result = ""
        lines = []
        for i, l in enumerate(f):
            if i >= 18:
                lines.append(l[:-1])
        lines[-3] = lines[-3][:-2]
        return "\n".join(lines[:-2])
    print "ERROR: could not find", fname
    sys.exit(-1)
    return ""

HEADER = """
(pingus-level 
  (version 3)
  (head 
    (license "GPLv3+")
    (levelname "%s")
    (description "")
    (author "MILLIHAMILTON")
    (number-of-pingus %d)
    (number-to-save %d)
    (time -1)
    (music "")
    (actions 
      (basher %d)
      (bridger %d)
      (climber 1)
      (digger %d))
    (levelsize %d %d))
  (objects 
    (starfield-background 
      (position 0 0 -1000)
      (small-stars 500)
      (middle-stars 250)
      (large-stars 125))
    (solidcolor-background 
      (position 0 0 -1000)
      (colori 0 0 0 255))
"""


GADGETMAP = {"1": load_gadget("Gadgets/crossoverfixed.pingus"), 
             "0": load_gadget("Gadgets/crossover0.pingus"), 
             "V": load_gadget("Gadgets/vertexfixed.pingus"),
             "*": load_gadget("Gadgets/vertexSpecial.pingus"),
             "L": load_gadget("Gadgets/bottomRightForCrossover.pingus"),
             "!": load_gadget("Gadgets/verticalFall.pingus"),
             "=": load_gadget("Gadgets/horizontalForCrossover.pingus"),
             "-": load_gadget("Gadgets/horizontalForVertexRight.pingus"),
             "|": load_gadget("Gadgets/vertical.pingus"),
             ">": load_gadget("Gadgets/topLeftCorner.pingus"),
             "D": load_gadget("Gadgets/topRightCorner.pingus"),
             "U": load_gadget("Gadgets/bottomLeftCorner.pingus"),
             "<": load_gadget("Gadgets/bottomRightForVertex.pingus"),
             "/": load_gadget("Gadgets/deathtrap.pingus"),
             ".": "", "v": ""}
             