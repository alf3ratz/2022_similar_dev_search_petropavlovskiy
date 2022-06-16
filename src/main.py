import fire

from git.helpers import get_repository_info, save_data


def get_repo(url, path):
    """
    Save data about repository to json file.
    :param path: path to JSON
    :param url: repository url
    :return: list of commits
    """
    path = path.replace('\\', '\\\\')
    repo_info = get_repository_info(url)
    save_data(repo_info, path)
    #save_data()

if __name__ == "__main__":
    fire.Fire({
        "repo-info": get_repo
    })
