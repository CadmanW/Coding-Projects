namespace Classes
{
    public class Inventory(List<Item> items)
    {
        // Private variables
        private List<Item> _items = items;

        // Public properties / methods
        public List<Item> Items
        {
            get { return _items; }
            private set { _items = value; }
        }

        public override string ToString()
        {
            Console.WriteLine();
            /* Get the max string length of the name and cost from the items */
            int maxNameLength = 0;
            int maxCostLength = 0;
            for (int i = 0; i < _items.Count; i++)
            {
                Item item = _items[i];
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
            for (int i = 0; i < _items.Count; i++)
            {
                Item item = _items[i];

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

            return "";
        }
    }

    public class User(string name, Inventory inventory)
    {
        // Private variables
        private string _name = name;
        private Inventory _inventory = inventory;


        // Public properties
        public string Name
        {
            get { return _name; }
            private set { _name = value; }
        }

        public Inventory Inventory
        {
            get { return _inventory; }
            private set { _inventory = value; }
        }

        public override string ToString()
        {
            return _name;
        }
    }

    public class Item(string name, float cost)
    {
        // Private variables
        private string name = name;
        private float cost = cost;

        // Public properties
        public string Name
        {
            get { return name; }
            private set { name = value; }
        }
        public float Cost
        {
            get { return cost; }
            private set { cost = value; }
        }

        public override string ToString()
        {
            return String.Format("name: {0} cost: {1}", name, cost);
        }
    }

    public class Vendor(string name, string profession, Inventory inventory)
    {
        // Private variables
        private string _name = name;
        private string _profession = profession;
        private Inventory _inventory = inventory;

        // Public properties
        public string Name
        {
            get { return _name; }
            private set { _name = value; }
        }

        public string Profession
        {
            get { return _profession; }
            private set { _profession = value; }
        }

        public Inventory Inventory
        {
            get { return _inventory; }
            private set { _inventory = value; }
        }

        public override string ToString()
        {
            return String.Format("name: {0} profession: {1}", _name, _profession);
        }
    }
}