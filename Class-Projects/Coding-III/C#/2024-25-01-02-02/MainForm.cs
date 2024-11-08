using System.Diagnostics;
using System.Drawing.Text;

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
            evenOddForm.StartPosition = FormStartPosition.CenterParent;
            evenOddForm.ShowDialog(this);
        }

        private Form fizzBuzzForm;
        private Label NumberLabel;
        private TextBox NumberTextBox;
        private Button RunButton;
        private Label ResultLabel;

        private void LaunchFizzBuzzFormButton_Click(object sender, EventArgs e)
        {
            // create a new form
            fizzBuzzForm = new Form();
            fizzBuzzForm.Text = "FizzBuzz";
            fizzBuzzForm.StartPosition = FormStartPosition.CenterParent;

            // Create the number label and add it to the form
            Label NumberLabel = new Label();
            NumberLabel.Text = "Number: ";
            NumberLabel.Size = new Size(60, NumberLabel.Size.Height);
            fizzBuzzForm.Controls.Add(NumberLabel);

            // create the textbox and add it to the form
            NumberTextBox = new TextBox();
            NumberTextBox.Location = new Point(60, 0);
            fizzBuzzForm.Controls.Add(NumberTextBox);

            // create the button and add it to the form
            RunButton = new Button();
            RunButton.Text = "Run";
            fizzBuzzForm.Controls.Add(RunButton);
            RunButton.Location = new Point(NumberLabel.Width + NumberTextBox.Width, 0);
            RunButton.Click += RunButton_Click;

            // create the result label and add it to the form
            ResultLabel = new Label();
            ResultLabel.Text = "THIS_WILL_POPULATE_DYNAMICALLY";
            ResultLabel.Location = new Point(0, NumberTextBox.Size.Height);
            fizzBuzzForm.Controls.Add(ResultLabel);

            // Show the form
            fizzBuzzForm.ShowDialog(this);
        }

        private void RunButton_Click(object sender, EventArgs e)
        {
            // fizz buzz algorithm, then update reult label
        }
    }
}