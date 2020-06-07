using System;
using System.Windows.Forms;

namespace RunShellcode
{
    public partial class MainWindow : Form
    {
        public MainWindow()
        {
            InitializeComponent();
        }

        private void buttonRunShellcode_Click(object sender, EventArgs e)
        {
            try
            {
                Shellcode.Run(richTextShellcode.Text, true);
            }
            catch (Exception ex)
            {
                MessageBox.Show(ex.Message, "Error", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }
    }
}
