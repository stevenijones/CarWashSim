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
        queue_data, car_wash_data, lost_cars, longest_wait, average_wait, total_reneged = run_simulation_with_data(
            run_length, num_systems, max_queue_length, arrival_rate
        )

        # Ensure the time points cover the entire run length
        time_points = list(range(run_length))

        # Adjust queue_data and car_wash_data to match the run length
        queue_data += [0] * (run_length - len(queue_data))
        car_wash_data += [0] * (run_length - len(car_wash_data))
        lost_cars += [0] * (run_length - len(lost_cars))

        # Display metrics
        st.write("### Simulation Metrics")
        st.write(f"**Longest Wait Time:** {longest_wait:.2f} minutes")
        st.write(f"**Average Wait Time:** {average_wait:.2f} minutes")
        st.write(f"**Total Reneged Cars:** {total_reneged}")
        
        # Create dataframes for visualization
        queue_df = pd.DataFrame({"Time": time_points, "Queue Length": queue_data})
        car_wash_df = pd.DataFrame({"Time": time_points, "Cars in Wash": car_wash_data})
        lost_cars_df = pd.DataFrame({"Time": time_points, "Lost Cars": lost_cars})

        # Plot queue length as a line chart
        st.write("### Queue Length Over Time")
        st.line_chart(queue_df.set_index("Time"))

        # Plot cars in wash as a column chart
        st.write("### Cars in Wash Over Time")
        st.bar_chart(car_wash_df.set_index("Time"))

        # Plot lost cars as a line chart
        st.write("### Lost Cars Over Time")
        st.line_chart(lost_cars_df.set_index("Time"))

        st.write("Simulation complete!")

if __name__ == "__main__":
    main()
