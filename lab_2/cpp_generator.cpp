#include <iostream>
#include <cstdlib>
#include <ctime>


/**
 * This program code generates random bits and outputs them.
 */
int main() 
{
    srand(time(nullptr));
    const int length = 128;
    for (int i = 0; i < length; ++i) 
    {
        int random_bit = rand() % 2; 
        std::cout << random_bit;
    }
    return 0;
}