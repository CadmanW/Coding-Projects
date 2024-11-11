using Classes;

namespace MarketCLI
{
    public class MarketCLI
    {
        static void Main(string[] args)
        {
            // Initialize user and vendors
            User user = InitUser();
            List<Vendor> vendors = InitVendors();
            
            // Display the intro
            DisplayIntro(user, vendors);

            // Start the Application
            bool play = true;
            while (play) 
            {
                play = GameLoop(user, vendors);
            }
        }










        // static method InitUser initializes the user
        // takes 0 arguments
        // returns an instance of the User class
        public static User InitUser()
        {
            Console.WriteLine("What's your name? ");
            string name = Console.ReadLine();
            if (name == null)
            {
                name = "Guest";
            }

            return new User(name, 1000.00f);
        }

        // static method InitVendors initializes the vendors
        // takes 0 arguments
        // returns an array of Vendor class instances
        public static List<Vendor> InitVendors()
        {
            List<Vendor> vendors = new List<Vendor>();

            vendors.Add(new Vendor(
                "Jerry",
                "Farmer",
                new List<Item>
                {
                    new Item("Apple", 1.19f),
                    new Item("Potato", 0.79f),
                    new Item("Beetroot", 0.69f),
                    new Item("Loaf of Bread", 4.99f)
                }
            ));

            vendors.Add(new Vendor(
                "Kenzie",
                "Potter",
                new List<Item>
                {
                    new Item("bowl", 9.99f),
                    new Item("mug", 3.99f),
                    new Item("plate", 8.99f)
                }
            ));

            return vendors;
        }

        // static method DisplayIntro displays the intro to the market
        // takes 1 argument: User
        // returns nothing
        public static void DisplayIntro(User user, List<Vendor> vendors)
        {
            Console.Write("\n");
            for (int i = 0; i < (user.Name.Length + 26); i++)
            {
                Console.Write('-');
            }
            Console.Write(String.Format("\n| WELCOME TO THE MARKET {0} |\n", user.Name));
            for (int i = 0; i < (user.Name.Length + 26); i++)
            {
                Console.Write('-');
            }
            Console.Write("\n\n");

            Console.WriteLine("Vendors currently in the market:");
            DisplayVendors(vendors);
        }

        // static method DisplayVendors displays all vendors in the market
        // takes 1 argument: List<Vendor>
        // returns nothing
        public static void DisplayVendors(List<Vendor> vendors)
        {
            for (int i = 0; i < vendors.Count; i++)
            {
                Vendor vendor = vendors[i];
                Console.WriteLine(String.Format("- {0} the {1}", vendor.Name, vendor.Profession));
            }
            Console.Write("\n");
        }

        // static method GameLoop is the main game loop that starts after user and vendors initialization
        // takes 2 arguments: User, List<Vendor>
        // returns False if the user wants to quit the application, true if use wants to continue
        public static bool GameLoop(User user, List<Vendor> vendors)
        {
            Console.Write("""
                What would you like to do?
                - display vendors,
                - display inventory,
                - display <vendor name> inventory,
                - buy <item name> from <vendor name>,
                - quit

                > 
                """);
                
            string[] input = Console.ReadLine().ToLower().Trim().Split(' ');

            if (input[0] == "display" && input[input.Length - 1] == "vendors")
            {
                DisplayVendors(vendors);
            }
            else if (input[0] == "display" && input[input.Length - 1] == "inventory")
            {
                if (input.Length == 2)
                {
                    DisplayInventory(user.Inventory);
                }
                else
                {
                    Vendor vendor =
                        (from v in vendors
                        where (String.Format("{0} the {1}", v.Name.ToLower(), v.Profession.ToLower()).Contains(input[1]))
                        select v)
                        .ToList()[0];

                    DisplayInventory(vendor.Inventory);
                }

            }
            else if (input[0] == "buy")
            {
                string parsedInput = "";

                for (int i = 1; i < input.Length - 1; i++)
                {
                    parsedInput += input[i] + " ";
                }

                Console.WriteLine(parsedInput);

                List<Vendor> vendor =
                    (from v in vendors
                     where (String.Format("{0} the {1}", v.Name.ToLower(), v.Profession.ToLower()).Contains(parsedInput))
                     select v)
                    .ToList();

                Console.WriteLine(vendor[0]);

            }
            else if (input[0] == "quit")
            {
                return false;
            }

            return true;
        }

        // static method DisplayInventory displays the inventory passed into it
        // takes 1 argument: List<Item>
        // returns nothing
        public static void DisplayInventory(List<Item> inventory)
        {
            Console.WriteLine();
            /* Get the max string length of the name and cost from the items */
            int maxNameLength = 0;
            int maxCostLength = 0;
            for (int i = 0; i < inventory.Count; i++)
            {
                Item item = inventory[i];
                int nameLength = item.Name.Length;
                int costLength = item.Cost.ToString().Length;

                if (nameLength > maxNameLength)
                {
                    maxNameLength = nameLength;
                }

                if (nameLength % 2 == 1)
                {
                    maxNameLength++;
                }

                if (costLength < maxCostLength)
                {
                    maxCostLength = costLength;
                }

                if (costLength % 2 == 1)
                {
                    maxCostLength++;
                }
            }

            /* Table header */
            for (int i = 0; i < (maxNameLength + maxCostLength + 11); i++)
            {
                Console.Write('-');
            }

            Console.Write("\n| ");
            for (int i = 0; i < ((maxNameLength - 4) / 2); i++)
            {
                Console.Write(' ');
            }
            Console.Write("Item");
            for (int i = 0; i < ((maxNameLength - 4) / 2); i++)
            {
                Console.Write(' ');
            }
            Console.Write(" | ");
            for (int i = 0; i < ((maxCostLength - 4) / 2); i++)
            {
                Console.Write(' ');
            }
            Console.Write("Cost");
            for (int i = 0; i < ((maxCostLength - 4) / 2); i++)
            {
                Console.Write(' ');
            }
            Console.Write(" |\n");

            for (int i = 0; i < (maxNameLength + maxCostLength + 11); i++)
            {
                Console.Write('-');
            }

            /* Table Contents */
            for (int i = 0; i < inventory.Count; i++)
            {
                Item item = inventory[i];

                Console.Write(String.Format("\n| {0}", item.Name));
                for (int x = 0; x < (maxNameLength - item.Name.Length); x++)
                {
                    Console.Write(' ');
                }
                Console.Write(String.Format(" | {0}", item.Cost.ToString()));
                for (int x = 0; x < (maxCostLength - item.Name.Length); x++)
                {
                    Console.Write(' ');
                }
                Console.Write(" |");
            }

            Console.Write("\n");
            for (int i = 0; i < (maxNameLength + maxCostLength + 11); i++)
            {
                Console.Write('-');
            }
            Console.Write("\n\n");
            
        }
    }
}