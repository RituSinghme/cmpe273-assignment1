import sys, getopt
import re
import json, yaml
#import PyGithub

from flask import Flask, url_for,render_template
from github import Github

app = Flask(__name__)

st = str(sys.argv)
list  = st.split(',')

string = list[1]
username = string.split('/') [-2]
#print username
repo1 = string.split('/') [-1]
repo = repo1.split('\'') [-2]
#print repo

github = Github("RituSinghme", "chhotu*14")

#github = Github()
user = github.get_user(username)
repository = user.get_repo(repo)


#user = github.get_user()
#repository = user.get_repo('cmpe273-assignment1')
#print repository

dev_file_content = repository.get_contents('dev-config.yml')
test_file_content = repository.get_contents('test-config.yml')

dev_yml = dev_file_content.decoded_content
test_yml = test_file_content.decoded_content

#print dev_yml
#print test_yml

dev_json = json.dumps(yaml.load(dev_yml), sort_keys=True, indent=2, separators=(',', ': '))
test_json = json.dumps(yaml.load(test_yml), sort_keys=True, indent=2, separators=(',', ': '))

#print dev_json
#print test_json

@app.route("/v1/dev-config.yml")
def publish():
    return dev_yml

@app.route("/v1/dev-config.json")
def publish1():
    return dev_json


@app.route("/v1/test-config.yml")
def publish2():
    return test_yml

@app.route("/v1/test-config.json")
def publish3():
    return test_json


if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')
