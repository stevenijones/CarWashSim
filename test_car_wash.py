import pytest
from car_wash_simulation import run_simulation_with_data

def test_run_simulation_with_data():
    # Test with valid inputs
    run_length = 60
    num_systems = 2
    max_queue_length = 5
    arrival_rate = 0.5

    # Run the simulation
    queue_data, car_wash_data, lost_cars_data, longest_wait, average_wait, total_reneged = run_simulation_with_data(
        run_length, num_systems, max_queue_length, arrival_rate
    )

    # Validate the output data
    assert len(queue_data) == run_length
    assert len(car_wash_data) == run_length
    assert len(lost_cars_data) == run_length

    # Ensure lost cars data is non-negative
    assert all(lost >= 0 for lost in lost_cars_data)

    # Validate the metrics
    assert longest_wait >= 0  # Longest wait time should be non-negative
    assert average_wait >= 0  # Average wait time should be non-negative
    assert total_reneged >= 0  # Total reneged cars should be non-negative

    # Test with invalid inputs
    with pytest.raises(ValueError):
        run_simulation_with_data(-1, num_systems, max_queue_length, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, -1, max_queue_length, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, num_systems, -1, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, num_systems, max_queue_length, -0.5)
