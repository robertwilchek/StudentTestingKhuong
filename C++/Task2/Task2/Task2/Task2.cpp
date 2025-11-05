//

#include <iostream>
#include <stdexcept>
#include <string>

void printLength(const std::string* textPtr)
{
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

    std::cout << "This line is never reached" << std::endl
}
