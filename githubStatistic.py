# 2022/11/30 18:03:22  zt    

from github import Github, GithubException

import configparser

class ghStats():
    def __init__(self):
        cfg = configparser.ConfigParser()
        cfg.read('config.ini')
        self.gh = Github(cfg['DEFAULT']['GH_TOKEN'])

    def ghGetStat(self):
        '''Get repository number/star/issues/commits
        '''

        repos = self.gh.get_user().get_repos()

        totStars  = 0
        totCmts = 0
        totPrs    = 0
        totIssues = 0

        for repo in repos:
            try:
                totStars += repo.stargazers_count
                totCmts  += repo.get_commits().totalCount
                prs = repo.get_pulls(state='open')
                totPrs += prs.totalCount
                issues = repo.get_issues(state='open')
                totIssues += issues.totalCount
            except GithubException:
                pass

        totRepos  = repos.totalCount
        return [totStars, totCmts, totPrs, totIssues, totRepos]
