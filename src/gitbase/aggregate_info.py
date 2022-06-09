import os
import subprocess

sql = '''
SELECT
    name, email,
    JSON_UNQUOTE(JSON_EXTRACT(stats, '$.Language')) AS language,
    sum(JSON_EXTRACT(stats, '$.Code.Additions')) AS code_lines_added,
    sum(JSON_EXTRACT(stats, '$.Code.Deletions')) AS code_lines_removed
FROM (
    SELECT
        repository_id AS repo,
        commits.commit_author_name as name, 
        commits.commit_author_email as email,
        commit_hash,
        EXPLODE(COMMIT_FILE_STATS(repository_id, commit_hash)) AS stats
    FROM commits
) t group by name, email, language;
'''


def aggregate():
    subprocess.check_output(
        [
            "powershell.exe",
            "Get-CimInstance -Class Win32_ComputerSystemProduct | Select-Object -ExpandProperty UUID",
        ]
    )
    path_to_gitbase_bin = f"{os.getcwd()}".replace('\\', '\\\\')
    path = '/mnt/c/users/user1337/pycharmprojects/2022_similar_dev_search_petropavlovskiy/'
    # os.system("c:/windows/system32/wsl -c ls -la")
    # subprocess.run("c:/windows/system32/wsl -c ls -la")
    query = 'select file_path, ref_commits.repository_id from commit_files natural join ref_commits where ref_name = \'HEAD\'  and history_index = 0;'
    # subprocess.run(['C:\Program Files\Git\\bin\\bash.exe', '-c', 'echo ls -l'], stdout=subprocess.PIPE)
    # subprocess.run(['c:\windows\system32\wsl',  '-c ls -l'], stdout=subprocess.PIPE)
    # subprocess.run(['c:\windows\system32\wsl.exe',  f'cd {path}'], stdout=subprocess.PIPE)
    DETACHED_PROCESS = 0x00000008
    CREATE_NEW_PROCESS_GROUP = 0x00000200
    # subprocess.call(['C:\\cygwin64\\bin\\bash.exe', '-l', 'RunModels.scr'],
    #                 stdin=vin, stdout=vout,
    #                 cwd='C:\\path\\dir_where_RunModels\\')
    pid1 = subprocess.Popen(['sh', 'test.sh'], shell=True,
                            stdout=subprocess.PIPE)
    subprocess.call(['sh', 'test.sh'], shell=True,
                     stdout=subprocess.PIPE)
    print(subprocess.check_call(['c:\windows\system32\wsl.exe', 'ls']))
    res = subprocess.Popen(['c:\windows\system32\wsl.exe', './gitbase server -d src/repos/'], shell=True,
                           executable='/bin/bash')
    bashCommand = "./gitbase server -d src/repos/"
    process = subprocess.Popen(['c:\windows\system32\wsl.exe', './gitbase server -d src/repos/'],
                               stdout=subprocess.PIPE)
    output, error = process.communicate()
    pid1 = subprocess.Popen(
        ['C:\Program Files\Git\\bin\\bash.exe', f'cd {path_to_gitbase_bin} && ./gitbase server -d src/repos/ && ls'],
        shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
        creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
    stdout_data = pid1.communicate(input='ls'.encode())[0]
    with pid1.stdout:
        for line in iter(pid1.stdout.readline, b''):
            print(line)
    pid1.wait()  # wait for the subprocess to exit
    # subprocess.run(['c:/windows/system32/wsl sudo ./gitbase server -d src/repos/'], stdout=subprocess.PIPE)
    # subprocess.run(['c:/windows/system32/wsl mysql -h 127.0.0.1 -u root'], stdout=subprocess.PIPE)
    pid2 = subprocess.Popen(['c:/windows/system32/wsl mysql -h 127.0.0.1 -u root'], shell=True,
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout_data = pid2.communicate(input=query.encode())[0]
    with pid2.stdout:
        for line in iter(pid2.stdout.readline, b''):
            print(line)
    pid2.stdin.flush()
    # pid3 = subprocess.Popen([f'echo {query}'], shell=True,
    #                         stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
    #                         creationflags=DETACHED_PROCESS | CREATE_NEW_PROCESS_GROUP)
    # subprocess.call(['echo', 'chmod +x ./gitbase'])
    # subprocess.call(['sudo', f'{path_to_gitbase_bin} server -d src/repos/'])
    # subprocess.call(['echo', 'mysql -h 127.0.0.1 -u root'])
    # subprocess.call(['echo', query])
    # os.system('sudo ./gitbase server -d repos/')
    # os.system('mysql -h 127.0.0.1 -u root')
    print(pid2.stdout.readlines(10))
