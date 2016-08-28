import sys
import json

scores = {}

def buildScoreDict():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score = line.split('\t')
        scores[term] = int(score)

def getTweetScores():
    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweet = json.loads(line)
        sentimentScore = 0
        if 'text' in tweet:
            for word in tweet['text'].encode('utf-8').split():
                if word in scores:
                    sentimentScore += scores[word]
        print sentimentScore

def main():
    buildScoreDict()
    getTweetScores()


if __name__ == '__main__':
    main()
