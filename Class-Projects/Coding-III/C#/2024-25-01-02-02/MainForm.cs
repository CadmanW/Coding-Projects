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
                            string[] input = strNumber.Trim().Split(" ");
                            string min = input[0];
                            string max = input[1];
                        }
                        catch (FormatException fe)
                        {
                            MessageBox.Show("nice try, moron!");
                            Debug.WriteLine(fe);
                        }
                        catch (Exception ex)
                        {
                            MessageBox.Show(ex.ToString());
                            Debug.WriteLine(ex);
                        }
                    }
                }
            }
        }

        private void ShowEnumerationButton_Click(object sender, EventArgs e)
        {
            DayOfWeek dayOfweek = DayOfWeek.Monday;

            switch (dayOfweek)
            {
                case DayOfWeek.Sunday:
                    break;
                case DayOfWeek.Monday:
                    break;
                case DayOfWeek.Tuesday:
                    break;
                case DayOfWeek.Wednesday:
                    break;
                case DayOfWeek.Thursday:
                    break;
                case DayOfWeek.Friday:
                    break;
                case DayOfWeek.Saturday:
                    break;
                default:
                    MessageBox.Show("Unkown day of week!");
                    break;
            }

            Month currentMonth = Month.December;

            switch (currentMonth)
            {
                case Month.January:
                    break;
                case Month.Febuary:
                    break;
                case Month.March:
                    break;
                case Month.April:
                    break;
                case Month.May:
                    break;
                case Month.June:
                    break;
                case Month.July:
                    break;
                case Month.August:
                    break;
                case Month.September:
                    break;
                case Month.October:
                    break;
                case Month.November:
                    break;
                case Month.December:
                    MessageBox.Show("The month is December");
                    break;
            }
        }

        private void ShowBirdButton_Click(object sender, EventArgs e)
        {
            Bird easternBlueBird = new Bird();
            easternBlueBird.Type = "Eastern Bluebird";
            MessageBox.Show(easternBlueBird.Type);

            Bird bluejay = new Bird();
            bluejay.Type = "German Shepard";
            MessageBox.Show(bluejay.Type);
        }

        public enum DayOfWeek
        {
            Sunday,
            Monday,
            Tuesday,
            Wednesday,
            Thursday,
            Friday,
            Saturday
        }

        public enum Month
        {
            January,
            Febuary,
            March,
            April,
            May,
            June,
            July,
            August,
            September,
            October,
            November,
            December
        }
    }
}