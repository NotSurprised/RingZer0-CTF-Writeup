#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
int main(int argc, char **argv) {
    char buffer[1024];
    int fd;
    fd = open64("flag.txt", O_RDONLY);
    pread64(fd, buffer, 1024, 0);
    printf("flag: %s\n", buffer);
    close(fd);
}