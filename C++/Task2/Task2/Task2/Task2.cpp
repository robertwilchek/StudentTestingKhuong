//

#include <iostream>
#include <stdexcept>
#include <string>

void printLength(const std::string* textPtr)
{   
    // Checks if pointer is null, if yes then print length of 0
    if (textPtr == nullptr)
        {
        std::cout << "Length: 0" << std::endl;
        return;
        }
    std::cout << "Length: " << textPtr->size() << std::endl;
}

int main()
{
    std::string* message = nullptr;
    printLength(message);

    if (true)
    {
        throw std::runtime_error("Simulated failure in Task2");
    }
// Missing semicolon at end of statement
    std::cout << "This line is never reached" << std::endl;
}
