import requests as r
from dotenv import load_dotenv
import os
import sys
load_dotenv()
oauth_token = os.getenv("GITHUB_TOKEN")
username = sys.argv[1]
base_url = "https://api.github.com"
response = r.get(
    f"{base_url}/users/{username}/events",
    headers={"Authorization": f"Bearer {oauth_token}"}
)
events = response.json()
for event in events:
    if event["type"] == "PushEvent":
        print(f"Запушено на {event['repo']['name']}" )
    elif event["type"] == "IssueCommentEvent":
        print(f"оставил комментарий к задаче {event['payload']['issue']['number']}")
    elif event["type"] == "PullRequestEvent":
        print(f"создал пул-реквест {event['payload']['pull_request']['number']}")
    elif event['type'] == 'CreateEvent':
        print(f"Созданный {event['payload']['ref_type']} {event['payload']['ref']}")