# 2022/11/30 18:03:22  zt    

from github import Github, GithubException

import configparser
import os

class ghStats():
    def __init__(self):
        cfg = configparser.ConfigParser()
        # Get script absolute path
        cfgPath = os.path.dirname(os.path.abspath(__file__))+os.path.sep+"config.ini"
        cfg.read(cfgPath)
        self.gh = Github(cfg['DEFAULT']['GH_TOKEN'])

    def ghGetStat(self):
        '''Get repository number/star/issues/commits
        '''

        totStars  = 0
        totCmts = 0
        totPrs    = 0
        totIssues = 0
        totRepos = 0

        try:
            repos = self.gh.get_user().get_repos()

            totRepos  = repos.totalCount

            for repo in repos:
                try:
                    totStars += repo.stargazers_count
                    totCmts  += repo.get_commits().totalCount
                    prs = repo.get_pulls(state='open')
                    totPrs += prs.totalCount
                    issues = repo.get_issues(state='open')
                    totIssues += issues.totalCount
                except GithubException as err:
                    pass

        except GithubException as error:
            pass

        return [totStars, totCmts, totPrs, totIssues, totRepos]
