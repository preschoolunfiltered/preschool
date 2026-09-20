"""Which doodles are easy to mistake for each other.

Counting is hardest when a near-twin sits right beside the thing you are
counting - a ladybug next to a bee, a maple leaf next to an oak leaf, two
snails nose to nose. The scatter uses these groups to deliberately park
lookalikes together instead of leaving that to chance.

Only icons that share a theme ever meet, so a group may safely span themes.
"""

from __future__ import annotations

GROUPS: tuple[tuple[str, ...], ...] = (
    # round bodies with little faces
    ("bee", "ladybug", "beetle", "firefly", "snail", "chick"),
    ("ant", "spider", "crab", "beetle", "grasshopper"),
    ("butterfly", "moth", "dragonfly", "bee"),
    # blooms
    ("daisy", "sunflower", "petal", "rose", "blossom_branch"),
    ("tulip", "sprout", "grass_tuft", "wheat_stalk", "carrot"),
    # leaves
    ("maple_leaf", "oak_leaf", "leaf_sprig", "fern", "monstera_leaf",
     "holly", "shamrock", "four_leaf_clover", "palm_tree"),
    # discs
    ("cookie", "donut", "gold_coin", "ornament", "moon_craters", "beach_ball",
     "swim_ring", "planet", "jelly_bean", "collar"),
    # points and spikes
    ("star", "shooting_star", "snowflake", "starfish", "confetti"),
    # hearts
    ("heart", "double_heart", "candy_hearts", "heart_balloon", "balloon",
     "chocolate_box"),
    # eggs and ovals
    ("easter_egg_dots", "easter_egg_stripes", "hatching_egg", "dino_egg",
     "acorn", "pinecone", "jelly_bean", "watermelon_slice"),
    # fruit-ish lumps
    ("pumpkin", "jack_o_lantern", "apple", "strawberry", "pie", "burger"),
    # swimmers
    ("fish", "shark", "dolphin", "whale", "seahorse", "submarine"),
    ("octopus", "jellyfish", "sea_turtle", "clam_pearl", "seashell",
     "conch_shell"),
    # cones and triangles
    ("christmas_tree", "pine_tree", "party_hat", "witch_hat", "candy_corn",
     "mountain", "volcano", "tent", "ice_cream_cone"),
    # spirals
    ("snail", "conch_shell", "rose", "lollipop", "ball_of_yarn", "spider_web"),
    # things you wear
    ("mitten", "garden_glove", "stocking", "rain_boot", "ice_skate",
     "sweater", "raincoat", "beanie_hat", "sun_hat", "santa_hat",
     "leprechaun_hat", "pilgrim_hat", "earmuffs"),
    # things that go
    ("car", "dump_truck", "fire_truck", "school_bus", "tractor", "train",
     "sleigh", "sled", "wheelbarrow", "skateboard", "scooter"),
    # sticks
    ("pencil", "crayon", "candle", "glue_stick", "ruler", "paperclip",
     "marshmallow_stick", "broom", "pitchfork", "hand_fork", "trowel"),
    # domes and arcs
    ("umbrella", "beach_umbrella", "rainbow", "cloud", "bell", "cauldron",
     "sand_bucket", "flower_pot", "hot_cocoa", "lemonade"),
    # furry faces
    ("dog", "cat", "bear", "polar_bear", "fox", "lion", "tiger", "monkey",
     "hamster", "mouse", "bunny", "lamb", "sheep", "squirrel", "reindeer",
     "teddy_bear", "cow", "pig", "hippo", "horse", "zebra"),
    # flappers
    ("bird", "seagull", "duck", "hen", "rooster", "owl", "parrot", "bat",
     "pterodactyl", "penguin"),
    # boxes
    ("gift", "seed_packet", "love_letter", "treasure_chest", "lunchbox",
     "abc_block", "book", "notebook", "chalkboard", "backpack", "map",
     "hay_bale", "gift_bag", "tombstone"),
    # long necks and tails
    ("brontosaurus", "t_rex", "stegosaurus", "triceratops", "giraffe",
     "crocodile", "snake", "worm", "caterpillar", "seaweed", "coral"),
)


def similar_map() -> dict[str, set[str]]:
    out: dict[str, set[str]] = {}
    for group in GROUPS:
        for name in group:
            out.setdefault(name, set()).update(group)
    for name, peers in out.items():
        peers.discard(name)
    return out


SIMILAR = similar_map()
