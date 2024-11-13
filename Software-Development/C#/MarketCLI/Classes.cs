namespace Classes
{
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

        // Public Methods
        public void Buy(Item item, Vendor vendor)
        {
            Inventory.Items[0].Cost -= item.Cost;
            Inventory.Items.Add(item);

            vendor.Inventory.Items[0].Cost += item.Cost;
            vendor.Inventory.Items.Remove(item);

            Console.WriteLine(String.Format("{0} bought {1} from {2} for {3}$", Name, item.Name, vendor, item.Cost));
            Console.WriteLine(String.Format("{0} has {1}$ left", Name, Inventory.Items[0].Cost));
            Console.WriteLine(String.Format("{0} now has {1}$"), vendor.Name, vendor.Inventory.Items[0].Cost);
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

        public void Display()
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
        }
    }

    public class Item(string name, float cost)
    {
        // Private variables
        private string _name = name;
        private float _cost = cost;

        // Public properties
        public string Name
        {
            get { return _name; }
            private set { _name = value; }
        }
        public float Cost
        {
            get { return _cost; }
            internal set { _cost = value; }
        }

        public override string ToString()
        {
            return name;
        }
    }
}