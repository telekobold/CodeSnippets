/*
 * Creates a text file "inventory.txt" in an existing folder "inventory" in
 * the user's home directory if this file does not already exist and fills it
 * with numbers "1:", "2:", ..., "10:", each separated by two newlines.
 */

// TODO: Check if assignments function/variable <-> import are correct:
#include <string> // for std::string
#include <sstream> // for stringstream()
#include <iostream> // for std::cout, getline()
#include <stdlib.h> // for getenv()
#include <fstream> // for ofstream
#include <unistd.h> // for access(), F_OK()
//#ifdef WIN32
//#define OS_SEP '\\'
//#else
#define OS_SEP '/'
//#endif

int main()
{
    std::string user_file_path = getenv("HOME");
    std::string dirname = "inventory";
    std::string filename = "inventory.txt";
    std::string absolute_filepath = user_file_path + OS_SEP + dirname + OS_SEP + filename;
    std::cout << absolute_filepath << std::endl; // test output
    std::string answer_str;
    char answer;
    unsigned number = 10;
    
    const char *absolute_filepath_char = absolute_filepath.c_str();
    if(access(absolute_filepath_char, F_OK) == 0)
    {
        std::cout << "The file " << absolute_filepath << " already exists. Do you want to override it [y|n]?";
        getline(std::cin, answer_str);
        std::stringstream(answer_str) >> answer;
        if(answer != 'y' && answer != 'Y')
            return 0;
    }
    
    std::ofstream inv_file (absolute_filepath);
    if(inv_file.is_open())
        inv_file << std::endl;
        for(int i = 1; i <= number; i++)
            inv_file << i << ":\n\n\n";
    
    std::cout << "The file " << absolute_filepath << " was written successfully." << std::endl;
}
