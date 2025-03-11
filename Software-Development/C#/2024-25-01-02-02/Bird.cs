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

        private Nest _nest = new Nest();
        public Nest? Nest { get; set; } = null;

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
                return _type;
            }
            set {
                if (ValidBirds.Contains(value))
                {
                    _type = value;
                }
                else
                {
                    MessageBox.Show("Invalid bird specified! - " + value);
                }
            }
        }

        #endregion

        #region methods

        public Nest BuildNest()
        {
            Nest nest = new Nest();
            Nest = nest;
            return nest;
        }
        #endregion
    }

    public class Nest
    { 
    
    }
}
