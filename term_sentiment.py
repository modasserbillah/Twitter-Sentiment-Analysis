import sys
import json

scores = {}

def buildScoreDict():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score = line.split('\t')
        scores[term] = int(score)

def computeTweetScores():
    tweetFile = open(sys.argv[2])
    newScoresDict = {}
    for line in tweetFile:
        tweet = json.loads(line)
        sentimentScore = 0

        if 'text' in tweet:
            words = tweet['text'].encode('utf-8').split()
            for word in words:
                if word in scores:
                    sentimentScore += scores[word]

            for word in words:
                if word not in scores:
                    if word not in newScoresDict:
                        newScoresDict[word] = float(sentimentScore) / len(words)
                    else:
                        newScoresDict[word] +=  float(sentimentScore) / len(words)

    for word, score in newScoresDict.items():
        print str(word) + " " + str(score)


def main():
    buildScoreDict()
    computeTweetScores()


if __name__ == '__main__':
    main()
