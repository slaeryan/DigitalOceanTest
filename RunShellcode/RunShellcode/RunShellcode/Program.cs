using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace RunShellcode
{
    static class Program
    {
        /// <summary>
        /// The main entry point for the application.
        /// </summary>
        [STAThread]
        static void Main()
        {
            AppDomain.CurrentDomain.UnhandledException += RestartProgram;
   
            Application.EnableVisualStyles();
            Application.SetCompatibleTextRenderingDefault(false);
            Application.Run(new MainWindow());
        }

        // todo: this doesn't work, need to fork monitor child process.
        private static void RestartProgram(object sender, UnhandledExceptionEventArgs e)
        {
            string info = e.ExceptionObject.ToString();

            MessageBox.Show("The program will now restart.", "Shellcode Crash", MessageBoxButtons.OK, MessageBoxIcon.Exclamation);

            System.Diagnostics.Process.Start(
                System.Reflection.Assembly.GetEntryAssembly().Location,
                string.Join(" ", Environment.GetCommandLineArgs()));
            Environment.Exit(1);
        }
    }
}
