using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2024_25_01_02_02
{
    public class Bird
    {
        private List<string> ValidBirds = new List<string>();

        private string _type = "";

        public string Type
        {
            get { return _type; }
            set
            {
                if (ValidBirds.Contains(value))
                {
                    _type = value;
                }
                else
                {
                    MessageBox.Show("Invalid bird specified!");
                }
            }
        }

        // Constructor
        public Bird()
        {
            ValidBirds.Add("Eastern Bluebird");
            ValidBirds.Add("American Crow");
            ValidBirds.Add("Red-Headed Woodpecker");
            Type = "";
        }
    }
}
