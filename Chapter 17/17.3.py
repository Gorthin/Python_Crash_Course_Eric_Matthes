#! python3

print("Task 17.3")

import requests

from plotly.graph_objs import Bar
from plotly import offline

def get_response():
    """Make an api call, and return the response."""
    url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
    headers = {'Accept': 'application/vnd.github.v3+json'}
    r = requests.get(url, headers=headers)
    return r

def get_repo_dicts(r):
    """Return a set of dicts representing the most popular repositories."""
    response_dict = r.json()
    repo_dicts = response_dict['items']
    return repo_dicts

def get_project_data(repo_dicts):
    """Return data needed for each project in visualization."""
    repo_links, stars, labels = [], [], []
    for repo_dict in repo_dicts:
        repo_name = repo_dict['name']
        repo_url = repo_dict['html_url']
        repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
        repo_links.append(repo_link)

        stars.append(repo_dict['stargazers_count'])

        owner = repo_dict['owner']['login']
        description = repo_dict['description']
        label = f"{owner}<br />{description}"
        labels.append(label)

    return repo_links, stars, labels

def make_visualization(repo_links, stars, labels):
    """Generate the visualization of most commented articles."""
    data = [{
        'type': 'bar',
        'x': repo_links,
        'y': stars,
        'hovertext': labels,
        'marker': {
            'color': 'rgb(255, 0, 0)',
            'line': {'width': 2, 'color': 'rgb(250, 200, 0)'}
        },
        'opacity': 0.6,
    }]

    my_layout = {
        'title': 'Most-Starred Python Projects on GitHub',
        'titlefont': {'size': 20},
        'xaxis': {
            'title': 'Repository',
            'titlefont': {'size': 18},
            'tickfont': {'size': 14},
        },
        'yaxis': {
            'title': 'Stars',
            'titlefont': {'size': 18},
            'tickfont': {'size': 14},
        },

    }

    fig = {'data': data, 'layout': my_layout}
    offline.plot(fig, filename='python_repos.html')

if __name__ == '__main__':
    r = get_response()
    repo_dicts = get_repo_dicts(r)
    repo_links, stars, labels = get_project_data(repo_dicts)
    make_visualization(repo_links, stars, labels)