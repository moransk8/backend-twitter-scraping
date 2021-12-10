import twint


def test(search, limit, username):
    c = twint.Config()
    c.Lang = "es"
    if search:
        print("search")
        c.Search = search
    c.Limit = limit
    if username:
        print("username")
        c.Username = "elonmusk"
    # c.Store_object = True
    # twint.run.Search(c)
    # tw_list = twint.output.tweets_list
    tw_list = []
    return tw_list


if __name__ == '__main__':
    rs_list = test([], 20, "")
    print(len(rs_list))
    for x in range(len(rs_list)):
        print(rs_list[x])

