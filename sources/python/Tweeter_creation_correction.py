import tweepy
from py2neo import Graph
import re

# uri = "10.5.0.6:7474" 
uri = "http://neo4j:7474" 
password="admin"


graph = Graph(uri,password=password)
# http://py2neo.org/v4/database.html#the-graph
# graph.data("CREATE (:USER {name:'VERLEYEN',bdd:'twitter.bdd'})")

# http://tweepy.readthedocs.io/en/v3.5.0/getting_started.html

# definir consumer_key, consumer_secret

consumer_key = "C2Qpfh7S6ml7ipONpsS6Z6Aqq"
consumer_secret = "VozFiaCTOYSu1YYtpG7U2rlZuK5kSzgmmpXrzFjBjMineA2cgL"
access_token = "831914034131849218-GkLaPrHsWYW2GLyUxheXPcpPHbkcrwr"
access_token_secret = "45iCrdYbxsM9HaQkFQ3tjMhWWFYGpssjW8mN40SZ2bTVo"


auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)




user = api.get_user('Dataswati')
print(user.screen_name)
print(user.followers_count)


#(USER)-[ :TWEETED]-(TWEET)
#(USER)-[ :RETWEETED]-(TWEET)
#(TWEET)-[CONTAIN]-(HASHTAG)
UTF_CHARS = r'a-z0-9_\u00c0-\u00d6\u00d8-\u00f6\u00f8-\u00ff'
TAG_EXP = r'(^|[^0-9A-Z&/]+)(#|\uff03)([0-9A-Z_]*[A-Z_]+[%s]*)' % UTF_CHARS
TAG_REGEX = re.compile(TAG_EXP, re.UNICODE | re.IGNORECASE)
AT_EXP = r'(^|[^0-9A-Z&/]+)(@|\uff03)([0-9A-Z_]*[A-Z_]+[%s]*)' % UTF_CHARS
AT_REGEX = re.compile(AT_EXP, re.UNICODE | re.IGNORECASE)


def find_hashtag(text):
    return [c[2] for c in TAG_REGEX.findall(text)]
def find_at(text):
    return [c[2] for c in AT_REGEX.findall(text)]

# http://docs.tweepy.org/en/v3.5.0/cursor_tutorial.html
for querie in ["@Apple, #AI"]:
    for tweet in tweepy.Cursor(api.search, q=querie).items(1000):
        list_lines = ""
        # print(tweet.created_at, tweet.text, tweet.lang)
        create_string = """
            MERGE (u:USER{name:\"%s\"}) 
            MERGE (u)-[:TWEETED]->(tweet:TWEET{text:\"%s\",retweet:\"%s\"}) """%(
        tweet.user.name,tweet.text,tweet.retweeted)
        list_lines+= (create_string+'\n ')
        for i,hastag in enumerate(find_hashtag(tweet.text)):
            create_hastag = """
                MERGE (h%s:HASHTAG{name:\"%s\"})
                MERGE (tweet)-[:CONTAIN]->(h%s) """%(str(i),hastag,str(i))
            list_lines+= (create_hastag+'\n ')

        for i,at in enumerate(find_at(tweet.text)):
            create_contain_user = \
            """
            MERGE (u%s:USER{name:\"%s\"}) 
            MERGE (tweet)-[:CONTAIN]->(u%s) """%(str(i),at,str(i))
            list_lines+= create_contain_user+'\n '
        try : 
            graph.data(list_lines)
        except :
            print("this call didn't work:")
            print(list_lines)
