#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>
#include <sys/types.h>
#include <sys/stat.h>
int main(int argc, char **argv) {
    int fd;
    char *filename = "flag.txt";
    ssize_t ret_in;
    char buffer[100];

    // Open file 
    if ((fd = open(filename, O_RDONLY)) < 0){
        printf("Can not open the flag!!");
    } else {
        // Read content
        if((ret_in = read(fd, &buffer, 100)) > 0){
            // Print buffer
            printf("Flag: %s\n", buffer);
        } else {
            printf("Can not read the flag!!");
        }    
    }
}