import simpy
import random

def car(env, name, car_wash, drying, waxing):
    """Car process that goes through wash, dry, and wax steps."""
    print(f"{name} arriving at car wash at {env.now}")
    with car_wash.request() as request:
        yield request
        print(f"{name} entering car wash at {env.now}")
        yield env.timeout(random.uniform(5, 10))  # Washing takes 5-10 minutes
        print(f"{name} leaving car wash at {env.now}")

    with drying.request() as request:
        yield request
        print(f"{name} entering drying at {env.now}")
        yield env.timeout(random.uniform(3, 7))  # Drying takes 3-7 minutes
        print(f"{name} leaving drying at {env.now}")

    with waxing.request() as request:
        yield request
        print(f"{name} entering waxing at {env.now}")
        yield env.timeout(random.uniform(4, 8))  # Waxing takes 4-8 minutes
        print(f"{name} leaving waxing at {env.now}")

def car_generator(env, car_wash, drying, waxing, arrival_rate, max_queue_length, queue_data, car_wash_data):
    """Generates cars arriving at the car wash and collects data."""
    car_count = 0
    while True:
        if len(car_wash.queue) < max_queue_length:
            car_count += 1
            env.process(car(env, f"Car {car_count}", car_wash, drying, waxing))
        queue_data.append(len(car_wash.queue))
        car_wash_data.append(len(car_wash.users))
        yield env.timeout(random.expovariate(arrival_rate))

def run_simulation_with_data(run_length, num_systems, max_queue_length, arrival_rate):
    """Run the car wash simulation and collect data."""
    env = simpy.Environment()
    car_wash = simpy.Resource(env, capacity=num_systems)
    drying = simpy.Resource(env, capacity=num_systems)
    waxing = simpy.Resource(env, capacity=num_systems)

    queue_data = []
    car_wash_data = []

    env.process(car_generator(env, car_wash, drying, waxing, arrival_rate, max_queue_length, queue_data, car_wash_data))
    env.run(until=run_length)

    return queue_data, car_wash_data

def run_simulation(run_length, num_systems, max_queue_length, arrival_rate):
    """Run the car wash simulation."""
    env = simpy.Environment()
    car_wash = simpy.Resource(env, capacity=num_systems)
    drying = simpy.Resource(env, capacity=num_systems)
    waxing = simpy.Resource(env, capacity=num_systems)

    env.process(car_generator(env, car_wash, drying, waxing, arrival_rate, max_queue_length, [], []))
    env.run(until=run_length)

if __name__ == "__main__":
    run_simulation(run_length=60, num_systems=2, max_queue_length=5, arrival_rate=0.5)
