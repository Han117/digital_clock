import time
import tkinter as tk


class DigitalClock:
    def __init__(self, root: tk.Tk) -> None:
        self.root = root
        self.root.title("Digital Clock")
        self.root.geometry("520x220")
        self.root.configure(bg="#111827")
        self.root.resizable(False, False)


#14行注释  digital_clock
#15行编辑
        self.time_label = tk.Label(
            root,
            text="",
            font=("Consolas", 48, "bold"),
            fg="#22d3ee",
            bg="#111827",
        )
        self.time_label.pack(pady=(40, 10))

        self.date_label = tk.Label(
            root,
            text="",
            font=("Consolas", 20),
            fg="#e5e7eb",
            bg="#111827",
        )
        self.date_label.pack()

        self.update_clock()

    def update_clock(self) -> None:
        current_time = time.strftime("%H:%M:%S")
        current_date = time.strftime("%Y-%m-%d  %A")

        self.time_label.config(text=current_time)
        self.date_label.config(text=current_date)

        self.root.after(1000, self.update_clock)


def main() -> None:
    root = tk.Tk()
    DigitalClock(root)
    root.mainloop()


if __name__ == "__main__":
    main()
