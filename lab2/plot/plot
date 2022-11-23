import pandas as pd
import matplotlib.pyplot as plt

def read_csv():
    df1 = pd.read_csv("1_stats_history.csv", usecols=['Requests/s'])
    df3 = pd.read_csv("3_stats_history.csv", usecols=['Requests/s'])
    df4 = pd.read_csv("4_stats_history.csv", usecols=['Requests/s'])

    seconds = list(range(0, 171))

    plt.plot(seconds, df1, label="Local Microservice", color="red")
    plt.plot(seconds, df3, label="Webapp", color="blue")
    plt.plot(seconds, df4, label="Function", color="green")

    plt.xlabel("Seconds")
    plt.ylabel("Request/s")

    plt.legend()
    plt.show()


read_csv()
