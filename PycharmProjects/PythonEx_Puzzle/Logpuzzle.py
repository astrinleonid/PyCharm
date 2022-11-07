from urllib import request
import os


FILENAME1 = '/Users/leonidastrin/myrepo/animal_code.google.com'
FILENAME2 = '/Users/leonidastrin/myrepo/place_code.google.com'
SERVER = 'http://code.google.com'
TARGET_DIRECTORY1 = '/Users/leonidastrin/myrepo/Logpuzzle1'
TARGET_DIRECTORY2 = '/Users/leonidastrin/myrepo/Logpuzzle2'

def find_the_puzzle(line):
    """
    If the line contains the path with the word 'puzzle' inside, returns (True, path)
    Otherwise returns (False, '')
    """
    index_after_GET = line.find('"GET')+4
    line_tail = line[index_after_GET:].split()
    path = line_tail[0]
    if "puzzle" in path.split('/'):
        return (True, path)
    else:
        return (False, '')

def sort_puzzles(urls):
    """
    Sort URLs in accordance to the last segment of the file name
    """
    tuples_to_sort = []
    for url in urls:
        file_name = url.split('/')[-1]
        url_path = "/".join(url.split('/')[:-1]) + "/" + "-".join(file_name.split('-')[:-1])
        file_name_last_part = file_name.split('-')[-1]
        tuples_to_sort.append(( file_name_last_part, url_path))
    tuples_sorted = sorted(tuples_to_sort)
    return [path + "-" + name for name, path in tuples_sorted]


def read_urls(filename):
    """
    Opens the file, finds all pathes containing word 'puzzle' inside,
    and returns list of full pathes in alphabetical order
    """
    server_name = "http://" + filename.split('/')[-1].split('_')[-1]
    puzzle_pathes = []
    file = open(filename,"r")
    log_text = file.read()
    file.close()
    logs = log_text.splitlines()
    for line in logs:
        (puzzle_is_there, path_to_puzzle) = find_the_puzzle(line)
        if puzzle_is_there:
            path_to_puzzle = server_name + path_to_puzzle
            if path_to_puzzle not in puzzle_pathes:   # filtering out duplicates
                puzzle_pathes.append(path_to_puzzle)

    return sort_puzzles(puzzle_pathes)

def build_html(files):
    """
    Builds HTML code displaying files listed in 'files'
    and writes it into 'index.html'
    """
    html_string = "<html><body>"
    for file_path in files:
        html_string += '<img src ="'
        html_string += file_path
        html_string += '">'
    html_string += "</body></html>"
    file = open("index.html","w")
    file.write(html_string)
    file.close()

def change_directory(dir):
    """
    Change working directory to the one specified in dir. Create if nesessary.
    """
    splitted_path = dir.split('/')
    base_dir = "/".join(splitted_path[:-1])
    puzzle_dir = splitted_path[-1]
    os.chdir(base_dir)
    try:
        os.mkdir(puzzle_dir)
    except:
        print("Directory already exists")
    os.chdir(puzzle_dir)


def download_images(urls, dir):
    """
    Download images from locations specified in urls, store them in the specified directory.
    Generate index.html file opening downloaded images side by side
    """
    change_directory(dir)
    files_for_html = []
    for i, url in enumerate(urls):
        store_name = "img" + str(i) +".jpg"
        store_path = dir + "/" + store_name
        files_for_html.append(store_path)
        print(f"Retrieving {url} as img{i}")
        print(f"Saving as {store_name}")
        response = request.urlretrieve(url,store_name)
        print("Done")
    build_html(files_for_html)


def main():

    pathes = read_urls(FILENAME1)
    download_images(pathes,TARGET_DIRECTORY1)

    pathes = read_urls(FILENAME2)
    download_images(pathes,TARGET_DIRECTORY2)

if __name__ == '__main__':
    main()