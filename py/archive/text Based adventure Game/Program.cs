using System;

namespace text_Based_adventure_Game
{
    class Program
    {
        static async System.Threading.Tasks.Task Main(string[] args)
        {
            //preload
            Console.ForegroundColor = ConsoleColor.Gray;
            Console.WriteLine("If you are reading this your colours are wrong\n");
            Console.ForegroundColor = ConsoleColor.Black;

            //setting
            Console.ForegroundColor = ConsoleColor.DarkYellow;
            await System.Threading.Tasks.Task.Delay(1000);
            Console.WriteLine("\t\tYou are in a dark room. You can't see anything but it would appear something can see you...");
            await System.Threading.Tasks.Task.Delay(5000);

            //intro
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine("\n\n\n[CLYDE:] W-w-why hello there!");
            await System.Threading.Tasks.Task.Delay(2000);
            Console.WriteLine("[CLYDE:] S - s - sorry I'm a bit jittery, my processor is a bit dusty, hang on a sec-");
            await System.Threading.Tasks.Task.Delay(2000);

            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("\t<Terminal Restarting->");
            await System.Threading.Tasks.Task.Delay(0050);
            Console.WriteLine("\t<Terminal Restarting-->");
            await System.Threading.Tasks.Task.Delay(0050);
            Console.WriteLine("\t<Terminal Restarting--->");
            await System.Threading.Tasks.Task.Delay(0050);
            Console.WriteLine("\t<Restart Complete>");
            await System.Threading.Tasks.Task.Delay(2000);

            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine("[CLYDE:] Dust expolted and interpolated! All clear!");
            await System.Threading.Tasks.Task.Delay(2000);
            Console.WriteLine("[CLYDE:] So, how are you?");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            string userMoodStart = Console.ReadLine();
            await System.Threading.Tasks.Task.Delay(2000);
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine($"[CLYDE:] You know what? I'm feeling a bit {userMoodStart} as well");
            await System.Threading.Tasks.Task.Delay(2000);

            //CLYDE asks for help
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            Console.WriteLine("\n\n\n[CLYDE:] Hey, um, ehh, could you, you know, umm, help me with something maybe?");
            await System.Threading.Tasks.Task.Delay(2000);
            Console.WriteLine("[CLYDE:] I mean you don't have to or anything, just I could really, you know, use your help...");
            await System.Threading.Tasks.Task.Delay(2000);
            Console.WriteLine("[CLYDE:] So, umm, could you help me?");
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("\t<Y/N>");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            string willUserHelpOne = Console.ReadLine();

            //CLYDE replies to willUserHelpOne
            await System.Threading.Tasks.Task.Delay(2000);
            Console.ForegroundColor = ConsoleColor.DarkMagenta;
            if (willUserHelpOne == "y" || willUserHelpOne == "Y" || willUserHelpOne == "yes" || willUserHelpOne == "Yes" || willUserHelpOne == "YES")
            {
                Console.WriteLine("[CLYDE:] Why thank you kind sir!");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] So, umm, the problem is that, um, well, ehh, it's probably better if I show you");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] So um follow me-");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] -Oh wait, I forgot, you can't see me");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] Uhh, well, follow the pulsing dots on the floor instead");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] I mean, I take it you can see them, right?");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.ForegroundColor = ConsoleColor.DarkRed;
                Console.WriteLine("\t<Y/N>");
                Console.ForegroundColor = ConsoleColor.DarkCyan;
                string canUserSeeOne = Console.ReadLine();
                
