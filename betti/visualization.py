import matplotlib.pyplot as plt

def plot_diagram(diagram):
    births = [b[0] for b in diagram]
    deaths = [b[1] for b in diagram]
    plt.figure(figsize=(6,6))
    plt.scatter(births, deaths, c='blue', s=30)
    max_val = max(max(births, default=0), max(deaths, default=0))
    plt.plot([0, max_val], [0, max_val], 'r--')
    plt.xlabel("Birth")
    plt.ylabel("Death")
    plt.title("Persistence Diagram")
    plt.show()

def plot_barcode(diagram):
    plt.figure(figsize=(8,4))
    for i, (birth, death) in enumerate(diagram):
        plt.hlines(y=i, xmin=birth, xmax=death, colors='blue', linewidth=2)
    plt.xlabel("Filtration value")
    plt.ylabel("Feature index")
    plt.title("Persistence Barcode")
    plt.show()
