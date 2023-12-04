import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from tkinter import simpledialog

class Event:
    def _init_(self, name, date, venue):
        self.name = name
        self.date = date
        self.venue = venue

class EventManagementSystem:
    def _init_(self, root):
        self.root = root
        self.root.title("Event Management System")

        self.events = []

        # Create a notebook for multiple pages
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)

        # Create and add tabs for each page
        self.create_event_tab()
        self.list_events_tab()
        self.search_events_tab()

        # Bind a window resize event to make the application responsive
        self.root.bind('<Configure>', self.on_resize)

    def create_event_tab(self):
        create_event_frame = ttk.Frame(self.notebook)
        self.notebook.add(create_event_frame, text="Create Event")

        self.name_label = ttk.Label(create_event_frame, text="Event Name:")
        self.name_label.grid(row=0, column=0, padx=10, pady=5, sticky=tk.W)

        self.name_entry = ttk.Entry(create_event_frame)
        self.name_entry.grid(row=0, column=1, padx=10, pady=5)

        self.date_label = ttk.Label(create_event_frame, text="Event Date:")
        self.date_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        # Use the Calendar widget for date input
        self.date_cal = Calendar(create_event_frame, selectmode="day", year=2023, month=8, day=30, background="lightblue")
        self.date_cal.grid(row=1, column=1, padx=10, pady=5)

        self.venue_label = ttk.Label(create_event_frame, text="Event Venue:")
        self.venue_label.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.venue_entry = ttk.Entry(create_event_frame)
        self.venue_entry.grid(row=2, column=1, padx=10, pady=5)

        self.add_event_button = ttk.Button(create_event_frame, text="Add Event", command=self.add_event, style="TButton")
        self.add_event_button.grid(row=3, columnspan=2, pady=10)

    def list_events_tab(self):
        list_events_frame = ttk.Frame(self.notebook)
        self.notebook.add(list_events_frame, text="List Events")

        self.list_frame = ttk.LabelFrame(list_events_frame, text="List of Events", padding=10)
        self.list_frame.pack(fill=tk.BOTH, expand=True)

        list_scrollbar = ttk.Scrollbar(self.list_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(self.list_frame, yscrollcommand=list_scrollbar.set)
        list_scrollbar.config(command=self.listbox.yview)
        list_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.listbox.pack(fill=tk.BOTH, expand=True)

        # Create a button to trigger the "List Events" function
        list_button = ttk.Button(list_events_frame, text="List Events", command=self.list_events, style="TButton")
        list_button.pack(pady=10)

    def search_events_tab(self):
        search_events_frame = ttk.Frame(self.notebook)
        self.notebook.add(search_events_frame, text="Search Events")

        self.search_frame = ttk.LabelFrame(search_events_frame, text="Search Results", padding=10)
        self.search_frame.pack(fill=tk.BOTH, expand=True)

        search_scrollbar = ttk.Scrollbar(self.search_frame, orient=tk.VERTICAL)
        self.search_listbox = tk.Listbox(self.search_frame, yscrollcommand=search_scrollbar.set)
        search_scrollbar.config(command=self.search_listbox.yview)
        search_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.search_listbox.pack(fill=tk.BOTH, expand=True)

        # Create a button to trigger the "Search Events" function
        search_button = ttk.Button(search_events_frame, text="Search Events", command=self.search_events, style="TButton")
        search_button.pack(pady=10)

    def add_event(self):
        event_name = self.name_entry.get()
        event_date = self.date_cal.get_date()
        event_venue = self.venue_entry.get()

        event = Event(event_name, event_date, event_venue)
        self.events.append(event)

        self.name_entry.delete(0, tk.END)
        self.date_cal.set_date("")
        self.venue_entry.delete(0, tk.END)

        self.name_entry.focus()

        print(f"Event Added: {event.name} on {event.date} at {event.venue}")

    def list_events(self):
        self.listbox.delete(0, tk.END)
        for idx, event in enumerate(self.events):
            self.listbox.insert(tk.END, f"{idx + 1}. {event.name} ({event.date}) at {event.venue}")

    def search_events(self):
        self.search_listbox.delete(0, tk.END)
        search_text = simpledialog.askstring("Search Events", "Enter search text:")
        if search_text:
            matching_events = [event for event in self.events if search_text.lower() in event.name.lower()]
            
            if matching_events:
                for idx, event in enumerate(matching_events):
                    self.search_listbox.insert(tk.END, f"{idx + 1}. {event.name} ({event.date}) at {event.venue}")
            else:
                self.search_listbox.insert(tk.END, "No matching events found.")

    def on_resize(self, event):
        # Adjust widget sizes and layouts here based on the window's size
        pass

if _name_ == "_main_":
    root = tk.Tk()
    app = EventManagementSystem(root)
    root.configure(bg="grey")

    style = ttk.Style()
    style.configure("TButton", background="blue", foreground="white")

    root.mainloop()
