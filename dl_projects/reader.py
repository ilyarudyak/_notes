import pandas

def get_titles():
    with open('cs230_projects_raw.txt') as f:
        lines = f.readlines()
    return [line[:line.index('by')-1] for line in lines]

def write_titles():
    with open('cs230_projects_titles.txt', 'w') as f:
        for line in get_titles():
            f.write(line + '\n')

if __name__ == '__main__':
    write_titles()
