using System;

namespace Calculator_V1
{
    class Program
    {
        static void Main(string[] args)
        {
            Console.ForegroundColor = ConsoleColor.Black;
            string exit = "y";
            while (exit == "y" || exit == "Y")
            {
                //num1 toStore Q
                Console.ForegroundColor = ConsoleColor.Black;
                Console.WriteLine("\nInput first number\n");
                //num1 store A
                Console.ForegroundColor = ConsoleColor.DarkCyan; 
                double numOne = Convert.ToDouble(Console.ReadLine());
                
                //opp1 multicolour Q
                Console.ForegroundColor = ConsoleColor.Black;
                Console.WriteLine("\nChoose operation:");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\n+");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("\n-");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\n*");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("\n/");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\nSqrt");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("\nAbs");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\nRound");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("\nLowest");
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                Console.WriteLine("\nHighest");
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                Console.WriteLine("\nx^y\n");

                //store opp1 variable
                Console.ForegroundColor = ConsoleColor.DarkCyan;
                string opp = Console.ReadLine();

                //num1 solve if sqrt, abs or round
                Console.ForegroundColor = ConsoleColor.DarkGreen;
                if (opp == "Sqrt" || opp == "sqrt" || opp == "Square Root" || opp == "square root" || opp == "Square root")
                {
                    Console.WriteLine("\n");
                    Console.WriteLine(Math.Sqrt(numOne));
                }
                else
                {
                    if (opp == "Abs" || opp == "abs")
                    {
                        Console.WriteLine("\n");
                        Console.WriteLine(Math.Abs(numOne));
                    }
                    else
                    {
                        if (opp == "Round" || opp == "round")
                        {
                            Console.WriteLine("\n");
                            Console.WriteLine(Math.Round(numOne));
                        }
                        else
                        {
                            if (opp == "x^y" || opp == "X^Y" || opp == "X^y" || opp == "^")
                            {
                                //ask indice value 
                                Console.ForegroundColor = ConsoleColor.Black;
                                Console.WriteLine("\nInput indice value\n");
                                //store indice value
                                Console.ForegroundColor = ConsoleColor.DarkCyan;
                                double indice = Convert.ToDouble(Console.ReadLine());
                                //convert to correct
                                double indiceMinus = indice - 3;

                                //loops and stuff solve
                                double ans = numOne * numOne;
                                for (int i = 0; i <= indiceMinus; i++)
                                {
                                    double ansTwo = ans * numOne;
                                    ans = ansTwo;
                                }
                                //write final 
                                Console.WriteLine($"\n{ans}\n");
                            }
                            else //num2 Q & A & solve
                            {
                                //num2 toStore Q
                                Console.ForegroundColor = ConsoleColor.Black;
                                Console.WriteLine("\nInput second number\n");
                                //num2 store A
                                Console.ForegroundColor = ConsoleColor.DarkCyan;
                                double numTwo = Convert.ToDouble(Console.ReadLine());


                                //solve num2 w. num1
                                Console.ForegroundColor = ConsoleColor.DarkGreen;
                                if (opp == "+")
                                {
                                    Console.WriteLine("\n");
                                    Console.WriteLine(numOne + numTwo);
                                }
                                else
                                {
                                    if (opp == "-")
                                    {
                                        Console.WriteLine("\n");
                                        Console.WriteLine(numOne - numTwo);
                                    }
                                    else
                                    {
                                        if (opp == "*")
                                        {
                                            Console.WriteLine("\n");
                                            Console.WriteLine(numOne * numTwo);
                                        }
                                        else
                                        {
                                            if (opp == "/")
                                            {
                                                Console.WriteLine("\n");
                                                Console.WriteLine(numOne / numTwo);
                                            }
                                            else
                                            {
                                                if (opp == "Lowest" || opp == "lowest" || opp == "Low" || opp == "low")
                                                {
                                                    Console.WriteLine("\n");
                                                    Console.WriteLine(Math.Min(numOne, numTwo));
                                                }
                                                else
                                                {
                                                    if (opp == "Highest" || opp == "highest" || opp == "High" || opp == "high")
                                                    {
                                                        Console.WriteLine("\n");
                                                        Console.WriteLine(Math.Max(numOne, numTwo));
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
                //restart y/n
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                Console.WriteLine("\n\nDo you wish to solve another equation? y/n\n");
                exit = Console.ReadLine();
            }
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("\nc:/Session terminated\nPress any button to exit the console\n");
            Console.ForegroundColor = ConsoleColor.Gray;
        }
    }
}
