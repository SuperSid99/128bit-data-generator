# creating dataset
if __name__ == "__main__":
    import csv
    import random

    header = []
    for _ in range(128):
        a = [_ + 1]
        header.append(a)

    def generate_datapoint():
        data_point = []
        for _ in range(128):
            data_point.append([random.randint(0, 1)])
        return data_point

    with open("ip_data_train.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for _ in range(10000):
            writer.writerow(generate_datapoint())

    with open("ip_data_test.csv", "w", encoding="UTF8", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(header)
        for _ in range(500):
            writer.writerow(generate_datapoint())
