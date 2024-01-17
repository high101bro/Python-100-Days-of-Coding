
facebook_posts = [
    {'Likes': 31, 'Comments': 2},
    {'Likes': 13, 'Comments': 2, 'Shares': 1},
    {'Likes': 33, 'Comments': 8, 'Shares': 3},
    {'Comments': 4, 'Shares': 2},
    {'Comments': 1, 'Shares': 1},
    {'Likes': 19, 'Comments': 3},
]


total_likes = 0
for post in facebook_posts:
    try:
        total_likes = total_likes + post['Likes']
        print('added likes')
    except:
        print('no likes')
print(total_likes)