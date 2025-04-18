from github import Github
import requests
from config import apikey as cfg

apikey = cfg["assign4tk"]

g = Github(apikey)

repo = g.get_repo("Emmet-Devaney/Private-Repo")

fileInfo = repo.get_contents("Wiki-Andrew.txt")

urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

replace_content = contentOfFile.replace('Andrew', 'Emmet')
#replace_content = contentOfFile.replace('Emmet', 'Andrew')


print(replace_content)

gitHubResponse = repo.update_file(fileInfo.path,"updated by program assignment04-github.py", replace_content, fileInfo.sha)

print(gitHubResponse)
