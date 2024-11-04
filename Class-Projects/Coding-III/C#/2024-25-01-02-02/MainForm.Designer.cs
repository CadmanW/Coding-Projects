namespace _2024_25_01_02_02
{
    partial class MainForm
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        private void InitializeComponent()
        {
            button1 = new Button();
            FizzBuzz = new Button();
            SuspendLayout();
            // 
            // button1
            // 
            button1.Location = new Point(12, 12);
            button1.Name = "button1";
            button1.Size = new Size(187, 98);
            button1.TabIndex = 0;
            button1.Text = "Even / Odd";
            button1.UseVisualStyleBackColor = true;
            button1.Click += button1_Click;
            // 
            // FizzBuzz
            // 
            FizzBuzz.Location = new Point(205, 12);
            FizzBuzz.Name = "FizzBuzz";
            FizzBuzz.Size = new Size(187, 98);
            FizzBuzz.TabIndex = 1;
            FizzBuzz.Text = "FizzBuzz";
            FizzBuzz.UseVisualStyleBackColor = true;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(657, 367);
            Controls.Add(FizzBuzz);
            Controls.Add(button1);
            Margin = new Padding(4, 5, 4, 5);
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "C# Learning Dashboard";
            ResumeLayout(false);
        }

        private Button button1;
        private Button FizzBuzz;
    }
}
