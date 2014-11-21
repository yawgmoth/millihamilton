
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

CROSSOVER = """
(groundpiece 
      (type "transparent")
      (surface 
        (image "groundpieces/transparent/halloween/kirby3")
        (modifier "ROT0"))
      (position 480 240 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 1 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 65 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 31 127 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 32 63 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 215 66 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 479 157 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 480 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 543 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 543 156 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/sweets/chocbloc")
        (modifier "ROT0"))
      (position 417 262 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 170 193 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position -10 258 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 225 96 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 32 0 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 121 40 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 215 1 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 34 321 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 218 454 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 217 517 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 35 513 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 35 450 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 35 385 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 525 296 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 368 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 524 361 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 207 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 97 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 67 397 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 217 583 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 33 590 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 33 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 156 522 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 184 40 0))
"""

GADGETMAP = {"1": CROSSOVER}