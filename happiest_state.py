import sys
import json
import operator

scores = {}
states = {
        'AK': 'Alaska',
        'AL': 'Alabama',
        'AR': 'Arkansas',
        'AS': 'American Samoa',
        'AZ': 'Arizona',
        'CA': 'California',
        'CO': 'Colorado',
        'CT': 'Connecticut',
        'DC': 'District of Columbia',
        'DE': 'Delaware',
        'FL': 'Florida',
        'GA': 'Georgia',
        'GU': 'Guam',
        'HI': 'Hawaii',
        'IA': 'Iowa',
        'ID': 'Idaho',
        'IL': 'Illinois',
        'IN': 'Indiana',
        'KS': 'Kansas',
        'KY': 'Kentucky',
        'LA': 'Louisiana',
        'MA': 'Massachusetts',
        'MD': 'Maryland',
        'ME': 'Maine',
        'MI': 'Michigan',
        'MN': 'Minnesota',
        'MO': 'Missouri',
        'MP': 'Northern Mariana Islands',
        'MS': 'Mississippi',
        'MT': 'Montana',
        'NA': 'National',
        'NC': 'North Carolina',
        'ND': 'North Dakota',
        'NE': 'Nebraska',
        'NH': 'New Hampshire',
        'NJ': 'New Jersey',
        'NM': 'New Mexico',
        'NV': 'Nevada',
        'NY': 'New York',
        'OH': 'Ohio',
        'OK': 'Oklahoma',
        'OR': 'Oregon',
        'PA': 'Pennsylvania',
        'PR': 'Puerto Rico',
        'RI': 'Rhode Island',
        'SC': 'South Carolina',
        'SD': 'South Dakota',
        'TN': 'Tennessee',
        'TX': 'Texas',
        'UT': 'Utah',
        'VA': 'Virginia',
        'VI': 'Virgin Islands',
        'VT': 'Vermont',
        'WA': 'Washington',
        'WI': 'Wisconsin',
        'WV': 'West Virginia',
        'WY': 'Wyoming'
}
stateSentiment = dict.fromkeys(states.keys(), 0)

def buildScoreDict():
    afinnFile = open(sys.argv[1])
    for line in afinnFile:
        term, score = line.split('\t')
        scores[term] = int(score)

def getHappiestState():
    global stateSentiment
    tweetFile = open(sys.argv[2])
    for line in tweetFile:
        tweet = json.loads(line)
        sentimentScore = 0
        if 'text' in tweet:
            for word in tweet['text'].encode('utf-8').split():
                if word in scores:
                    sentimentScore += scores[word]

        if 'user' in tweet and 'location' in tweet['user']:
            locationTokens = tweet['text'].encode('utf-8').split(',')
            if len(locationTokens) == 2:
                for code, name in states:
                    if locationTokens[1] == code or locationTokens[1] == name:
                        stateSentiment[code] += sentimentScore

    happiestState = sorted(stateSentiment.items(), key=operator.itemgetter(1), reverse=True)[0]
    stateCode, stateName = happiestState
    print stateCode



def main():
    buildScoreDict()
    getHappiestState()


if __name__ == '__main__':
    main()
