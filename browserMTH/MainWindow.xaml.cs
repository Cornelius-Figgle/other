using Microsoft.Win32; using System; using System.Collections.Generic; using System.Linq; using System.Reflection; using System.Reflection.Metadata; using System.Security.Policy; using System.Text; using System.IO; using System.Threading.Tasks; using System.Threading; using System.Windows; using System.Windows.Controls; using System.Windows.Data; using System.Windows.Documents; using System.Windows.Input; using System.Windows.Media; using System.Windows.Media.Imaging; using System.Windows.Navigation; using System.Windows.Shapes; using static System.Net.Mime.MediaTypeNames;  using System.Printing; using System.Diagnostics; using System.Windows.Controls.Primitives;using System.Timers;

namespace browserMTH { public partial class MainWindow : Window {
        //public static class Globals {public static string temp;}
        //private static bool willNavigate;
        public static DateTime Now { get; }
        public MainWindow() { InitializeComponent(); HideScriptErrors(webBrowser, true); webBrowser.Navigate(Properties.Settings.Default.homePage); }
        /*Hides Errors Code */
        public void HideScriptErrors(WebBrowser wb, bool Hide)
        {
            FieldInfo fiComWebBrowser = typeof(WebBrowser)
                .GetField("_axIWebBrowser2",
                          BindingFlags.Instance | BindingFlags.NonPublic);
            if (fiComWebBrowser == null) return;
            object objComWebBrowser = fiComWebBrowser.GetValue(wb);
            if (objComWebBrowser == null) return;
            objComWebBrowser.GetType().InvokeMember(
                "Silent", BindingFlags.SetProperty, null, objComWebBrowser,
                new object[] { Hide });
        }
        public void updateDateTime() { timeBox.Text = DateTime.UtcNow.ToString("HH:mm:ss"); dateBox.Text = DateTime.UtcNow.ToString("yyyy-MM-dd"); }


        private void mouseInBox(object sender, RoutedEventArgs e) { /*URL_Box.Text = webBrowser.Source.ToString();*/ URL_Box.SelectAll(); }
        private void OnKeyDownHandler(object sender, KeyEventArgs e) {  if (string.IsNullOrEmpty(URL_Box.Text)) {; } else { if (e.Key == Key.Return) { { try { webBrowser.Navigate(URL_Box.Text); URL_Box.Text = webBrowser.Source.ToString(); } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } } } else {; } } }
        private void searchButtonClick(object sender, RoutedEventArgs e) { if (string.IsNullOrEmpty(URL_Box.Text)) {; } else { try {webBrowser.Navigate(URL_Box.Text); URL_Box.Text = webBrowser.Source.ToString(); } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } } }
        private void backButtonClick(object sender, RoutedEventArgs e) { try { webBrowser.GoBack();} catch {; } }
        private void nextButtonClick(object sender, RoutedEventArgs e) { try { webBrowser.GoForward(); } catch {; } }
        private void reloadButtonClick(object sender, RoutedEventArgs e) { webBrowser.Refresh(); URL_Box.Text = webBrowser.Source.ToString(); }
        private void homeButtonClick(object sender, RoutedEventArgs e) { webBrowser.Navigate(Properties.Settings.Default.homePage); URL_Box.Text = Properties.Settings.Default.homePage; }
        private void editHomeSite(object sender, RoutedEventArgs e) { Properties.Settings.Default.homePage = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void newWindow(object sender, RoutedEventArgs e) { string str = @"C:\Users\Max.Harrison\source\py\browserMTH\bin\Debug\net5.0-windows\browserMTH.exe"; Process process = new Process(); process.StartInfo.FileName = str; process.Start(); }

        private void bookmarkOneClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkOne); URL_Box.Text = Properties.Settings.Default.userBookmarkOne; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkOne(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkOne = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkTwoClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkTwo); URL_Box.Text = Properties.Settings.Default.userBookmarkTwo; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkTwo(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkTwo = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkThreeClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkThree); URL_Box.Text = Properties.Settings.Default.userBookmarkThree; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkThree(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkThree = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkFourClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkFour); URL_Box.Text = Properties.Settings.Default.userBookmarkFour; } catch { MessageBox.Show("Can't locate site:\n   Pease check the address is correct", "Error"); } }
        private void editBookmarkFour(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkFour = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkFiveClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkFive); URL_Box.Text = Properties.Settings.Default.userBookmarkFive; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkFive(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkFive = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkSixClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkSix); URL_Box.Text = Properties.Settings.Default.userBookmarkSix; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkSix(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkSix = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkSevenClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkSeven); URL_Box.Text = Properties.Settings.Default.userBookmarkSeven; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkSeven(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkSeven = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkEightClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkEight); URL_Box.Text = Properties.Settings.Default.userBookmarkEight; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkEight(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkEight = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }
        private void bookmarkNineClick(object sender, RoutedEventArgs e) { try { webBrowser.Navigate(Properties.Settings.Default.userBookmarkNine); URL_Box.Text = Properties.Settings.Default.userBookmarkNine; } catch { MessageBox.Show("Can't locate site:\n   Please check the address is correct", "Error"); } }
        private void editBookmarkNine(object sender, RoutedEventArgs e) { Properties.Settings.Default.userBookmarkNine = webBrowser.Source.ToString(); Properties.Settings.Default.Save(); }

        /*private void webBrowser_Navigating(object sender, NavigatingCancelEventArgs e) { if (!willNavigate) { willNavigate = true; return; }

            Process[] proc = Process.GetProcessesByName("*Internet Explorer");
            if (proc.Length == 0)
            {
                // run whatever here if process is NOT open
            }
            else
            {
                // run whatever here if process is open
                MessageBox.Show("detected");
            }
            //e.Cancel = true;
            var startInfo = new ProcessStartInfo { FileName = e.Uri.ToString() }; // ¯\_(ツ)_/¯ 
            //MessageBox.Show("boop"); //what to do when nav
        }*/
    } }
