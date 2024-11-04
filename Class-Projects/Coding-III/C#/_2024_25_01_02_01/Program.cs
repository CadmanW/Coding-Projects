using System.Runtime.CompilerServices;

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
        // constructor methods
        public Player()
        {
            Name = "";
            Ability = "";
        }
        public Player(string playerName)
        {
            Name = playerName;
            Ability = "";
        }

        private string name = "";

        // properties ok...
        public string Name
        {
            get { return Name; }
            set
            {
                // check input and test for correct case
            }
        }

        public string Ability { get; set; }

        // method (behavior)
        public void Attack()
        {

        }
    }
}