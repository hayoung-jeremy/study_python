import requests

indeed_results = requests.get("https://www.indeed.com/q-python-jobs.html")

print(indeed_results)