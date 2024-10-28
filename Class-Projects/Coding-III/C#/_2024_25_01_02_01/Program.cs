namespace _2024_25_01_02_01
{
    public class Program
    {
        private int playerScore = 100;


        static void Main(string[] args)
        {
            Player newPlayer = new Player();
            newPlayer.Attack();
            newPlayer.Name = "CASEY DIYA";
            Console.WriteLine(newPlayer.Name);

            Player playerTwo = new Player("player two");
        }

        static void SayHi()
        {

        }
	}

    class Player
    {
        // this is referred to as a FIELD
        // a variable inside a class
        private string name = "";

        // constructor methods
        public Player()
        {
            Name = name;
        }
        public Player(string playerName)
        {
            Name = playerName;
        }

        // properties ok...
        // creates a "getter" and a "setter"
        public string Name
        {
            get { return name; }
            set { // TODO: implement Name setter....
        }

        // method (behavior)
        public void Attack()
        {

        }
    }
}