import os 
import cProfile
import pstats
from StorageSFTP import StorageSFTP
from StorageGitHub import StorageGitHub
from StoragePCloud import StoragePCloud

from storage_actions import list, rename, delete, compare, synchronize, copy

# with cProfile.Profile() as pr:
#with create_logging_object() as ll:
  #folders_sftp_github = [['www/yu51a5.org/public_html/wp-content/themes/pinboard-child', 'pinboard-child'], ['www/yu51a5.org/backup', 'posts'], ['www/yu51a5.org/public_html/wp-content/themes', 'themes']]
  #folders_pcloud_github = [['music/nein', 'b']]

  #sync_contents(folders_sftp_github, StorageSFTP, StorageGitHub) #, StoragePCloud,)
  #sync_contents([['music/warum', 'a']], StorageGitHub, StorageGitHub) 
  # sync_contents([['tiny', 'e']], StorageGitHub, StoragePCloud) 
  #sync_contents([['music/warum', 'e']], StorageGitHub, StoragePCloud) 
  #sync_contents([['', 'music/warum']], StoragePCloud, StorageGitHub) 
  #

# list_contents(StorageSFTP, 'www/yu51a5.org/backup')
# list_contents(StorageSFTP, 'www/yu51a5.org/public_html/wp-content/uploads/')

#list_contents(StoragePCloud, '')
#list_contents(StorageSFTP, 'www/yu51a5.org/public_html/wp-content/themes/')
#list_contents(StorageGitHub, 'w1')

copy(StoragePCloud, 'My Music/GotJoy.mp3', StoragePCloud, 'aa/My_Music/GotJoy.mp3')

copy(StoragePCloud, 'My Pictures', StoragePCloud, 'aa/My_Pictures')

compare(StoragePCloud, 'My Pictures', StoragePCloud, 'aa/My_Pictures')
compare(StoragePCloud, 'My Music', StoragePCloud, 'aa/My_Music')
copy(StoragePCloud, 'My Music', StoragePCloud, 'aa/My_Music')
copy(StoragePCloud, 'My Music', StoragePCloud, 'aa/My_Music2')


list(StoragePCloud, 'My Music')
list(StorageSFTP, 'www/yu51a5.xyz/public_html/wp-content/themes/')


if False:
  synchronize(StoragePCloud, 'aa', StorageGitHub, 'a')
  
_, files, dirs = list(StoragePCloud, 'aa')
dirs_with_files = [d for d in dirs if len(dirs[d][0]) >= 1]

print(dirs_with_files)
print(dirs)
assert len(dirs_with_files) >= 3
assert len(dirs[dirs_with_files[0]][0]) >=2

delete(StoragePCloud, dirs[dirs_with_files[0]][0][1])
delete(StoragePCloud, dirs_with_files[2])

if False:
  synchronize(StorageGitHub, 'a', StoragePCloud, 'aa')
  compare(StorageGitHub, 'a', StoragePCloud, 'aa')

rename(StoragePCloud, dirs[dirs_with_files[0]][0][0], dirs[dirs_with_files[0]][0][1])
rename(StoragePCloud, dirs_with_files[1], dirs_with_files[2])

if False:
  synchronize(StorageGitHub, 'a', StoragePCloud, 'aa')
  compare(StorageGitHub, 'a', StoragePCloud, 'aa')

synchronize(StorageSFTP, 'www/yu51a5.xyz/public_html/wp-content/uploads', StoragePCloud, 'wp_uploads')
  #sync_contents(StorageSFTP, 'www/yu51a5.org/public_html/wp-content/uploads', StorageGitHub, 'dont')
  #list_contents(StoragePCloud, 'sf')
  #sync_contents(StorageSFTP, 'www/yu51a5.org/backup', StoragePCloud, 'sf') 
  #sync_contents(StorageSFTP, 'www/yu51a5.org/backup', StorageGitHub, 'w1/w3')  
  #sync_contents(StorageSFTP, 'www/yu51a5.org/public_html/wp-content/themes/pinboard-child', StorageGitHub, 'pinboard-child')  
  #sync_contents(StorageSFTP, 'www/yu51a5.org/public_html/wp-content/uploads/persia_greece', StoragePCloud, 'persia_greece')  
  #list_contents(StorageGitHub, 'w1')
print("all done!")

  #stats = pstats.Stats(pr).sort_stats('tottime')
  # stats.print_stats()
  #stats.dump_stats('pstats.csv')

  # pr.print_stats()
