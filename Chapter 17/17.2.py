#! python3

print("Task 17.2")

from operator import itemgetter

import requests
from plotly.graph_objs import Bar
from plotly import offline

# Make an API call and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Process information about each submission.
submission_ids = r.json()
submission_dicts = []
for submission_id in submission_ids[:10]:
    # Make a separate API call for each submission.
    url = f"https://hacker-news.firebaseio.com/v0/item/{submission_id}.json"
    r = requests.get(url)
    print(f"id: {submission_id}\tstatus: {r.status_code}")
    response_dict = r.json()

    # Build a dictionary for each article.
    submission_dict = {
        'title': response_dict['title'],
        'hn_link': f"http://news.ycombinator.com/item?id={submission_id}",
        'comments': response_dict['descendants'],
    }
    submission_dicts.append(submission_dict)

submission_dicts = sorted(submission_dicts, key=itemgetter('comments'),
                          reverse=True)

for submission_dict in submission_dicts:
    print(f"\nTitle: {submission_dict['title']}")
    print(f"Discussion link: {submission_dict['hn_link']}")
    print(f"Comments: {submission_dict['comments']}")

# Generate lists for plotting.
titles, num_comments, discussion_links = [], [], []
for sd in submission_dicts:
    title = sd['title']
    hn_link = sd['hn_link']
    discussion_link = f"<a href='{hn_link}'>{title[:15]}...</a>"

    titles.append(title)
    num_comments.append(sd['comments'])
    discussion_links.append(discussion_link)

# Make visualization.
data = [{
    'type': 'bar',
    'x': discussion_links,
    'y': num_comments,
    'hovertext': titles,
    'marker': {
        'color': 'rgb(255, 0, 0)',
        'line': {'width': 2, 'color': 'rgb(250, 200, 0)'}
    },
    'opacity': 0.6,
}]

my_layout = {
    'title': 'Most discusion articles in Hacker-News.',
    'titlefont': {'size': 20},
    'xaxis': {
        'title': 'Article',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14},
    },
    'yaxis': {
        'title': 'Numbers of Comments',
        'titlefont': {'size': 18},
        'tickfont': {'size': 14},
    },

}

fig = {'data': data, 'layout': my_layout}
offline.plot(fig, filename='discussion_articles_repos.html')