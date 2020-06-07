namespace RunShellcode
{
    partial class MainWindow
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
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

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            System.ComponentModel.ComponentResourceManager resources = new System.ComponentModel.ComponentResourceManager(typeof(MainWindow));
            this.tableLayoutPanel1 = new System.Windows.Forms.TableLayoutPanel();
            this.richTextShellcode = new System.Windows.Forms.RichTextBox();
            this.buttonRunShellcode = new System.Windows.Forms.Button();
            this.tableLayoutPanel1.SuspendLayout();
            this.SuspendLayout();
            // 
            // tableLayoutPanel1
            // 
            this.tableLayoutPanel1.ColumnCount = 1;
            this.tableLayoutPanel1.ColumnStyles.Add(new System.Windows.Forms.ColumnStyle());
            this.tableLayoutPanel1.Controls.Add(this.buttonRunShellcode, 0, 1);
            this.tableLayoutPanel1.Controls.Add(this.richTextShellcode, 0, 0);
            this.tableLayoutPanel1.Dock = System.Windows.Forms.DockStyle.Fill;
            this.tableLayoutPanel1.Location = new System.Drawing.Point(0, 0);
            this.tableLayoutPanel1.Margin = new System.Windows.Forms.Padding(0);
            this.tableLayoutPanel1.Name = "tableLayoutPanel1";
            this.tableLayoutPanel1.RowCount = 2;
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Percent, 100F));
            this.tableLayoutPanel1.RowStyles.Add(new System.Windows.Forms.RowStyle(System.Windows.Forms.SizeType.Absolute, 35F));
            this.tableLayoutPanel1.Size = new System.Drawing.Size(482, 253);
            this.tableLayoutPanel1.TabIndex = 0;
            // 
            // richTextShellcode
            // 
            this.richTextShellcode.BackColor = System.Drawing.Color.Black;
            this.richTextShellcode.Dock = System.Windows.Forms.DockStyle.Fill;
            this.richTextShellcode.Font = new System.Drawing.Font("Consolas", 10.2F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.richTextShellcode.ForeColor = System.Drawing.Color.FromArgb(((int)(((byte)(32)))), ((int)(((byte)(194)))), ((int)(((byte)(14)))));
            this.richTextShellcode.Location = new System.Drawing.Point(3, 3);
            this.richTextShellcode.Name = "richTextShellcode";
            this.richTextShellcode.Size = new System.Drawing.Size(476, 212);
            this.richTextShellcode.TabIndex = 1;
            this.richTextShellcode.Text = "";
            // 
            // buttonRunShellcode
            // 
            this.buttonRunShellcode.Dock = System.Windows.Forms.DockStyle.Fill;
            this.buttonRunShellcode.Location = new System.Drawing.Point(3, 221);
            this.buttonRunShellcode.Name = "buttonRunShellcode";
            this.buttonRunShellcode.Size = new System.Drawing.Size(476, 29);
            this.buttonRunShellcode.TabIndex = 0;
            this.buttonRunShellcode.Text = "Run Shellcode";
            this.buttonRunShellcode.UseVisualStyleBackColor = true;
            this.buttonRunShellcode.Click += new System.EventHandler(this.buttonRunShellcode_Click);
            // 
            // MainWindow
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(8F, 16F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(482, 253);
            this.Controls.Add(this.tableLayoutPanel1);
            this.Icon = ((System.Drawing.Icon)(resources.GetObject("$this.Icon")));
            this.Name = "MainWindow";
            this.Text = "RunShellcode";
            this.tableLayoutPanel1.ResumeLayout(false);
            this.ResumeLayout(false);

        }

        #endregion

        private System.Windows.Forms.TableLayoutPanel tableLayoutPanel1;
        private System.Windows.Forms.RichTextBox richTextShellcode;
        private System.Windows.Forms.Button buttonRunShellcode;
    }
}

