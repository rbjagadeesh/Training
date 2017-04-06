from wxPython.wx import * 
import wx

ID_ABOUT = 101 
ID_EXIT  = 102 

class MyFrame(wxFrame): 
	def __init__(self, parent, ID, title): 
		wxFrame.__init__(self, parent, ID, title, wxDefaultPosition, wxSize(200, 150)) 
		self.CreateStatusBar() 
		self.SetStatusText("This is the statusbar") 
		menu = wxMenu() 
		menu.Append(ID_ABOUT, "&About", "More information about this program") 
		menu.AppendSeparator() 
		menu.Append(ID_EXIT, "E&xit", "Terminate the program") 
		menuBar = wxMenuBar() 
		menuBar.Append(menu, "&File"); 
		self.SetMenuBar(menuBar) 

		EVT_MENU(self, ID_ABOUT, self.OnAbout) 
		EVT_MENU(self, ID_EXIT,  self.TimeToQuit) 

	def OnAbout(self, event): 
		dlg = wxMessageDialog(self, "This sample program shows off\n" 
				"frames, menus, statusbars, and this\n" 
				"message dialog.", 
				"About Me", wxOK | wxICON_INFORMATION) 
		dlg.ShowModal() 
		dlg.Destroy() 

	def TimeToQuit(self, event): 
		self.Close(true) 

if __name__ == "__main__": 
	class myApp(wxApp): 
		def OnInit(self): 
			frame=MyFrame(NULL, -1, "Hello from wxPython") 
			frame.Show(true) 
			self.SetTopWindow(frame) 
			return true 

app = myApp(0) 
app.MainLoop() 
