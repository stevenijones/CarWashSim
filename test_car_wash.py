import pytest
from car_wash_simulation import run_simulation_with_data

def test_run_simulation_with_data():
    # Test with valid inputs
    run_length = 60
    num_systems = 2
    max_queue_length = 5
    arrival_rate = 0.5

    queue_data, car_wash_data, lost_cars_data = run_simulation_with_data(run_length, num_systems, max_queue_length, arrival_rate)

    # Validate the output data
    assert len(queue_data) == run_length
    assert len(car_wash_data) == run_length
    assert len(lost_cars_data) == run_length

    # Ensure lost cars data is non-negative
    assert all(lost >= 0 for lost in lost_cars_data)

    # Test with invalid inputs
    with pytest.raises(ValueError):
        run_simulation_with_data(-1, num_systems, max_queue_length, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, -1, max_queue_length, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, num_systems, -1, arrival_rate)

    with pytest.raises(ValueError):
        run_simulation_with_data(run_length, num_systems, max_queue_length, -0.5)
