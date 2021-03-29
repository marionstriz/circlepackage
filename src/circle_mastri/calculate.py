"""Circle package main functions."""
import math
import tkinter


def calculate_circumference(radius: float):

    if radius < 0:
        raise ValueError("Radius must be positive!")
    return radius * 2 * math.pi


def calculate_area(radius: float):

    if radius < 0:
        raise ValueError("Radius must be positive!")
    return radius ** 2 * math.pi


def circle_data_gui():

    window = tkinter.Tk()

    window.title("Circle Calculations")

    canvas = tkinter.Canvas(window, height=150, width=500, bg="#c2eaee")
    canvas.pack()

    radius = tkinter.Label(window, text="Radius: ", bg="#c2eaee")
    canvas.create_window(180, 25, window=radius)

    radius_input = tkinter.Entry(window, width=15)
    radius_input.focus()
    canvas.create_window(280, 25, window=radius_input)

    circumference = tkinter.Label(window, text="Circumference: ", bg="#c2eaee")
    canvas.create_window(250, 100, window=circumference)

    area = tkinter.Label(window, text="Area: ", bg="#c2eaee")
    canvas.create_window(250, 120, window=area)

    def get_data():

        try:
            circint = calculate_circumference(float(radius_input.get()))
            areaint = calculate_area(float(radius_input.get()))

            circumference.configure(text="Circumference: " + str(circint))
            area.configure(text="Area: " + str(areaint))

        except ValueError:
            error = tkinter.Toplevel()
            error.title("ValueError")
            error_canvas = tkinter.Canvas(error, height=100, width=400, bg="#c2eaee")
            error_canvas.pack()

            error_label = tkinter.Label(error, text="Radius must be a positive number!",
                                        bg="#c2eaee", fg="red", font=("TKDefaultFont", 20))
            error_canvas.create_window(200, 50, window=error_label)

    button = tkinter.Button(text="Calculate", command=get_data)
    canvas.create_window(250, 60, window=button)

    window.mainloop()
