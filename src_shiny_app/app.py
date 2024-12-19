from shiny import ui, render, App
import numpy as np
import matplotlib.pyplot as plt

app_ui = ui.page_fluid(
    ui.row(
        ui.column(
            12,  # Set the width of the column
            ui.input_slider("slider", label="Number of bins", min=1, max=100, value=30)
        )
    ),
    ui.row(
        ui.column(
            12,  # Set the width of the column
            ui.output_plot("histogram")
        )
    )
)

def server(input, output, session):
    @output
    @render.plot
    def histogram():
        x = 100 + np.random.randn(500)
        plt.title("A histogram", size=20)
        plt.hist(x=x, bins=input.slider(), color="grey", ec="black")

app = App(ui=app_ui, server=server)