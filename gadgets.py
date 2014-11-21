
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
      (position 493 240 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 0 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 78 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 44 127 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 45 63 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 228 66 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 492 157 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 493 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 556 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 556 156 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/sweets/chocbloc")
        (modifier "ROT0"))
      (position 430 262 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 183 193 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position -17 258 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 238 96 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 45 0 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 134 40 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 228 1 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 47 321 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 231 454 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 230 517 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 513 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 450 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 385 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 538 296 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 381 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 537 361 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 220 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 110 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 80 397 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 230 583 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 47 586 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 46 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 169 497 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 197 40 0))
"""

CROSSOVER0 = """
(groundpiece 
      (type "transparent")
      (surface 
        (image "groundpieces/transparent/halloween/kirby3")
        (modifier "ROT0"))
      (position 493 240 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 0 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 78 159 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 44 127 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 45 63 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 228 66 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 492 157 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 493 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 556 263 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 556 156 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 183 193 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position -17 258 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel5")
        (modifier "ROT0"))
      (position 238 96 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 45 0 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 134 40 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 228 1 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 47 321 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 231 454 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 230 517 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 513 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 450 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 48 385 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 538 296 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 381 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 537 361 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 220 408 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 110 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 80 397 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 230 583 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT90"))
      (position 47 586 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 46 576 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 169 497 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/rectsolid")
        (modifier "ROT0"))
      (position 197 40 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/squaresolid")
        (modifier "ROT0"))
      (position 431 262 0))
"""

VERTEX = """
(groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 50 142 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 205 142 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 361 143 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 281 25 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 504 142 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 1072 604 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 653 591 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 4 605 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 167 606 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 279 605 0))
    (prefab 
      (name "prefabs/entrances/desert")
      (position 1082 174 0)
      (overrides 
        (release-rate 50)
        (direction "misc")
        (owner-id 0)))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 1156 191 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 995 253 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block2")
        (modifier "ROT0"))
      (position 938 189 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block2")
        (modifier "ROT0"))
      (position 938 125 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 877 326 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 878 293 0))
    (liquid 
      (surface 
        (image "liquids/lava")
        (modifier "ROT0"))
      (position 670 527 0)
      (speed 0)
      (repeat 1))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block2")
        (modifier "ROT0"))
      (position 671 204 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 655 425 0))
    (exit 
      (surface 
        (image "exits/ice2")
        (modifier "ROT0"))
      (position 288 605 0)
      (owner-id 0))
    (liquid 
      (surface 
        (image "liquids/lava")
        (modifier "ROT0"))
      (position 733 527 0)
      (speed 0)
      (repeat 1))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block3")
        (modifier "ROT0"))
      (position 596 429 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 654 462 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel4")
        (modifier "ROT0"))
      (position 433 544 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 431 426 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 3 -2 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block2")
        (modifier "ROT0"))
      (position 671 140 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel1")
        (modifier "ROT0"))
      (position 721 78 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel1")
        (modifier "ROT0"))
      (position 923 253 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 878 444 0))
    (liquid 
      (surface 
        (image "liquids/lava")
        (modifier "ROT0"))
      (position 860 528 0)
      (speed 0)
      (repeat 1))
    (liquid 
      (surface 
        (image "liquids/lava")
        (modifier "ROT0"))
      (position 795 527 0)
      (speed 0)
      (repeat 1))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 810 592 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 6 445 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel1")
        (modifier "ROT0"))
      (position 654 333 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 622 181 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 113 388 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position -3 388 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 793 78 0))
    (groundpiece 
      (type "ground")
      (surface 
        (image "groundpieces/ground/snow/block2")
        (modifier "ROT0"))
      (position 671 77 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 627 -1 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 787 118 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/crystal/smallsolid")
        (modifier "ROT0"))
      (position 428 394 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel3")
        (modifier "ROT0"))
      (position 950 78 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel1")
        (modifier "ROT0"))
      (position 1110 78 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel2")
        (modifier "ROT0"))
      (position 1156 78 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel4")
        (modifier "ROT180FLIP"))
      (position 208 335 0))
    (groundpiece 
      (type "solid")
      (surface 
        (image "groundpieces/solid/industrial/steel4")
        (modifier "ROT180FLIP"))
      (position -4 277 0))
"""

GADGETMAP = {"1": CROSSOVER, "0": CROSSOVER0, "V": VERTEX}