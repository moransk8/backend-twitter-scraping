import twint


def scraping_twitter(event):
    # search, limit, username
    print(event)
    search = ""
    limit = 20
    username = "elonmusk"

    c = twint.Config()
    c.Lang = "es"
    if not search:
        c.Search = search
    c.Limit = limit
    if not username:
        c.Username = username
    c.Store_object = True
    twint.run.Search(c)
    tw_list = twint.output.tweets_list

    return tw_list