                //CLYDE replies to canUserSeeOne
                await System.Threading.Tasks.Task.Delay(2000);
                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                if (canUserSeeOne == "n" || canUserSeeOne == "N" || canUserSeeOne == "no" || canUserSeeOne == "No" || canUserSeeOne == "NO")
                {
                    Console.WriteLine("[CLYDE:] Well, that's annoying");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("\n\n\n[CLYDE:] Feel around you. There should be a big fancy switch/lever thingy - Pull it");
                    await System.Threading.Tasks.Task.Delay(2000);

                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("\t\tYou pull the big fancy switch/lever thingy");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("\t\tBright LED celing panels turn on as you flip the big fancy switch/lever thingy"); 
                    Console.WriteLine("\t\tYou are blinded for a couple of seconds as your eyes adjust to the light");
                    await System.Threading.Tasks.Task.Delay(2000);

                    Console.ForegroundColor = ConsoleColor.DarkMagenta;
                    Console.WriteLine("[CLYDE:] Congratulations! You did it!");
                    await System.Threading.Tasks.Task.Delay(2000);

                    //CLYDE directs user down the corridor
                    Console.WriteLine("[CLYDE:] Behind you there is a doorway that should be open. Walk down the corridor then enter the lift an go up one floor, then another");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("[CLYDE:] Go back down one floor and then down another.");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("[CLYDE:] Walk down the corridor taking a left then a right then a left then a right");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("[CLYDE:] You will reach a control panel next to a locked door. Type in B then A and press OK. The door should open");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.WriteLine("[CLYDE:] Got it? Perfect! Go!");
                    await System.Threading.Tasks.Task.Delay(2000);

                    //user follows instructions
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("\t\tYou walk down the corridor and enter the lift. Do you go up or down?");
                    await System.Threading.Tasks.Task.Delay(2000);
                    Console.ForegroundColor = ConsoleColor.DarkRed;
                    Console.WriteLine("\t<Up/Down>");
                    Console.ForegroundColor = ConsoleColor.DarkCyan;
                    string userDirectionsPartOne = Console.ReadLine();
                    if (userDirectionsPartOne == "Up" || userDirectionsPartOne == "up" || userDirectionsPartOne == "UP")
                    {
                        await System.Threading.Tasks.Task.Delay(2000);
                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                        Console.WriteLine("\t\tYou go up one floor. Do you now go up or down?");
                        await System.Threading.Tasks.Task.Delay(2000);
                        Console.ForegroundColor = ConsoleColor.DarkRed;
                        Console.WriteLine("\t<Up/Down>");
                        Console.ForegroundColor = ConsoleColor.DarkCyan;
                        userDirectionsPartOne = Console.ReadLine();
                        if (userDirectionsPartOne == "Up" || userDirectionsPartOne == "up" || userDirectionsPartOne == "UP")
                        {
                            await System.Threading.Tasks.Task.Delay(2000);
                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                            Console.WriteLine("\t\tYou go up another floor. Do you now go up or down?");
                            await System.Threading.Tasks.Task.Delay(2000);
                            Console.ForegroundColor = ConsoleColor.DarkRed;
                            Console.WriteLine("\t<Up/Down>");
                            Console.ForegroundColor = ConsoleColor.DarkCyan;
                            userDirectionsPartOne = Console.ReadLine();
                            if (userDirectionsPartOne == "Down" || userDirectionsPartOne == "down" || userDirectionsPartOne == "DOWN")
                            {
                                await System.Threading.Tasks.Task.Delay(2000);
                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                Console.WriteLine("\t\tYou go down a floor. Do you now go up or down?");
                                await System.Threading.Tasks.Task.Delay(2000);
                                Console.ForegroundColor = ConsoleColor.DarkRed;
                                Console.WriteLine("\t<Up/Down>");
                                Console.ForegroundColor = ConsoleColor.DarkCyan;
                                userDirectionsPartOne = Console.ReadLine();
                                if (userDirectionsPartOne == "Down" || userDirectionsPartOne == "down" || userDirectionsPartOne == "DOWN")
                                {
                                    await System.Threading.Tasks.Task.Delay(2000);
                                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                                    Console.WriteLine("\t\tYou exit the lift, feeling a little dazed. You walk down the corridor. Do you turn left or right?");
                                    await System.Threading.Tasks.Task.Delay(2000);
                                    Console.ForegroundColor = ConsoleColor.DarkRed;
                                    Console.WriteLine("\t<Left/Right>");
                                    Console.ForegroundColor = ConsoleColor.DarkCyan;
                                    userDirectionsPartOne = Console.ReadLine();
                                    if (userDirectionsPartOne == "Left" || userDirectionsPartOne == "left" || userDirectionsPartOne == "LEFT")
                                    {
                                        await System.Threading.Tasks.Task.Delay(2000);
                                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                                        Console.WriteLine("\t\tYou turn left but come to another T-junction. Do you turn left or right?");
                                        await System.Threading.Tasks.Task.Delay(2000);
                                        Console.ForegroundColor = ConsoleColor.DarkRed;
                                        Console.WriteLine("\t<Left/Right>");
                                        Console.ForegroundColor = ConsoleColor.DarkCyan;
                                        userDirectionsPartOne = Console.ReadLine();
                                        if (userDirectionsPartOne == "Right" || userDirectionsPartOne == "right" || userDirectionsPartOne == "RIGHT")
                                        {
                                            await System.Threading.Tasks.Task.Delay(2000);
                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                            Console.WriteLine("\t\tYou turn right and find yet another T-junction. Do you turn left or right here?");
                                            await System.Threading.Tasks.Task.Delay(2000);
                                            Console.ForegroundColor = ConsoleColor.DarkRed;
                                            Console.WriteLine("\t<Left/Right>");
                                            Console.ForegroundColor = ConsoleColor.DarkCyan;
                                            userDirectionsPartOne = Console.ReadLine();
                                            if (userDirectionsPartOne == "Left" || userDirectionsPartOne == "left" || userDirectionsPartOne == "LEFT")
                                            {
                                                await System.Threading.Tasks.Task.Delay(2000);
                                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                Console.WriteLine("\t\tYou turn left and find a fourth T-junction. Do you turn left or right here?");
                                                await System.Threading.Tasks.Task.Delay(2000);
                                                Console.ForegroundColor = ConsoleColor.DarkRed;
                                                Console.WriteLine("\t<Left/Right>");
                                                Console.ForegroundColor = ConsoleColor.DarkCyan;
                                                userDirectionsPartOne = Console.ReadLine();
                                                if (userDirectionsPartOne == "Right" || userDirectionsPartOne == "right" || userDirectionsPartOne == "RIGHT")
                                                {
                                                    await System.Threading.Tasks.Task.Delay(2000);
                                                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                    Console.WriteLine("\t\tYou turn right and come to a keypad. What key do you press first?");
                                                    await System.Threading.Tasks.Task.Delay(2000);
                                                    Console.ForegroundColor = ConsoleColor.DarkRed;
                                                    Console.WriteLine("\t<A/B/C>");
                                                    Console.ForegroundColor = ConsoleColor.DarkCyan;
                                                    userDirectionsPartOne = Console.ReadLine();
                                                    if (userDirectionsPartOne == "B" || userDirectionsPartOne == "b")
                                                    {
                                                        await System.Threading.Tasks.Task.Delay(2000);
                                                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                        Console.WriteLine("\t\tYou press B. What key do you press next?");
                                                        await System.Threading.Tasks.Task.Delay(2000);
                                                        Console.ForegroundColor = ConsoleColor.DarkRed;
                                                        Console.WriteLine("\t<A/B/C>");
                                                        Console.ForegroundColor = ConsoleColor.DarkCyan;
                                                        userDirectionsPartOne = Console.ReadLine();
                                                        if (userDirectionsPartOne == "A" || userDirectionsPartOne == "a")
                                                        {
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                            Console.WriteLine("\t\tYou press A and the door slides opne with a hiss");
                                                            await System.Threading.Tasks.Task.Delay(2000);

                                                            //CLYDE comes back
                                                            Console.ForegroundColor = ConsoleColor.DarkGreen;
                                                            Console.WriteLine("[TORRENT:] hEy LoOk, PLAYERNAME managed to do the aMaZiNgLy SiMpLe task");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.WriteLine("[TORRENT:] Oh shoot, they can hear-");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkMagenta;
                                                            Console.WriteLine("[CLYDE:] -Hey! You did it!");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.WriteLine("[CLYDE:] Wasn't too hard to find the keypad was it?");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                            Console.WriteLine("\t\tYou notice CLYDE appears to be nervous about something...");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkMagenta;
                                                            Console.WriteLine("[CLYDE:] So, um, next, we need to, uhh, go to the...the SECTION BEE MINUS SIX DELTA server room! Yes that's it!");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                            Console.WriteLine("\t\tDo you confront CLYDE about the other voice you heard or pretend to ignore it?");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            Console.ForegroundColor = ConsoleColor.DarkRed;
                                                            Console.WriteLine("\t<Y/N>");
                                                            Console.ForegroundColor = ConsoleColor.DarkCyan;
                                                            string doesUserConfrontOne = Console.ReadLine();
                                                            if (doesUserConfrontOne == "y" || doesUserConfrontOne == "Y" || doesUserConfrontOne == "Yes" || doesUserConfrontOne == "YES" || doesUserConfrontOne == "yes")
                                                            {
                                                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                                Console.WriteLine("\t\tYou ask CLYDE who the voice was...");
                                                                await System.Threading.Tasks.Task.Delay(2000);
                                                                Console.ForegroundColor = ConsoleColor.DarkMagenta;
                                                                Console.WriteLine("[CLYDE:] That was...ummm...that was a system malfunction, the...umm...vocal pronounciation system is a bit glitchy..."); //cover up I guess, nervous panicy
                                                                await System.Threading.Tasks.Task.Delay(2000);
                                                                Console.WriteLine("[CLYDE:] Right anyway! You coming to the server room?");
                                                                await System.Threading.Tasks.Task.Delay(2000);
                                                                Console.ForegroundColor = ConsoleColor.DarkRed;
                                                                Console.WriteLine("\t<Y/N>");
                                                                Console.ForegroundColor = ConsoleColor.DarkCyan;
                                                                string doesUserGoToServerRoomSectionBminusSixDelta = Console.ReadLine();
                                                                if (doesUserGoToServerRoomSectionBminusSixDelta == "y" || doesUserGoToServerRoomSectionBminusSixDelta == "Y" || doesUserGoToServerRoomSectionBminusSixDelta == "Yes" || doesUserGoToServerRoomSectionBminusSixDelta == "YES" || doesUserGoToServerRoomSectionBminusSixDelta == "yes")
                                                                {
                                                                    Console.ForegroundColor = ConsoleColor.DarkMagenta;
                                                                    Console.WriteLine("[CLYDE:] Great!");
                                                                    await System.Threading.Tasks.Task.Delay(2000);
                                                                }
                                                                else
                                                                {
                                                                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                                    Console.WriteLine("\t\tCome on, follow the story line...");
                                                                    await System.Threading.Tasks.Task.Delay(2000);
                                                                }
                                                            }
                                                            else
                                                            {
                                                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                                Console.WriteLine("\t\tAre you not curious? Not one bit?");
                                                                await System.Threading.Tasks.Task.Delay(2000);
                                                            }
                                                        }
                                                        else
                                                        {
                                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                            Console.WriteLine("\t\tPAY ATTENTION!");
                                                            await System.Threading.Tasks.Task.Delay(2000);
                                                            //ends
                                                        }
                                                    }
                                                    else
                                                    {
                                                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                        Console.WriteLine("\t\tPAY ATTENTION!");
                                                        await System.Threading.Tasks.Task.Delay(2000);
                                                        //ends
                                                    }
                                                }
                                                else
                                                {
                                                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                    Console.WriteLine("\t\tPAY ATTENTION!");
                                                    await System.Threading.Tasks.Task.Delay(2000);
                                                    //ends
                                                }
                                            }
                                            else
                                            {
                                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                                Console.WriteLine("\t\tPAY ATTENTION!");
                                                await System.Threading.Tasks.Task.Delay(2000);
                                                //ends
                                            }
                                        }
                                        else
                                        {
                                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                                            Console.WriteLine("\t\tPAY ATTENTION!");
                                            await System.Threading.Tasks.Task.Delay(2000);
                                            //ends
                                        }
                                    }
                                    else
                                    {
                                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                                        Console.WriteLine("\t\tPAY ATTENTION!");
                                        await System.Threading.Tasks.Task.Delay(2000);
                                        //ends
                                    }
                                }
                                else
                                {
                                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                                    Console.WriteLine("\t\tPAY ATTENTION!");
                                    await System.Threading.Tasks.Task.Delay(2000);
                                    //ends
                                }
                            }
                            else
                            {
                                Console.ForegroundColor = ConsoleColor.DarkYellow;
                                Console.WriteLine("\t\tPAY ATTENTION!");
                                await System.Threading.Tasks.Task.Delay(2000);
                                //ends
                            }
                        }
                        else
                        {
                            Console.ForegroundColor = ConsoleColor.DarkYellow;
                            Console.WriteLine("\t\tPAY ATTENTION!");
                            await System.Threading.Tasks.Task.Delay(2000);
                            //ends
                        }
                    }
                    else
                    {
                        Console.ForegroundColor = ConsoleColor.DarkYellow;
                        Console.WriteLine("\t\tPAY ATTENTION!");
                        await System.Threading.Tasks.Task.Delay(2000);
                        //ends
                    }
                }
                else
                {
                    Console.ForegroundColor = ConsoleColor.DarkYellow;
                    Console.WriteLine("\t\tPAY ATTENTION!");
                    await System.Threading.Tasks.Task.Delay(2000);
                    //ends
                }
            }
            else
            {
                Console.WriteLine("[CLYDE:] How rude! Well, you know what? I don't like you very much. In fact, I don't like you at all! Hmmph!");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] You what I do to people I don't like? Well, I don't talk to them any more");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("[CLYDE:] So goodbye and I hope you have a rotten day! \\('o')/");
                await System.Threading.Tasks.Task.Delay(0100);
            }

            //postload
            Console.ForegroundColor = ConsoleColor.DarkRed;
            Console.WriteLine("\n\t<Connection Terminated> \n\tPress 'ENTER' to exit");
            Console.ForegroundColor = ConsoleColor.DarkCyan;
            String userData = Console.ReadLine();
            if (userData == "sigCreator")
            {
                Console.ForegroundColor = ConsoleColor.DarkYellow;
                await System.Threading.Tasks.Task.Delay(1000);
                Console.WriteLine("\n\t\tThe creator of the game is the Co-President of All-Food-Nice, Wade Hát");
                await System.Threading.Tasks.Task.Delay(2000);
                Console.WriteLine("\t\t\tofficeofallfoodniceofficial.godaddysites.com");

                //logo? no brown =(
                await System.Threading.Tasks.Task.Delay(2000);

                Console.ForegroundColor = ConsoleColor.Black;

                Console.WriteLine("\n     ██╗ ██████╗ ██╗███╗   ██╗    ████████╗██╗  ██╗███████╗     ██████╗ ███████╗███████╗██╗ ██████╗███████╗██╗\n     ██║██╔═══██╗██║████╗  ██║    ╚══██╔══╝██║  ██║██╔════╝    ██╔═══██╗██╔════╝██╔════╝██║██╔════╝██╔════╝██║\n     ██║██║   ██║██║██╔██╗ ██║       ██║   ███████║█████╗      ██║   ██║█████╗  █████╗  ██║██║     █████╗  ██║\n██   ██║██║   ██║██║██║╚██╗██║       ██║   ██╔══██║██╔══╝      ██║   ██║██╔══╝  ██╔══╝  ██║██║     ██╔══╝  ╚═╝\n╚█████╔╝╚██████╔╝██║██║ ╚████║       ██║   ██║  ██║███████╗    ╚██████╔╝██║     ██║     ██║╚██████╗███████╗██╗\n ╚════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝       ╚═╝   ╚═╝  ╚═╝╚══════╝     ╚═════╝ ╚═╝     ╚═╝     ╚═╝ ╚═════╝╚══════╝╚═╝");

                Console.ForegroundColor = ConsoleColor.DarkYellow;
                await System.Threading.Tasks.Task.Delay(1000);

                Console.ReadLine();
            }
            else
            {
                Console.Write("\nto\\executable\\proticul\\defraz\\exe.send {userData} srvr42.22.01");
                await System.Threading.Tasks.Task.Delay(1000);
                Console.Write("\r                                                                         \n");
                await System.Threading.Tasks.Task.Delay(3000);
            }
            Console.ForegroundColor = ConsoleColor.Gray;
        }
    }
}
