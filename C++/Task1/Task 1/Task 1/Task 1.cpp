#include <iostream>
#include <fstream>

int main()
{
    // Prints to term
    std::cout << "Hello World" << std::endl;

    // Print to file
    std::ofstream outputFile;
    outputFile.open("HelloWorld.txt");

    outputFile << "Hello World" << std::endl;
    outputFile.close();

    return 0;
}