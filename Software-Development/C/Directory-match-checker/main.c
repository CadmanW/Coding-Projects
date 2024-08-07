#include <stdio.h>
#include <dirent.h>

void main () {

    // open the directory stream
    DIR *d = opendir("/users/cadma/github/coding-projects/software-development/c/directory-match-checker");
    struct dirent *dir;

    if (d) {
        while ((dir = readdir(d)) != NULL) {
            printf("%s\n", dir->d_name);
        }
        closedir(d);
    }


}