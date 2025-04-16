from github import Github
import requests
from config import config as cfg

apikey = cfg["assign4tk"]

g = Github(apikey)

repo = g.get_repo("Emmet-Devaney/Private-Repo")

fileInfo = repo.get_contents("Wiki-Andrew.txt")

urlOfFile = fileInfo.download_url

response = requests.get(urlOfFile)
contentOfFile = response.text

replace_content = file_content.replace('Andrew', 'Emmet')


'''
newContents = contentOfFile + " more stuff 2 \n"
print (newContents)
gitHubResponse=repo.update_file(fileInfo.path,"updated by prog",newContents,fileInfo.sha)
print (gitHubResponse)
'''