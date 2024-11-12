namespace Classes
{
    public class Inventory(List<Item> items)

    public class User(string name, float money)
    {
        // Private variables
        private string name = name;
        private List<Item> inventory = new List<Item>()
        {
            new Item("money", money)
        };


        // Public properties
        public string Name
        {
            get { return name; }
            private set { name = value; }
        }

        public List<Item> Inventory
        {
            get { return inventory; }
            private set { inventory = value; }
        }

        public override string ToString()
        {
            return name;
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

    public class Vendor(string name, string profession, List<Item> inventory)
    {
        // Private variables
        private string name = name;
        private string profession = profession;
        private List<Item> inventory = inventory;

        // Public properties
        public string Name
        {
            get { return name; }
            private set { name = value; }
        }

        public string Profession
        {
            get { return profession; }
            private set { profession = value; }
        }

        public List<Item> Inventory
        {
            get { return inventory; }
            private set { inventory = value; }
        }

        public override string ToString()
        {
            return String.Format("name: {0} profession: {1}", name, profession);
        }
    }
}