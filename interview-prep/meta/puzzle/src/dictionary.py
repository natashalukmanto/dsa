class Dictionary:
    @staticmethod
    def get_test_dictionary():
        return {
            "abet", "abey", "able", "ably", "abut", "ache", "achy", "acid", "acne", "adze",
            "ajar", "akin", "alit", "alms", "aloe", "also", "alum", "amen", "amid", "amok",
            "anew", "ankh", "ante", "apse", "aqua", "arch", "area", "aria", "arms",
            "army", "arid", "ashy", "atom", "atop", "avow", "avid", "away", "axle", "axon",
            "easy", "hard", "dock", "drop", "dome", "doff",
            "dodo", "mota", "oog", "dog", "aab", "aac"
        }

    @staticmethod
    def get_prod_dictionary():
        return Dictionary.read_file_dictionary("data/up_to_six_letters.txt")

    @staticmethod
    def read_file_dictionary(filepath):
        dict_set = set()
        try:
            with open(filepath, "r") as f:
                for line in f:
                    dict_set.add(line.strip())
        except Exception as e:
            print(f"Error reading dictionary file: {e}")
        return dict_set
