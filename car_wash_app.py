import streamlit as st
from car_wash_simulation import run_simulation_with_data
import pandas as pd

def main():
    st.title("Car Wash Simulation")

    st.sidebar.header("Simulation Parameters")
    run_length = st.sidebar.number_input("Run Length (minutes)", min_value=1, value=60)
    num_systems = st.sidebar.number_input("Number of Car Wash Systems", min_value=1, value=2)
    max_queue_length = st.sidebar.number_input("Max Queue Length", min_value=1, value=5)
    arrival_rate = st.sidebar.number_input("Arrival Rate (cars per minute)", min_value=0.1, value=0.5, step=0.1)

    if st.button("Run Simulation"):
        st.write("Running simulation...")

        # Run the simulation and collect data
        queue_data, car_wash_data = run_simulation_with_data(run_length, num_systems, max_queue_length, arrival_rate)

        # Create dataframes for visualization
        time_points = list(range(len(queue_data)))
        queue_df = pd.DataFrame({"Time": time_points, "Queue Length": queue_data})
        car_wash_df = pd.DataFrame({"Time": time_points, "Cars in Wash": car_wash_data})

        # Plot queue length as a line chart
        st.write("### Queue Length Over Time")
        st.line_chart(queue_df.set_index("Time"))

        # Plot cars in wash as a column chart
        st.write("### Cars in Wash Over Time")
        st.bar_chart(car_wash_df.set_index("Time"))

        st.write("Simulation complete!")

if __name__ == "__main__":
    main()
