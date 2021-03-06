import sys
import getopt
from got import manager

def main(argv):
    if len(argv) == 0:
        print('You must pass some parameters. Use \"-h\" to help.')
        return

    try:
        opts, args = getopt.getopt(argv, "", (
            "username=",
            "near=",
            "within=",
            "since=",
            "until=",
            "querysearch=",
            "toptweets=",
            "maxtweets=",
            "output=",
            "everyn="
        ))

        tweetCriteria = manager.TweetCriteria()

        everyN = None
        for opt, arg in opts:
            if opt == '--username' and arg != '':
                tweetCriteria.username = arg

            elif opt == '--since' and arg != '':
                tweetCriteria.since = arg

            elif opt == '--until' and arg != '':
                tweetCriteria.until = arg

            elif opt == '--querysearch' and arg != '':
                tweetCriteria.querySearch = arg

            elif opt == '--toptweets':
                tweetCriteria.topTweets = arg

            elif opt == '--maxtweets' and arg != '':
                tweetCriteria.maxTweets = int(arg)

            elif opt == '--near' and arg != '':
                tweetCriteria.near = '"' + arg + '"'

            elif opt == '--within' and arg != '':
                tweetCriteria.within = '"' + arg + '"'

            elif opt == '--everyn' and arg != '':
                everyN = int(arg)

        results = []
        if everyN is None:
            results = (manager.TweetManager.getTweets(tweetCriteria))
        else:
            results = manager.TweetManager.getTweets(tweetCriteria, everyN=everyN)

        if len(results) > 0:
            print(results)
            sys.stdout.flush()

        doneMessage = "All done"
        print(doneMessage)
        sys.stdout.flush()


    except Exception as argv:
        print('Arguments parser error, try -h' + argv)
    finally:
        pass


if __name__ == '__main__':
    main(sys.argv[1:])
