import fire

from helpers import *
from gitbase.aggregate_info import aggregate



def get_repo():
    """
    Save data about repository to json file.
    :param path: path to JSON
    :param url: repository url
    :return: list of commits
    """
    # url = 'https://github.com/OmdenaAI/Arabic-Chapter'
    # path = path.replace('\\','\\\\')
    # with open(path) as file:
    #     lines = file.readlines()
    #     print(lines)
    # save_data(get_repository_info(url), path)
    #get_stargazers("","",10)
    aggregate()


if __name__ == "__main__":
    fire.Fire({
        "repo-info": get_repo
    })
