import sys
import json



def computeFrequency():
    wordDict = {}
    wordCount = 0
    tweetFile = open(sys.argv[1])
    for line in tweetFile:
        tweet = json.loads(line)

        if 'text' in tweet:
            for word in tweet['text'].encode('utf-8').split():
                if word not in wordDict:
                    wordDict[word] = 1
                else:
                    wordDict[word] += 1
                wordCount += 1
    for word, count in wordDict.items():
        print str(word) + " " + str(float(count) / wordCount)

def main():
    computeFrequency()


if __name__ == '__main__':
    main()
