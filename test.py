import twint


def test():
    search = "hola"
    limit = 20
    username = ""
    c = twint.Config()
    # c.Lang = "es"
    # c.Geo = "40,0,500000"
    # c.Since = "2015-01-01"
    # c.Until = "2021-01-01"
    if search:
        c.Search = search
    c.Limit = limit
    if username:
        c.Username = username
    c.Store_object = True
    print(c.Geo.lower())
    twint.run.Search(c)
    tw_list = twint.output.tweets_list
    return tw_list


if __name__ == '__main__':
    tww_list = test()
    for x in range(len(tww_list)):
        va = vars(tww_list[x])
        print(va['tweet'])
