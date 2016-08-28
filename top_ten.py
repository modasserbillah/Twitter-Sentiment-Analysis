import sys
import json
import operator

def main():
    tweetFile = open(sys.argv[1])
    hashtags = {}

    for line in tweetFile:
        tweet = json.loads(line)
        if 'entities' in tweet and 'hashtags' in tweet['entities']:
            tags = tweet['entities']['hashtags']
            for tag in tags:
                tagText = tag['text'].encode('utf-8')
                if tagText not in hashtags:
                    hashtags[tagText] = 1
                else:
                    hashtags[tagText] += 1

    sortedHashTags = sorted(hashtags.items(), key=operator.itemgetter(1), reverse=True)
    for i in range(10):
        print sortedHashTags[i][0] +" "+ str(sortedHashTags[i][1])


if __name__ == '__main__':
    main()
