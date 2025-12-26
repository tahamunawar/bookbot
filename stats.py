def get_num_words(text):
    return len(text.split())

def get_character_count(text):
    ans = {}
    for c in text.lower():
        if c in ans:
            ans[c] += 1
        else:
            ans[c] = 1
    return ans

def get_sorted_dict(dic):
    return dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))

