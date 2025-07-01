def get_num_words(words):
        return len(words.split())

def get_num_chars(words):
        full_charsnums = {}
        for chars in words.lower():
                if chars in full_charsnums:
                        full_charsnums[chars] += 1
                else:
                        full_charsnums[chars] = 1
        return full_charsnums

def sort_on(item):
    return item["nums"]

def sort_dict(charsnums):
        sorted_dict = []
        for i in charsnums:
            sorted_dict.append({"char": i, "nums": charsnums[i]})
        sorted_dict.sort(reverse=True, key=sort_on)
        return sorted_dict