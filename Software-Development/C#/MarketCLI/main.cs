using Classes;
using System.Diagnostics;

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
            string? name = Console.ReadLine();
            if (name == null)
            {
                name = "Guest";
            };

            return new User(name, new Inventory(new List<Item> 
            {
                new Item("money", 1000.00f)
            }));
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

                new Inventory(new List<Item>
                {
                    new Item("Money", 1000.00f),
                    new Item("Apple", 1.19f),
                    new Item("Potato", 0.79f),
                    new Item("Beetroot", 0.69f),
                    new Item("Loaf of Bread", 4.99f)
                })
            ));

            vendors.Add(new Vendor(
                "Kenzie",

                "Potter",

                new Inventory(new List<Item>
                {
                    new Item("Money", 1000.00f),
                    new Item("bowl", 9.99f),
                    new Item("mug", 3.99f),
                    new Item("plate", 8.99f)
                })
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
                
            string? input = Console.ReadLine().ToLower().Trim();

            if (input != null)
            {
                string[] splitInput = input.Split(' ');

                if (splitInput[0] == "display" && splitInput[splitInput.Length - 1] == "vendors")
                {
                    DisplayVendors(vendors);
                }
                else if (splitInput[0] == "display" && splitInput[splitInput.Length - 1] == "inventory")
                {
                    if (splitInput.Length == 2)
                    {
                        user.Inventory.Display();
                    }
                    else
                    {
                        Vendor vendor =
                            (from v in vendors
                            where (String.Format("{0} the {1}", v.Name.ToLower(), v.Profession.ToLower()).Contains(splitInput[1]))
                            select v)
                            .ToList()[0];

                        vendor.Inventory.Display();
                    }

                }
                else if (splitInput[0] == "buy")
                {
                    string itemName = input.Split("from")[0][3..].Trim();
                    string vendorName = input.Split("from")[1].Trim();


                    Vendor vendor =
                        (from v in vendors
                         where (String.Format("{0} the {1}", v.Name.ToLower(), v.Profession.ToLower()).Contains(vendorName))
                         select v)
                        .ToList()[0];

                    Item item =
                        (from i in vendor.Inventory.Items
                         where i.Name.ToLower().Contains(itemName)
                         select i)
                         .ToList()[0];

                    user.Buy(item, vendor);
                }
                else if (splitInput[0] == "quit")
                {
                    return false;
                }
            }
            return true;
        }
    }
}