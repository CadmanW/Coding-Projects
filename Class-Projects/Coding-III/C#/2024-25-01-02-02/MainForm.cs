using System.Diagnostics;

namespace _2024_25_01_02_02
{
    public partial class MainForm : Form
    {
        public MainForm()
        {
            InitializeComponent();
        }

        private void LaunchEvenOddFormButton_Click(object sender, EventArgs e)
        {
            EvenOddForm evenOddForm = new EvenOddForm();
            evenOddForm.Parent = this;
            evenOddForm.StartPosition = FormStartPosition.CenterParent;
            evenOddForm.Show();
        }
    }
}