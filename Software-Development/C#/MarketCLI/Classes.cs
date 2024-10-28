using static MarketCLI.MarketCLI;

namespace Classes
{
    /* public class User is used to initialize the user
       takes 2 arguments: string name, float money */
    public class User(string name, float money)
    {
        public string Name = name;
        public float Money = money;
        public List<Item> Inventory = new List<Item>();

        public void DisplayInventory()
        {
            /* Get the max string length of the name and cost from the items */
            int maxNameLength = 0;
            int maxCostLength = 0;
            for (int i = 0; i < this.Inventory.Count; i++)
            {
                Item item = this.Inventory[i];
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
            for (int i = 0; i < this.Inventory.Count; i++)
            {
                Item item = this.Inventory[i];

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
            Console.Write("\n");
        }
    }

    public class Item(string name, float cost)
    {
        public string Name = name;
        public float Cost = cost;
    }

    /* public class Vendor is the class used when initializing a new vendor in the market that has a name and inventory
           takes 2 arguments: string name, Dictionary<string, float> inventory */
    public class Vendor(string name, string profession, List<Item> inventory)
    {
        public string Name = name;
        public string Profession = profession;
        public List<Item> Inventory = inventory;

        public void DisplayInventory()
        {
            /* Get the max string length of the name and cost from the items */
            int maxNameLength = 0;
            int maxCostLength = 0;
            for (int i = 0; i < this.Inventory.Count; i++)
            {
                Item item = this.Inventory[i];
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
            for (int i = 0; i < this.Inventory.Count; i++)
            {
                Item item = this.Inventory[i];

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
            Console.Write("\n");
        }
    }
}