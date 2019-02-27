from typing import List, Dict, Tuple


def create_profile_dictionary(file_name: str) \
        -> Dict[int, Tuple[str, List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    profile dictionary as defined on Page 2 Functions 1.

    Note, some spacing has been added for human readability.
    
    >>> create_profile_dictionary("profiles.txt")
    {100: ('Mulan', [300, 500], [200, 400]), 
    200: ('Ariel', [100, 500], [500]), 
    300: ('Jasmine', [500], [500, 100]), 
    400: ('Elsa', [100, 500], []), 
    500: ('Belle', [200, 300], [100, 200, 300, 400])}
    """
    opened = open(file_name)
    lol = opened.readlines()
    num = len(lol)
    line = 0
    profiles = {}
    user = 0
    while line <= num:
        if (line + 1) == 0:
            user = user
        elif line % 5 == 0:
            profiles.setdefault(int(lol[line]), ('', [], []))
            user = int(lol[line])
        elif (line - 1) % 5 == 0:
            b = list(profiles[user])
            b[0] = lol[line].replace('\n', '')
            profiles[user] = tuple(b)
        elif (line - 2) % 5 == 0:
            b = list(profiles[user])
            prior = lol[line].split(',')
            if prior[0] == '\n':
                followers = []
            else:
                followers = [int(x) for x in prior]
            b[1] = followers
            profiles[user] = tuple(b)
        elif (line - 3) % 5 == 0:
            b = list(profiles[user])
            prior = lol[line].split(',')
            if prior[0] == '\n':
                following = []
            else:
                following = [int(x) for x in prior]
            b[2] = following
            profiles[user] = tuple(b)
        line += 1
    return profiles


def create_chirp_dictionary(file_name: str) \
        -> Dict[int, Tuple[int, str, List[str], List[int], List[int]]]:
    """
    Opens the file "file_name" in working directory and reads the content into a
    chirp dictionary as defined on Page 2 Functions 2.

    Note, some spacing has been added for human readability.
    
    >>> create_chirp_dictionary("chirps.txt")
    {100000: (
        400, 
        'Does not want to build a %SnowMan %StopAsking',
        ['SnowMan', 'StopAsking'], 
        [100, 200, 300], 
        [400, 500]), 
    100001: (
        200, 
        'Make the ocean great again.', 
        [''], 
        [], 
        [400]), 
    100002: (
        500, 
        "Help I'm being held captive by a beast!  %OhNoes", 
        ['OhNoes'], 
        [400], 
        [100, 200, 300]), 
    100003: (
        500, 
        "Actually nm. This isn't so bad lolz :P %StockholmeSyndrome", 
        ['StockholmeSyndrome'], 
        [400, 100], 
        []), 
    100004: (
        300, 
        'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
        ['ShowYouTheWorld', 'JustSayNo'], 
        [500, 200], 
        [400]), 
    100005: (
        400, 
        'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan', 
        ['StockholmeSyndrome', 'SnowMan'], 
        [], 
        [200, 300, 100, 500])}
    """
    opened = open(file_name)
    lol = opened.readlines()
    num = len(lol)
    line = 0
    chirps = {}
    hash = []
    chirp_id = 0
    while line <= num:
        if line % 7 == 0:
            chirps.setdefault(int(lol[line]), (int, str, List[str], List[int], List[int]))
            chirp_id = int(lol[line])
            b = list(chirps[chirp_id])
        elif (line - 1) % 7 == 0:
            b[0] = int(lol[line])
        elif (line - 2) % 7 == 0:
            b[1] = lol[line].replace('\n', '')
        elif (line - 3) % 7 == 0:
            hash = lol[line].split(',')
            hash[len(hash) - 1] = hash[len(hash) - 1].replace('\n', '')
            b[2] = hash
        elif (line - 4) % 7 == 0:
            prior = lol[line].split(',')
            if prior[0] == '\n':
                likes = []
            else:
                likes = [int(x) for x in prior]
            b[3] = likes
        elif (line - 5) % 7 == 0:
            prior = lol[line].split(',')
            if prior[0] == '\n':
                dislikes = []
            else:
                dislikes = [int(x) for x in prior]
            b[4] = dislikes
        chirps[chirp_id] = tuple(b)
        if (line - 6) % 7 == 0:
            chirp_id = 0
        line += 1
    return chirps


def get_top_chirps( \
        profile_dictionary: Dict[int, Tuple[str, List[int], List[int]]], \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]],
        user_id: int)\
        -> List[str]:
    """
    Returns a list of the most liked chirp for every user user_id follows.
    See Page 3 Function 3 of th .pdf.
    >>> profile_dictionary = create_profile_dictionary("profiles.txt")
    >>> chirp_dictionary   = create_chirp_dictionary("chirps.txt")
    >>> get_top_chirps(profile_dictionary, chirp_dictionary, 300)
    ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"]
    >>> get_top_chirps( profiles, chirps, 500 )
    ['Make the ocean great again.', 
    'If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.', 
    'Does not want to build a %SnowMan %StopAsking']
    """
    followed_u = profile_dictionary[user_id][2]
    current_u_chirps = []
    current_top = -1
    top_chirps = []
    top = None
    for user in followed_u:
        for chirps in chirp_dictionary:
            if chirp_dictionary[chirps][0] == user:
                current_u_chirps.append(chirps)
        for chirps in current_u_chirps:
            if len(chirp_dictionary[chirps][3]) > current_top:
                current_top = len(chirp_dictionary[chirps][3])
                top = chirp_dictionary[chirps][1]
        top_chirps.append(top)
        current_u_chirps = []
    if None in top_chirps:
        top_chirps.remove(None)
    return top_chirps


def create_tag_dictionary( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]]) \
        -> Dict[str, Dict[int, List[str]]]:
    """
    Creates a dictionary that keys tags to tweets that contain them.

    Note, some spacing has been added for human readability.
    
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> create_tag_dictionary(chirp_dictionary)
    {'SnowMan': {
        400: ['Does not want to build a %SnowMan %StopAsking', 'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'StopAsking': {
        400: ['Does not want to build a %SnowMan %StopAsking']}, 
    '': {
        200: ['Make the ocean great again.']}, 
    'OhNoes': {
        500: ["Help I'm being held captive by a beast!  %OhNoes"]}, 
    'StockholmeSyndrome': {
        500: ["Actually nm. This isn't so bad lolz :P %StockholmeSyndrome"], 
        400: ['LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']}, 
    'ShowYouTheWorld': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}, 
    'JustSayNo': {
        300: ['If some random dude offers to %ShowYouTheWorld do yourself a favour and %JustSayNo.']}}
    """
    tags = {}
    for chirp in chirp_dictionary:
        for tag in chirp_dictionary[chirp][2]:
            tags[tag] = {}
    for chirp in chirp_dictionary:
        for tag in chirp_dictionary[chirp][2]:
            user = chirp_dictionary[chirp][0]
            text = chirp_dictionary[chirp][1]
            if tags[tag].get(user, -1) == -1:
                tags[tag][user] = []
                tags[tag][user].append(text)
            else:
                tags[tag][user].append(text)
    return tags


def get_tagged_chirps( \
        chirp_dictionary: Dict[int, Tuple[int, str, List[str], List[int], List[int]]], \
        tag: str) \
        -> List[str]:
    """
    Returns a list of chirps containing specified tag.
    >>> chirp_dictionary = create_chirp_dictionary("chirps.txt")
    >>> get_tagged_chirps(chirp_dictionary, "SnowMan")
    ['Does not want to build a %SnowMan %StopAsking', 
    'LOLZ BELLE.  %StockholmeSyndrome  %SnowMan']
    """
    dic = create_tag_dictionary(chirp_dictionary)
    tagged = []
    for user in dic[tag]:
        tagged += dic[tag][user]
    return tagged




    
