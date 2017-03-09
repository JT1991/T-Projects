using System;

namespace Treehouse.CodeChallenges
{
    class Program
    {
        static Main()
        {
            Console.Write("Enter the number of times to print \"Yay!\": ");
            int loop = int.Parse(Console.ReadLine());
            int counter = 0;
            if (counter < loop) {
                Console.Write("Yay!");
                counter += 1;
            }
            else{ 
                Console.Write("Goodbye");}
        }
    }
}