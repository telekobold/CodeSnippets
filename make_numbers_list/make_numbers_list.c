/*
 * Creates a text file "inventory.txt" in an existing folder "inventory" in
 * the user's home directory if this file does not already exist and fills it
 * with numbers "1:", "2:", ..., "10:", each separated by two newlines.
 */

#include <stdio.h> // for printf, snprintf
#include <linux/limits.h> // for ARG_MAX
#include <limits.h> // for PATH_MAX
#include <stdlib.h> // for getenv()
#include <unistd.h> // for access(), F_OK
#include <string.h> // for strcpy
//#ifdef WIN32
//#define OS_SEP '\\'
//#else
#define OS_SEP '/'
//#endif

// `end` must be any number != 0 if the produced string is the end of a file
// path (e.g. if the name of a text file is appended). If `end` is 0,
// this function appends a `/` at the end of `dest` (behind the copy of `src`).
// `count` is not used but demonstrates that non-pointer variables must be
// passed as references to functions (see call of copy_str() in the main 
// function).
char *copy_str(char *dest, char *src, unsigned *count, int end)
{
    for(unsigned i = 0; *src != '\0'; src++, dest++)
    {
        *dest = *src;
        *count++;
    }
    if(end)
        *dest++ = OS_SEP;
    else
        *dest++ = '\0';
    *count++;
    return dest;
}

int main()
{
    // Build the absolute file path "/home/telekobold/inventory/inventory.txt"
    // (quite complicated in C):
    // Get the user's file path (e.g. "/home/telekobold" on my system):
    char user_file_path[PATH_MAX];
    snprintf(user_file_path, PATH_MAX, "%s", getenv("HOME"));
    char *dirname = "inventory\0";
    char *filename = "inventory.txt\0";
    char absolute_filepath[PATH_MAX];
    char *absolute_filepath_ptr;
    char c;
    unsigned count = 0;
    absolute_filepath_ptr = copy_str(absolute_filepath, user_file_path, &count, 1);
    absolute_filepath_ptr = copy_str(absolute_filepath_ptr, dirname, &count, 1);
    copy_str(absolute_filepath_ptr, filename, &count, 0);
    unsigned number = 10;
    
    if(access(absolute_filepath, F_OK) == 0)
    {
        printf("The file %s already exists. Do you want to override it [y|n]?", absolute_filepath);
        char answer = getchar(); // Read a single char from stdin
        if(answer != 'y' && answer != 'Y')
            return 0;
    }
    
    FILE *inv_file = fopen(absolute_filepath, "w");
    fprintf(inv_file, "\n");
    for(int i = 1; i <= number; i++)
        fprintf(inv_file, "%d:\n\n\n", i);
    
    printf("The file %s was written successfully.\n", absolute_filepath);
}
