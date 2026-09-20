"""Theme definitions: title, the icons that appear, and cover art."""

from __future__ import annotations

from dataclasses import dataclass, field


@dataclass(frozen=True)
class Theme:
    key: str
    title: str
    eyebrow: str
    subtitle: str
    icons: tuple[str, ...]
    cover_icons: tuple[str, ...] = field(default=())

    @property
    def cover(self) -> tuple[str, ...]:
        return self.cover_icons or self.icons[:10]


def _t(key, title, subtitle, icons, eyebrow="I SPY", cover=()):
    return Theme(key, title, eyebrow, subtitle, tuple(icons), tuple(cover))


THEMES: list[Theme] = [
    _t("spring", "SPRING", "Count the signs of spring", [
        "tulip", "daisy", "blossom_branch", "seed_packet", "watering_can",
        "flower_pot", "sun_hat", "sprout", "trowel", "snail", "ladybug",
        "bee", "butterfly", "worm", "birds_nest", "rainbow", "umbrella",
        "rain_boot"]),
    _t("summer", "SUMMER", "A sunny day at the beach", [
        "beach_ball", "ice_cream_cone", "popsicle", "sunglasses", "flip_flop",
        "sandcastle", "surfboard", "beach_umbrella", "watermelon_slice",
        "lemonade", "pineapple", "palm_tree", "kite", "swim_ring",
        "sand_bucket", "sailboat", "seagull", "sun"]),
    _t("fall", "FALL", "Cozy autumn counting fun", [
        "acorn", "pumpkin", "maple_leaf", "oak_leaf", "apple", "corn",
        "sunflower", "hay_bale", "mushroom", "squirrel", "owl", "pinecone",
        "sweater", "wheelbarrow", "pie", "hot_cocoa", "fox", "rain_boot"]),
    _t("winter", "WINTER", "Snow day search and count", [
        "snowflake", "snowman", "mitten", "beanie_hat", "scarf", "sled",
        "ice_skate", "penguin", "polar_bear", "icicles", "earmuffs",
        "pine_tree", "skis", "hot_cocoa", "cloud", "bird", "sweater",
        "mountain"]),
    _t("christmas", "CHRISTMAS", "Merry counting and finding", [
        "christmas_tree", "gift", "candy_cane", "stocking", "santa_hat",
        "reindeer", "bell", "wreath", "gingerbread_man", "ornament", "sleigh",
        "snow_globe", "holly", "string_lights", "santa_face", "cookie",
        "snowflake", "star"]),
    _t("halloween", "HALLOWEEN", "Spooky but not too scary", [
        "jack_o_lantern", "ghost", "bat", "spider", "spider_web", "candy_corn",
        "witch_hat", "cauldron", "black_cat", "skull", "broom", "wrapped_candy",
        "tombstone", "crescent_moon", "mummy", "potion_bottle", "owl",
        "star"]),
    _t("thanksgiving", "THANKSGIVING", "Gather round and count", [
        "turkey", "pumpkin", "pie", "corn", "wheat_stalk", "pilgrim_hat",
        "apple", "acorn", "maple_leaf", "oak_leaf", "hay_bale", "sunflower",
        "hot_cocoa", "squirrel", "fox", "owl", "mushroom", "pinecone"]),
    _t("valentine", "VALENTINE", "Sweet hearts to hunt for", [
        "heart", "double_heart", "love_letter", "cupcake", "rose",
        "teddy_bear", "chocolate_box", "cupid_arrow", "heart_balloon",
        "lollipop", "heart_banner", "candy_hearts", "cookie", "donut", "gift",
        "star", "butterfly", "ladybug"]),
    _t("easter", "EASTER", "Hop to it and count", [
        "easter_egg_stripes", "easter_egg_dots", "hatching_egg", "bunny",
        "easter_basket", "carrot", "lamb", "jelly_bean", "chick", "tulip",
        "daisy", "butterfly", "birds_nest", "rainbow", "sun", "bee",
        "blossom_branch", "sprout"]),
    _t("stpatrick", "ST. PATRICK'S", "Lucky finds and counts", [
        "shamrock", "four_leaf_clover", "pot_of_gold", "horseshoe",
        "leprechaun_hat", "gold_coin", "lucky_coin_bag", "rainbow", "cloud",
        "star", "heart", "sun", "leaf_sprig", "bird", "butterfly", "mushroom",
        "snail", "grass_tuft"]),
    _t("ocean", "OCEAN", "Dive in and count", [
        "fish", "whale", "dolphin", "octopus", "jellyfish", "sea_turtle",
        "seahorse", "crab", "starfish", "seashell", "conch_shell", "coral",
        "anchor", "treasure_chest", "submarine", "bubbles", "seaweed",
        "shark"]),
    _t("space", "SPACE", "Blast off and count", [
        "rocket", "planet", "star", "shooting_star", "astronaut", "ufo",
        "moon_craters", "satellite", "comet", "telescope", "alien",
        "space_helmet", "crescent_moon", "sun", "bubbles"]),
    _t("farm", "FARM", "Down on the farm", [
        "barn", "cow", "pig", "hen", "sheep", "horse", "tractor", "duck",
        "fence", "milk_bottle", "rooster", "pitchfork", "silo", "egg_basket",
        "hay_bale", "corn", "sunflower", "wheelbarrow"]),
    _t("dinosaur", "DINOSAURS", "Roar and count", [
        "t_rex", "stegosaurus", "brontosaurus", "triceratops", "pterodactyl",
        "dino_egg", "volcano", "fern", "dino_footprint", "bone",
        "fossil_skull", "palm_tree", "mountain", "leaf_sprig", "grass_tuft"]),
    _t("jungle", "JUNGLE", "Safari counting adventure", [
        "lion", "monkey", "elephant", "giraffe", "zebra", "tiger", "snake",
        "parrot", "banana", "hippo", "crocodile", "monstera_leaf", "paw_print",
        "palm_tree", "butterfly", "bird", "fern", "sun"]),
    _t("school", "SCHOOL", "Back to school counting", [
        "pencil", "crayon", "book", "backpack", "ruler", "scissors",
        "glue_stick", "notebook", "globe", "school_bus", "abc_block",
        "paint_palette", "chalkboard", "paperclip", "lunchbox", "apple",
        "star", "heart"]),
    _t("transport", "THINGS THAT GO", "Wheels, wings and waves", [
        "car", "train", "airplane", "bicycle", "dump_truck", "helicopter",
        "hot_air_balloon", "fire_truck", "scooter", "traffic_light",
        "skateboard", "school_bus", "sailboat", "submarine", "rocket",
        "tractor", "canoe", "kite"]),
    _t("camping", "CAMPING", "Out in the great outdoors", [
        "tent", "campfire", "marshmallow_stick", "compass", "lantern",
        "canoe", "fishing_rod", "binoculars", "map", "flashlight", "mountain",
        "bear", "smore", "log", "pine_tree", "owl", "fish", "backpack"]),
    _t("birthday", "BIRTHDAY", "Party time counting", [
        "birthday_cake", "party_hat", "balloon", "candle", "confetti",
        "bunting", "donut", "party_popper", "gift_bag", "gift", "cupcake",
        "lollipop", "cookie", "ice_cream_cone", "star", "heart",
        "wrapped_candy", "double_heart"]),
    _t("bugs", "BUGS", "Creepy crawly counting", [
        "ant", "caterpillar", "dragonfly", "grasshopper", "beetle", "firefly",
        "moth", "honeycomb", "magnifying_glass", "ladybug", "bee", "butterfly",
        "snail", "worm", "spider", "leaf_sprig", "grass_tuft", "daisy"]),
    _t("pets", "PETS", "Furry friends to find", [
        "dog", "cat", "fish_bowl", "bird_cage", "ball_of_yarn", "hamster",
        "pet_bowl", "dog_house", "collar", "mouse", "bone", "paw_print",
        "heart", "bunny", "bird", "fish", "sea_turtle", "duck"]),
    _t("food", "YUMMY FOOD", "Snack time counting", [
        "pizza_slice", "burger", "hot_dog", "taco", "strawberry", "grapes",
        "cheese", "broccoli", "apple", "banana", "carrot", "watermelon_slice",
        "cookie", "donut", "cupcake", "ice_cream_cone", "milk_bottle",
        "corn"]),
]

BY_KEY = {t.key: t for t in THEMES}
