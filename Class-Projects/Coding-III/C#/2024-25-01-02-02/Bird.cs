using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace _2024_25_01_02_02
{
    public class Bird
    {
        #region properties

        private List<string> _validBirds = new List<string>();
        public List<string> ValidBirds
        {
            get
            {
                return _validBirds;
            }
            private set
            {
                _validBirds = value;
            }
        }
        private string _type = "";
        public string Type
        {
            get {
                if (DateTime.Now.Hour != 12)
                {
                    MessageBox.Show("Cannot read this property until 12 :)");
                    return null;
                }
                else
                {
                    return _type;
                }
              
            }
            set {
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

        #endregion

        #region constructor

        public Bird()
        {
            ValidBirds.Add("Eastern Bluebird");
            ValidBirds.Add("American Crow");
            ValidBirds.Add("Red-Headed Woodpecker");
            Type = "";
        }
        #endregion
    }
}
