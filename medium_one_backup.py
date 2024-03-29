from storage_actions import backup_a_Medium_website
from StorageGitHub import StorageGitHub

for url, dirname in [['https://hoffa.medium.com', "mediumH"],
                     ['https://medium.com/@real.zyxxy', "mediumZ"], 
                     ['https://medium.com/@yu51a5', "mediumY"], 
  ]:

  backup_a_Medium_website(url_or_urls=url, path=dirname, StorageType=StorageGitHub, kwargs_storage={'secret_name': "medium_github_secret"}, do_same_root_urls=True, check_other_urls=True)
