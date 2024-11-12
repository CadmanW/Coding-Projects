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

        private void LaunchFizzBuzzFormButton_Click(object sender, EventArgs e)
        {
            // create a new form
            Form fizzBuzzForm = new Form();
            fizzBuzzForm.Text = "FizzBuzz";
            fizzBuzzForm.StartPosition = FormStartPosition.CenterParent;

            // Create the number label and add it to the form
            Label numberLabel = new Label();
            numberLabel.Text = "Number: ";
            numberLabel.Size = new Size(60, numberLabel.Size.Height);
            fizzBuzzForm.Controls.Add(numberLabel);

            // create the textbox and add it to the form
            TextBox numberTextBox = new TextBox();
            numberTextBox.Location = new Point(60, 0);
            fizzBuzzForm.Controls.Add(numberTextBox);

            // create the button and add it to the form
            Button runButton = new Button();
            runButton.Text = "Run";
            fizzBuzzForm.Controls.Add(runButton);
            runButton.Location = new Point(numberLabel.Width + numberTextBox.Width, 0);
            runButton.Click += RunButton_Click;

            // create the result label and add it to the form
            Label resultLabel = new Label();
            resultLabel.Text = "THIS_WILL_POPULATE_DYNAMICALLY";
            resultLabel.Location = new Point(0, numberTextBox.Size.Height);
            fizzBuzzForm.Controls.Add(resultLabel);

            // Show the form
            fizzBuzzForm.ShowDialog(this);
        }

        private void RunButton_Click(object? sender, EventArgs e)
        {
            Button? runButton = sender as Button;
            if (runButton != null)
            {
                Form? fizzBuzzForm = runButton.Parent as Form;
                if (fizzBuzzForm != null)
                {
                    TextBox? numberTextBox = fizzBuzzForm.Controls[1] as TextBox;
                    if (numberTextBox != null)
                    {
                        string strNumber = numberTextBox.Text;
                        try
                        {
                            int number = int.Parse(strNumber);
                        }
                        catch (Exception err)
                        {
                            Debug.WriteLine(err);
                        }
                    }
                }
            }
        }
    }
}