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
            LaunchEvenOddFormButton = new Button();
            SuspendLayout();
            // 
            // LaunchEvenOddFormButton
            // 
            LaunchEvenOddFormButton.Location = new Point(12, 12);
            LaunchEvenOddFormButton.Name = "LaunchEvenOddFormButton";
            LaunchEvenOddFormButton.Size = new Size(233, 59);
            LaunchEvenOddFormButton.TabIndex = 0;
            LaunchEvenOddFormButton.Text = "Launch Even Odd Form";
            LaunchEvenOddFormButton.UseVisualStyleBackColor = true;
            LaunchEvenOddFormButton.Click += LaunchEvenOddFormButton_Click;
            // 
            // MainForm
            // 
            AutoScaleDimensions = new SizeF(10F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(578, 344);
            Controls.Add(LaunchEvenOddFormButton);
            Margin = new Padding(4, 5, 4, 5);
            Name = "MainForm";
            StartPosition = FormStartPosition.CenterScreen;
            Text = "C# Learning Dashboard";
            ResumeLayout(false);
        }

        private Button LaunchEvenOddFormButton;
    }
}
