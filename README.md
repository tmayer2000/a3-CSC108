# a3-CSC108
this program takes in a file of the form seen in profiles.txt and chirp.txt. It then creates a dictionary of users where the key is the user's profile id and the value is a tuple -> (user_name, list[followers], list[following]). Also users can create chirps (think tweets from twitter), and can also make a dictionary of chirps. the chirp dictionary has a chirp_id as a key and the value is a tuple -> (user_id, "chirp_str", list[chirp_tags], list[users_id_who_liked], list[users_id_who_disliked]). The following functions can be called




1. create_profile_dictionary(str) -> profiles_dictionary
  The input parameter is the name of a text file containing all of Chirper's profile information.
  You may assume the file is in the same directory as assignment3.py. The le is a series of
  profile data, where data for each profile has the following format:
  USERID
  USERNAME
  FOLLOWER1, FOLLOWER2, ..., FOLLOWERn
  FOLLOWED1, FOLLOWED2, ..., FOLLOWEDm
  where USERID, FOLLOWERi, and FOLLOWEDj are all unique numbers. The third line represents
  the users which follow USERNAME, and the forth line represents the users which USERNAME fol-
  lows. In the text file there is always a blank-line between different profiles. See profiles.txt
  as an example.
  Based on this data, the function constructs a profiles_dictionary where the orders of the
  ids representing followers and users follows, are the same orders as which they appear in the
  text file. See the doctstring and profiles.txt for further clarification. Assume that the given
  text file is perfect and that there are no formatting errors.
2. create_chirp_dictionary(str) -> chirp_dictionary
  The input parameter is the name of a text file containing all of Chirper's message information.
  You may assume the file is in the same directory as the as assignment3.py. The file is a series
  of message data, where data for each message has the following format:
  CHIRPID
  USERID
  MESSAGE
  TAG1, TAG2, ..., TAGk
  LIKED1, LIKED2, ..., LIKEDn
  DISLIKED1, DISLIKED2, ..., DISLIKEDm
  where CHIRPID, USERID, LIKEDi, and DISLIKEDj are all unique numbers. USERID is the id of
  the user which made the chirp. The third line is the chirp itself. The forth line represents a
  list of tags associated with said chirp. The fifth line is a sequence of user ids which liked the
  chirp. The sixth line is a sequence of user ids which disliked the chirp. In the text file there is
  always a blank-line between different chirps. See chirps.txt as an example.
  Based on this data, the function constructs a profiles_dictionary where the orders of the
  tags and ids representing likes and dislikes, are in the same orders in which they appear in the
  text file. If there are no tags associated with a chirp, the empty string is associated with it
  instead. See the doctstring and chirps.txt for further clarification. Assume that the given
  text file is perfect and that there are no formatting errors.
3. get_top_chirps(profile_dictionary, chirp_dictionary, int) -> List[str]
  The third parameter is a user id which is in the given profile_dictionary. Let the user with
  this user id be denoted by u. The function uses the data from the first two parameters to nd
  the chirp with the most likes for each user followed by u. The function creates a list of these
  chirps and returns it. You may assume:
  (a) For a given user, there does not exist any two chirps with the same number of likes.
  (b) The order of the chirps in the returned list is arbitrary. As long as all the correct chirps
  are present and no incorrect chirps are present, the function is correct.
  See the docstring for examples.
4. create_tag_dictionary(chirp_dictionary) -> Dict[str, Dict[int, List[str]]]
  Takes in a chirp_dictionary and creates a new dictionary. In the new dictionary, tags are
  keys, the values are dictionaries where the keys in these dictionaries are user ids, and the
  values of these dictionaries are chirps made by the corresponding user, which also had the
  corresponding tag. See the docstring for examples.
5. get_tagged_chirps(chirp_dictionary, str) -> List[str]
  Takes in a chirp_dictionary and a tag, and returns a list which contains a list of all the
  chirps which had said tag on them. The order of the returned list is arbitary, as long as all
  the correct chirps are present and no incorrect chirps are present, the function is correct. See
  the docstring for examples.
