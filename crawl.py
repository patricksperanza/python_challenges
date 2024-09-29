import os


def list_files_in_directory(path):
    return [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]


directory_path = "C:\\Users\\Revenova User\\Desktop\\tmsMain\\packages\\seedMain\\force-app\\main\\default\\flexipages"
os.chdir(directory_path)
files = list_files_in_directory(directory_path)
res = set()
for f in files:
    print(f)
    with (open(f, 'r') as f):
        lines = f.readlines()
        for i in range(len(lines)):
            if 'quickaction' in lines[i].lower():
                l = lines[i+1]
                start = l.index('value>') + 6
                stop = l.index('</value>')
                print('\t' + l[start:stop])