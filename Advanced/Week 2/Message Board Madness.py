import collections
def second_key(wo):
    return 10 - wo[1], wo[0:2]
def author_rankings(thread_list):
    def find_thread(thread_list, names):
        for i in thread_list:
            for posts in thread_list[i]:
                if type(posts) == type(dict()):
                    names[posts["author"]] += posts["upvotes"]

  # TODO: Determine (author, upvotes, ranking) over all threads.
    names = collections.defaultdict(int)
    if len(thread_list) > 0:
        if len(thread_list) < 2:
            thread_list = thread_list[0]
            find_thread(thread_list, names)
        else:
            for threads in thread_list:
                find_thread(threads, names)
        report = []
        for n in names:
            up = names[n]
            title = ""
            if up == 0:
                title = 'Insignificantly Evil'
            elif up < 20:
                title = 'Cautiously Evil'
            elif up < 100:
                title = 'Justifiably Evil'
            elif up < 500:
                title = 'Wickedly Evil'
            else:
                title = 'Diabolically Evil'
            report.append((n, up, title))
        report = sorted(report, key = second_key)
        return report
    return []


if __name__ == '__main__':
  # Example calls to your function.
  print(author_rankings([
    {
        'title': 'Invade Manhatten, anyone?',
        'tags': ['world-domination', 'hangout'],
        'posts': [
            {
                'author': 'Mr. Sinister',
                'content': "I'm thinking 9 pm?",
                'upvotes': 2,
            },
            {
                'author': 'Mystique',
                'content': "Sounds fun!",
                'upvotes': 20,
            },
            {
                'author': 'Magneto',
                'content': "I'm in!",
                'upvotes': 0,
            },
            {
                'author': 'Mr. Sinister',
                'content': "I'm thinking 9 pm?",
                'upvotes': 2,
            },
        ],
    }
  ]))

  print(author_rankings([
  {
    'title': 'Invade Manhattan, anyone?',
    'tags': ['world-domination', 'hangout'],
    'posts': [
      {
        'author': 'ZA. Sinister',
        'content': "I'm thinking 9 pm?",
        'upvotes': 2,
      }
    ]
  },
  {
    'title': 'Interested in a weekly meetup?',
    'tags': ['introductions', 'hangout'],
    'posts': [
      {
        'author': 'AAAystique',
        'content': "Sounds fun!",
        'upvotes': 0,
      },
    ],
    }
  ]))
