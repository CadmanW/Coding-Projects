namespace Classes
{


    // public class User is used to initialize the user
    // takes 2 arguments: string name, float money
    public class User(string name, float money)
    {
        private string name = name;
        private List<Item> inventory = new List<Item>()
        {
            new Item("money", money)
        };

        public string Name
        {
            get { return name; }
            private set { name = value; }
        }

        public List<Item> Inventory()
        {
            return inventory;
        }
        
    }

    public class Item(string name, float cost)
    {
        public string Name = name;
        public float Cost = cost;
    }

    // public class Vendor is used to initialize a vendor
    // takes 2 arguments: string name, Dictionary<string, float> inventory
    public class Vendor(string name, string profession, List<Item> inventory)
    {
        public string Name = name;
        public string Profession = profession;
        public List<Item> Inventory = inventory;

    }


}