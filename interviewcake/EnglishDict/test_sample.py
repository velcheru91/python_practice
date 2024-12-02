from math import floor
def find_rotation_idx_binary_search(words):
    # searching for minimum value in a rotated list using binary search
    # O(log n)
    first = int(0)
    last = int(len(words)-1)
    while words[int(first)] > words[int(last)]:
        middle = (first + last) / 2
        if words[int(middle)] > words[int(last)]:
            first = middle + 1
        else:
            last = middle
    return floor(first)

c_level_words = [
        # Q
        "Quaint", "Quake", "Quarrel", "Quench", "Query", "Quest", "Quibble", "Quick", "Quiet", "Quiver",
        # R
        "Radiant", "Ramble", "Rancor", "Ravenous", "Rebel", "Recline", "Rejoice", "Relent", "Remorse", "Resolve",
        # S
        "Sage", "Salvage", "Savor", "Scorn", "Secure", "Serene", "Shimmer", "Shrill", "Solemn", "Strive",
        # T
        "Tactful", "Tangle", "Temper", "Tender", "Thrift", "Thwart", "Timid", "Toil", "Tranquil", "Trepid",
        # U
        "Uncover", "Unify", "Unique", "Uplift", "Uproot", "Urbane", "Urgent", "Usher", "Utter", "Utopia",
        # V
        "Vacate", "Vague", "Valiant", "Valuable", "Vanquish", "Venture", "Verge", "Vex", "Vibrate", "Victory",
        # W
        "Wager", "Wander", "Wary", "Weary", "Whim", "Wield", "Willing", "Wisdom", "Wistful", "Witty",
        # X
        "Xenial", "Xerox", "Xylophone", "Xenophobia", "Xenon", "Xenic", "Xenopus", "Xiphoid", "Xylem", "Xylograph",
        # Y
        "Yearn", "Yield", "Yonder", "Youthful", "Yell", "Yoke", "Yawn", "Yelp", "Yucky", "Yuletide",
        # Z
        "Zeal", "Zealous", "Zenith", "Zest", "Zigzag", "Zinc", "Zonal", "Zoology", "Zoom", "Zestful"
        # A
        "Abate", "Abide", "Abode", "Abroad", "Absurd", "Accord", "Accuse", "Achieve", "Acquire", "Adept",
        # B
        "Babble", "Balmy", "Banish", "Bargain", "Barrier", "Beacon", "Befall", "Beget", "Belief", "Beneath",
        # C
        "Candid", "Canopy", "Captive", "Carefree", "Caution", "Cease", "Census", "Censure", "Chafe", "Chide",
        # D
        "Dabble", "Dainty", "Daring", "Dazzle", "Dealt", "Decay", "Decipher", "Decline", "Deduce", "Defiant",
        # E
        "Earnest", "Ebb", "Eclipse", "Eerie", "Effort", "Elate", "Elude", "Embrace", "Employ", "Endure",
        # F
        "Faint", "Faith", "Falter", "Famine", "Fatal", "Feeble", "Fervent", "Flare", "Fleeting", "Flourish",
        # G
        "Gallant", "Gamble", "Garner", "Gasp", "Gauge", "Generous", "Gentle", "Giddy", "Glare", "Gleam",
        # H
        "Hasten", "Havoc", "Hearty", "Hinder", "Hoist", "Honor", "Humble", "Humor", "Hustle", "Hybrid",
        # I
        "Idle", "Ignite", "Illume", "Impart", "Implore", "Impulse", "Induce", "Inflict", "Inhale", "Inquire",
        # J
        "Jaded", "Jagged", "Jeopardy", "Jester", "Jingle", "Jitter", "Jovial", "Jubilant", "Judicious", "Juggle",
        # K
        "Keen", "Keeper", "Kindle", "Kingdom", "Kinship", "Knit", "Knotty", "Kudos", "Keenly", "Kindred",
        # L
        "Lament", "Lattice", "Linger", "Lofty", "Loom", "Lustrous", "Lurk", "Lush", "Loyal", "Lucid",
        # M
        "Magnify", "Majesty", "Marvel", "Meddle", "Melancholy", "Mellow", "Mend", "Merit", "Mingle", "Misery",
        # N
        "Narrate", "Navigate", "Neglect", "Nimble", "Noble", "Nomad", "Notable", "Notify", "Nourish", "Nurture",
        # O
        "Obey", "Oblige", "Obscure", "Observe", "Obtain", "Occupy", "Offset", "Omit", "Oppose", "Outlast",
        # P
        "Pacify", "Paragon", "Passion", "Pensive", "Peril", "Persist", "Pinnacle", "Placid", "Plight", "Prosper",
    ]
words = ['ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist', 'asymptote', 'babka', 'banoffee',
             'engender', 'karpatka', 'othellolagkage']
correct_words = ['asymptote', 'babka', 'banoffee', 'engender', 'karpatka', 'othellolagkage','ptolemaic', 'retrograde', 'supplant', 'undulate', 'xenoepist']

def test_answer():
    assert find_rotation_idx_binary_search(words) == 5
    assert find_rotation_idx_binary_search(c_level_words) == 100
